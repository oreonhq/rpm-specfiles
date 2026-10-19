%global source47_hash ced3678a2879b30306d323f4542626697a464a97c0a07c9aebf7ebca65cd4dde
%global source46_hash f17a85883d4e6d00e8a97c586de764dabcc06133f7f1d55dce5cdc070ad7fe59
%global source45_hash 0562428422c63773dad2c345a1882263bbf4d65cf3f42e90921f787ef5ad58e7
%global source44_hash 883478de20367e224c0090af9cf5f9fa85bed63a95c1abf3afc5c083ebc06e8c
%global source43_hash 0b928f33d975fc6ad9f86c8f283853ad26bdd5b10b7f1542aa2fa15e2289105a
%global source42_hash f63a545481291138910575129486daeaf8ac54aee4387fe7906919f7830c7d9d
%global source41_hash 1dccffe3ce07af9386bfd29e80c0ab1a8205a2fc34e4bcd40364df902cfa8f3f
%global source40_hash df7f62577c25e07834649fc3b39fafdc597c0a3527dc1c60129201ccfcbaa50c
%global source39_hash ede7c438028d4436d71104916910f5bb611972c5cfd7f89b8300a8186e6fada6
%global source38_hash 13c2bddecc57b384dee18652358fb23172facb8a2c51ccc10d74c157bdea3292
%global source37_hash a7507d819769d01a365ab707794a4084392c824f54a7a6a7862f8c3d0892b283
%global source36_hash 69cdb34c158ceb288df11e18b4bd39de994f6657d83847bdffdbd7f346754b0f
%global source35_hash 1885c039570dc00dcb4ff087a89e185fd56bae234ddc7f056a945bf36467248d
%global source34_hash 6143877a16e82b5a727b7127ff4cd86858a24a28d745d72f43e6f227c7b1bdb3
%global source33_hash 6100e8a4b5eba53afaa5ed078364851a0b2499c553a44c31026b929049b49dc6
%global source32_hash dfc0b8e19df29aad7086cf977bb0c2a2f143e30567eb113e9cf72b62ca698330
%global source31_hash 7b3fc0c4d08f6bb10e71fe39dfb9e2f59c6eb6854e22ec8092f50c69a4499adb
%global source30_hash 700d18fa267b73b9b521fd7e13580e2f446916f176cacee1ab63fcc8191f1655
%global source29_hash 89ae43fd86e4158d6db51ad8e2b80f313af9cc74f5c0e03ccb87de09998732de
%global source28_hash f84267b20a16ea918e43c6a88433c2d54fa145c92a811b5b047ccbe153674483
%global source27_hash f8ed6a7761f76e3b9f92dfb0a60a6a6477c61024b775147ff0973a02653abaf2
%global source26_hash 42f5e15c9953c5e4ccceeb2e7382a716482c34515315f7b03532b8b4e8393d2d
%global source25_hash 58f929b4d672ea937a23a1ab494143d968337a5f47e56d0815df1e0890ddf174
%global source24_hash 879f10e63c20629ecabbb64a8010319738c66a5cd0c29b02d63d272b03751d01
%global source23_hash 2304e00983f87ffb38b55b444b5e3b60a884b5d30c0fca7d82fe33449bbe55ea
%global source22_hash 26145e563e54f2cadc477553f1ec5ee650b00862f0a58bcd12cbdc5f0ea2d2f4
%global source21_hash 85649ca51fd72272d7821adaf274ad91c288277713d9c18820d8499a7ff69e9a
%global source20_hash 9ed9a281f7bc9b7576e61468ba615a66a5c8cfdff42420a70aa82701a3b1e292
%global source19_hash 1bfb12502f3fc46cca1bb51ac28df9d618d813cdc3d2f25b9fe775a34af26bb3
%global source18_hash 59ed5838eebb26a2bb2e58f6d5b5316989ae9d08bab10e0e6d103e656d1b0280
%global source17_hash 773f3b9af64447d2ce9850330c473515014aa235e6a783b02db81ff39e4a3dad
%global source16_hash 2fd1289c04a9ea8cb22300a459a72a385d7c73d3259e2ed7dcb2af674838cfa9
%global source15_hash 1fd0f2584146f6f2ef48085050886acf353beff7305ebd1ae69500e27c67f64b
%global source14_hash e412e2cd0f2b2d93e02543ceae7917b3c70331573df19ee046bcbc35e45e87d7
%global source13_hash 3078c7629b62d3f0439517fa394996acacc5cbc91c5a20d8c658e77abd503a71
%global source12_hash 6aeac2e1fe888769f34f05ac343bbef98b14d1ffb292ab69d4608b3abc86f2a2
%global source11_hash abaf6da45c74385272ddf00e1ac074c7d8a6c1a1dda376902bd6a427522a8b2c
%global source10_hash 72b3254f16251a8381aa12e40e3c4d2f0199f8c6508fbecb9d91f575e0fbb8c6
%global source0_hash f748f7c2d6fd375cc93d3fba7ef4a9e3a092421b8dbf34d8d4dc06be9492dfdd
Name:           python-bcrypt
Version:        5.0.0
Release:        1%{?dist}
Summary:        Modern password hashing for your software and your servers
License:        Apache-2.0
URL:            https://github.com/pyca/bcrypt/
Source0:        https://files.pythonhosted.org/packages/source/b/bcrypt/bcrypt-%{version}.tar.gz
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
Patch:          python-bcrypt-5.0.0-pyo3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42.0.0
BuildRequires:  python3dist(setuptools-rust) >= 1.7.0
Requires:       python3-bcrypt = %{version}-%{release}
# /oreon:deps
%package -n       python3-bcrypt+tests
Summary:        Metapackage for python3-bcrypt tests extras
Requires:       python3-bcrypt = %{version}-%{release}
Requires:       python3dist(pytest) >= 3.2.1
Provides:       python3dist(bcrypt[tests]) = %{version}-%{release}

%description -n python3-bcrypt+tests
Metapackage for python3-bcrypt tests extras.

%package -n       python3-bcrypt+typecheck
Summary:        Metapackage for python3-bcrypt typecheck extras
Requires:       python3-bcrypt = %{version}-%{release}
Provides:       python3dist(bcrypt[typecheck]) = %{version}-%{release}

%description -n python3-bcrypt+typecheck
Metapackage for python3-bcrypt typecheck extras.

%description

%package -n     python3-bcrypt
Summary:        Modern password hashing for your software and your servers
%description -n python3-bcrypt

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n bcrypt-%{version}
mkdir -p src/_bcrypt/vendor .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored"

[source.vendored]
directory = "src/_bcrypt/vendor"
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

%build

export CARGO_NET_OFFLINE=true
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bcrypt usr/lib/python3*/site-packages/bcrypt* usr/lib64/python3*/site-packages/bcrypt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bcrypt* usr/lib64/python3*/site-packages/bcrypt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bcrypt -f %{oreon_filedir}/python3-bcrypt.list

%changelog

%autochangelog
