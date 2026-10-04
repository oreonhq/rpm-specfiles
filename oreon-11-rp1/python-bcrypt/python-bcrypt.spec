%global source0_hash f748f7c2d6fd375cc93d3fba7ef4a9e3a092421b8dbf34d8d4dc06be9492dfdd

Name:           python-bcrypt
Version:        5.0.0
Release:        %autorelease
Summary:        Modern password hashing for your software and your servers
License:        Apache-2.0
URL:            https://github.com/pyca/bcrypt/
Source:         %{pypi_source bcrypt}
Source10:        https://static.crates.io/crates/base64/base64-0.22.1.crate
Source11:        https://static.crates.io/crates/bcrypt/bcrypt-0.17.1.crate
Source12:        https://static.crates.io/crates/bcrypt-pbkdf/bcrypt-pbkdf-0.10.0.crate
Source13:        https://static.crates.io/crates/block-buffer/block-buffer-0.10.4.crate
Source14:        https://static.crates.io/crates/blowfish/blowfish-0.9.1.crate
Source15:        https://static.crates.io/crates/byteorder/byteorder-1.5.0.crate
Source16:        https://static.crates.io/crates/cfg-if/cfg-if-1.0.3.crate
Source17:        https://static.crates.io/crates/cipher/cipher-0.4.4.crate
Source18:        https://static.crates.io/crates/cpufeatures/cpufeatures-0.2.17.crate
Source19:        https://static.crates.io/crates/crypto-common/crypto-common-0.1.6.crate
Source20:        https://static.crates.io/crates/digest/digest-0.10.7.crate
Source21:        https://static.crates.io/crates/generic-array/generic-array-0.14.7.crate
Source22:        https://static.crates.io/crates/getrandom/getrandom-0.3.3.crate
Source23:        https://static.crates.io/crates/heck/heck-0.5.0.crate
Source24:        https://static.crates.io/crates/inout/inout-0.1.4.crate
Source25:        https://static.crates.io/crates/libc/libc-0.2.176.crate
Source26:        https://static.crates.io/crates/once_cell/once_cell-1.21.3.crate
Source27:        https://static.crates.io/crates/pbkdf2/pbkdf2-0.12.2.crate
Source28:        https://static.crates.io/crates/portable-atomic/portable-atomic-1.11.1.crate
Source29:        https://static.crates.io/crates/proc-macro2/proc-macro2-1.0.101.crate
Source30:        https://static.crates.io/crates/pyo3/pyo3-0.29.3.crate
Source31:        https://static.crates.io/crates/pyo3-build-config/pyo3-build-config-0.29.3.crate
Source32:        https://static.crates.io/crates/pyo3-ffi/pyo3-ffi-0.29.3.crate
Source33:        https://static.crates.io/crates/pyo3-macros/pyo3-macros-0.29.3.crate
Source34:        https://static.crates.io/crates/pyo3-macros-backend/pyo3-macros-backend-0.29.3.crate
Source35:        https://static.crates.io/crates/quote/quote-1.0.40.crate
Source36:        https://static.crates.io/crates/r-efi/r-efi-5.3.0.crate
Source37:        https://static.crates.io/crates/sha2/sha2-0.10.9.crate
Source38:        https://static.crates.io/crates/subtle/subtle-2.6.1.crate
Source39:        https://static.crates.io/crates/syn/syn-2.0.106.crate
Source40:        https://static.crates.io/crates/target-lexicon/target-lexicon-0.13.3.crate
Source41:        https://static.crates.io/crates/typenum/typenum-1.18.0.crate
Source42:        https://static.crates.io/crates/unicode-ident/unicode-ident-1.0.19.crate
Source43:        https://static.crates.io/crates/version_check/version_check-0.9.5.crate
Source44:        https://static.crates.io/crates/wasi/wasi-0.14.7+wasi-0.2.4.crate
Source45:        https://static.crates.io/crates/wasip2/wasip2-1.0.1+wasi-0.2.4.crate
Source46:        https://static.crates.io/crates/wit-bindgen/wit-bindgen-0.46.0.crate
Source47:        https://static.crates.io/crates/zeroize/zeroize-1.8.1.crate

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  rust

