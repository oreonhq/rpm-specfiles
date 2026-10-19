%global source0_hash e838401fb2873bad417e6a03179014c748746f67311cb7317ab14fc0881fa9f0
%bcond check 0
%global debug_package %{nil}
%global crate pasetors
Name:           rust-pasetors
Version:        0.7.8
Release:        1%{?dist}
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
License:        MIT
URL:            https://crates.io/crates/pasetors
Source0:        https://static.crates.io/crates/pasetors/pasetors-%{version}.crate
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
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ed25519-compact-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+ed25519-compact-devel

This package contains library source intended for building other packages which
use the "ed25519-compact" feature of the "%{crate}" crate.

%package     -n %{name}+orion-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+orion-devel

This package contains library source intended for building other packages which
use the "orion" feature of the "%{crate}" crate.

%package     -n %{name}+p384-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+p384-devel

This package contains library source intended for building other packages which
use the "p384" feature of the "%{crate}" crate.

%package     -n %{name}+paserk-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+paserk-devel

This package contains library source intended for building other packages which
use the "paserk" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+v2-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+v2-devel

This package contains library source intended for building other packages which
use the "v2" feature of the "%{crate}" crate.

%package     -n %{name}+v3-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+v3-devel

This package contains library source intended for building other packages which
use the "v3" feature of the "%{crate}" crate.

%package     -n %{name}+v4-devel
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust)
BuildArch:      noarch
%description -n %{name}+v4-devel

This package contains library source intended for building other packages which
use the "v4" feature of the "%{crate}" crate.

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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-pasetors-devel -f %{oreon_filedir}/rust-pasetors-devel.list

%changelog

%autochangelog
