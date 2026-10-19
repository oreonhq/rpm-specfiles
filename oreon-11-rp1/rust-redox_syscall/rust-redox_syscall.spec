%global source0_hash 4722d768eff46b75989dd134e5c353f0d6296e5aaa3132e776cbdb56be7731aa
%bcond check 0
%global debug_package %{nil}
%global crate redox_syscall
Name:           rust-redox_syscall
Version:        0.4.1
Release:        1%{?dist}
Summary:        Redox system calls interface
License:        MIT
URL:            https://crates.io/crates/redox_syscall
Source0:        https://static.crates.io/crates/redox_syscall/redox_syscall-%{version}.crate
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
use the "redox_syscall" crate.

%package     -n %{name}+default-devel
Summary:        Redox system calls interface
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-redox_syscall-devel -f %{oreon_filedir}/rust-redox_syscall-devel.list

%changelog

%autochangelog
