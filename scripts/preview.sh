#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
if ! command -v node >/dev/null 2>&1; then
  for runtime in "$PWD"/.tools/node-*/bin; do
    if [ -x "$runtime/node" ]; then
      PATH="$runtime:$PATH"
      export PATH
      break
    fi
  done
fi
if ! command -v node >/dev/null 2>&1; then
  echo "Node.js 22.12+ est nécessaire. Consultez README.md." >&2
  exit 1
fi
npm run build
exec npm run preview -- "$@"
