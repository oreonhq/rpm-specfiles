%global source0_hash 24d4c7647d67c53194fa0740404c6c508880aef2bfe99a9868dbb4b86f090377
%bcond check 0
%global debug_package %{nil}
%global crate botan
Name:           rust-botan
Version:        0.11.1
Release:        1%{?dist}
Summary:        Rust wrapper for Botan cryptography library
License:        MIT
URL:            https://crates.io/crates/botan
Source0:        https://static.crates.io/crates/botan/botan-%{version}.crate
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
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+botan3-devel
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+botan3-devel

This package contains library source intended for building other packages which
use the "botan3" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Rust wrapper for Botan cryptography library
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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
%files -n rust-botan-devel -f %{oreon_filedir}/rust-botan-devel.list

%changelog

%autochangelog