%global _description %{expand:
Modern password hashing for your software and your servers.}

Patch:          python-bcrypt-5.0.0-pyo3.patch

%description %_description

%package -n     python3-bcrypt
Summary:        %{summary}

%description -n python3-bcrypt %_description

%pyproject_extras_subpkg -n python3-bcrypt tests

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n bcrypt-%{version}
mkdir -p src/_bcrypt/vendor src/_bcrypt/.cargo
cat > src/_bcrypt/.cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored"

[source.vendored]
directory = "vendor"
EOF
vendor_one() {
  dir="src/_bcrypt/vendor/${1}-${2}"
  tar -xzf "$3" -C src/_bcrypt/vendor
  python3 - "$dir" "$3" << 'PY'
import hashlib, json, sys
from pathlib import Path
root = Path(sys.argv[1])
crate = Path(sys.argv[2])
files = {}
for p in root.rglob("*"):
    if p.is_file():
        files[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
pkg = hashlib.sha256(crate.read_bytes()).hexdigest()
(root / ".cargo-checksum.json").write_text(json.dumps({"files": files, "package": pkg}, separators=(",", ":")))
PY
}
vendor_one base64 0.22.1 %{SOURCE10}
vendor_one bcrypt 0.17.1 %{SOURCE11}
vendor_one bcrypt-pbkdf 0.10.0 %{SOURCE12}
vendor_one block-buffer 0.10.4 %{SOURCE13}
vendor_one blowfish 0.9.1 %{SOURCE14}
vendor_one byteorder 1.5.0 %{SOURCE15}
vendor_one cfg-if 1.0.3 %{SOURCE16}
vendor_one cipher 0.4.4 %{SOURCE17}
vendor_one cpufeatures 0.2.17 %{SOURCE18}
vendor_one crypto-common 0.1.6 %{SOURCE19}
vendor_one digest 0.10.7 %{SOURCE20}
vendor_one generic-array 0.14.7 %{SOURCE21}
vendor_one getrandom 0.3.3 %{SOURCE22}
vendor_one heck 0.5.0 %{SOURCE23}
vendor_one inout 0.1.4 %{SOURCE24}
vendor_one libc 0.2.176 %{SOURCE25}
vendor_one once_cell 1.21.3 %{SOURCE26}
vendor_one pbkdf2 0.12.2 %{SOURCE27}
vendor_one portable-atomic 1.11.1 %{SOURCE28}
vendor_one proc-macro2 1.0.101 %{SOURCE29}
vendor_one pyo3 0.29.3 %{SOURCE30}
vendor_one pyo3-build-config 0.29.3 %{SOURCE31}
vendor_one pyo3-ffi 0.29.3 %{SOURCE32}
vendor_one pyo3-macros 0.29.3 %{SOURCE33}
vendor_one pyo3-macros-backend 0.29.3 %{SOURCE34}
vendor_one quote 1.0.40 %{SOURCE35}
vendor_one r-efi 5.3.0 %{SOURCE36}
vendor_one sha2 0.10.9 %{SOURCE37}
vendor_one subtle 2.6.1 %{SOURCE38}
vendor_one syn 2.0.106 %{SOURCE39}
vendor_one target-lexicon 0.13.3 %{SOURCE40}
vendor_one typenum 1.18.0 %{SOURCE41}
vendor_one unicode-ident 1.0.19 %{SOURCE42}
vendor_one version_check 0.9.5 %{SOURCE43}
vendor_one wasi 0.14.7+wasi-0.2.4 %{SOURCE44}
vendor_one wasip2 1.0.1+wasi-0.2.4 %{SOURCE45}
vendor_one wit-bindgen 0.46.0 %{SOURCE46}
vendor_one zeroize 1.8.1 %{SOURCE47}

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*' +auto

%check
%_pyproject_check_import_allow_no_modules -t

%files -n python3-bcrypt -f %{pyproject_files}

%changelog
%autochangelog
