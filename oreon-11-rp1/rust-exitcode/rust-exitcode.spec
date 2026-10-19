%global source0_hash de853764b47027c2e862a995c34978ffa63c1501f2e15f987ba11bd4f9bba193
%bcond check 0
%global debug_package %{nil}
%global crate exitcode
Name:           rust-exitcode
Version:        1.1.2
Release:        1%{?dist}
Summary:        Preferred system exit codes as defined by sysexits.h
License:        Apache-2.0
URL:            https://crates.io/crates/exitcode
Source0:        https://static.crates.io/crates/exitcode/exitcode-%{version}.crate
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
Summary:        Preferred system exit codes as defined by sysexits.h
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-exitcode-devel -f %{oreon_filedir}/rust-exitcode-devel.list

%changelog

%autochangelog
