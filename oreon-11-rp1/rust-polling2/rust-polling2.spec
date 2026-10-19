%global source0_hash 4b2d323e8ca7996b3e23126511a523f7e62924d93ecd5ae73b333815b0eb3dce
%bcond check 0
%global debug_package %{nil}
%global crate polling
Name:           rust-polling2
Version:        2.8.0
Release:        1%{?dist}
Summary:        Portable interface to epoll, kqueue, event ports, and IOCP
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/polling
Source0:        https://static.crates.io/crates/polling/polling-%{version}.crate
Patch:          polling-fix-metadata-auto.diff
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
Summary:        Portable interface to epoll, kqueue, event ports, and IOCP
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Portable interface to epoll, kqueue, event ports, and IOCP
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-polling2-devel -f %{oreon_filedir}/rust-polling2-devel.list

%changelog

%autochangelog
