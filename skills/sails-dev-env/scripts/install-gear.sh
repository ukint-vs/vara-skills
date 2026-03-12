#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install the latest official Gear binary release.

Usage:
  install-gear.sh [--tag TAG] [--target TARGET] [--to DEST]

Options:
  --tag TAG       Release tag to install. Defaults to the latest GitHub release.
  --target TARGET Archive target triple. Defaults from uname.
  --to DEST       Destination directory. Defaults to $HOME/.local/bin.
  -h, --help      Show this help.
EOF
}

need() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'error: need %s\n' "$1" >&2
    exit 1
  }
}

tag=""
target=""
dest="${HOME}/.local/bin"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tag)
      tag="${2:?missing value for --tag}"
      shift 2
      ;;
    --target)
      target="${2:?missing value for --target}"
      shift 2
      ;;
    --to)
      dest="${2:?missing value for --to}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'error: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

need curl
need tar
need xz
need mktemp
need install
need uname

if [[ -z "${tag}" ]]; then
  tag="$(
    curl --proto '=https' --tlsv1.2 -sSf https://api.github.com/repos/gear-tech/gear/releases/latest |
      grep '"tag_name"' |
      cut -d'"' -f4
  )"
fi

if [[ -z "${target}" ]]; then
  case "$(uname -m)-$(uname -s)" in
    arm64-Darwin)
      target="aarch64-apple-darwin"
      ;;
    x86_64-Darwin)
      target="x86_64-apple-darwin"
      ;;
    aarch64-Linux)
      target="aarch64-unknown-linux-gnu"
      ;;
    x86_64-Linux)
      target="x86_64-unknown-linux-gnu"
      ;;
    *)
      printf 'error: unsupported platform, pass --target explicitly\n' >&2
      exit 1
      ;;
  esac
fi

archive_name="gear-${tag}-${target}.tar.xz"
archive_url="https://get.gear.rs/${archive_name}"
tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT

curl --proto '=https' --tlsv1.2 -sSfL "${archive_url}" -o "${tmpdir}/${archive_name}"
tar -C "${tmpdir}" -xf "${tmpdir}/${archive_name}"

mkdir -p "${dest}"
for candidate in "${tmpdir}"/*; do
  if [[ -x "${candidate}" && -f "${candidate}" ]]; then
    install -m 755 "${candidate}" "${dest}"
  fi
done

printf 'installed gear release %s to %s\n' "${tag}" "${dest}"
