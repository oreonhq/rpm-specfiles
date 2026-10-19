%global source0_hash a1dce859f0832a7d088c4f1119888ab94ef4b5d6795d1ce05afb7fe159d79f98
%bcond check 1
%global debug_package %{nil}
%global crate cc
Name:           rust-cc
Version:        1.2.62
Release:        1%{?dist}
Summary:        Build-time dependency for Cargo build scripts to invoke the native C compiler
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cc
Source0:        https://static.crates.io/crates/cc/cc-%{version}.crate
# oreon:deps
BuildRequires:  /usr/bin/g++
BuildRequires:  /usr/bin/gcc
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/gcc
Requires:       /usr/bin/g++
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Build-time dependency for Cargo build scripts to invoke the native C compiler
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+jobserver-devel
Summary:        Build-time dependency for Cargo build scripts to invoke the native C compiler
BuildArch:      noarch
%description -n %{name}+jobserver-devel

This package contains library source intended for building other packages which
use the "jobserver" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Build-time dependency for Cargo build scripts to invoke the native C compiler
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

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
%files -n rust-cc-devel -f %{oreon_filedir}/rust-cc-devel.list

%changelog

%autochangelog
