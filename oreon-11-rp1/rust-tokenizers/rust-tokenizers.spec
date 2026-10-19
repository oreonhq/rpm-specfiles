%global source0_hash b238e22d44a15349529690fb07bd645cf58149a1b1e44d6cb5bd1641ff1a6223
%bcond check 1
%global debug_package %{nil}
%global crate tokenizers
Name:           rust-tokenizers
Version:        0.22.2
Release:        1%{?dist}
Summary:        Implementation of today's most used tokenizers in Rust
License:        Apache-2.0
URL:            https://crates.io/crates/tokenizers
Source0:        https://static.crates.io/crates/tokenizers/tokenizers-%{version}.crate
Patch:          tokenizers-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+esaxx_fast-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+esaxx_fast-devel

This package contains library source intended for building other packages which
use the "esaxx_fast" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-regex-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+fancy-regex-devel

This package contains library source intended for building other packages which
use the "fancy-regex" feature of the "%{crate}" crate.

%package     -n %{name}+hf-hub-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+hf-hub-devel

This package contains library source intended for building other packages which
use the "hf-hub" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+indicatif-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+indicatif-devel

This package contains library source intended for building other packages which
use the "indicatif" feature of the "%{crate}" crate.

%package     -n %{name}+onig-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+onig-devel

This package contains library source intended for building other packages which
use the "onig" feature of the "%{crate}" crate.

%package     -n %{name}+progressbar-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+progressbar-devel

This package contains library source intended for building other packages which
use the "progressbar" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-devel
Summary:        Implementation of today's most used tokenizers in Rust
BuildArch:      noarch
%description -n %{name}+rustls-tls-devel

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --doc -- --skip 926
%{cargo_test -- --test added_tokens -- --exact %{shrink:
    --skip lstrip_tokens
    --skip overlapping_tokens
    --skip rstrip_tokens
    --skip single_word_tokens
}}
%cargo_test -- --test from_pretrained
%{cargo_test -- --test serialization -- --exact %{shrink:
    --skip bpe_serde
    --skip test_deserialize_long_file
    --skip wordlevel_serde
    --skip wordpiece_serde
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tokenizers-devel -f %{oreon_filedir}/rust-tokenizers-devel.list

%changelog

%autochangelog
