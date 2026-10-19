%global source0_hash 1679e6ea370dee694f91f1dc469bf94cf8f52051d147aec3e1f9497c6fc22461
%bcond check 0
%global debug_package %{nil}
%global crate heapsize
Name:           rust-heapsize
Version:        0.4.2
Release:        1%{?dist}
Summary:        Infrastructure for measuring the total runtime size of an object on t...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/heapsize
Source0:        https://static.crates.io/crates/heapsize/heapsize-%{version}.crate
Patch:          heapsize-fix-metadata-auto.diff
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

%package     -n %{name}+flexible-tests-devel
Summary:        Infrastructure for measuring the total runtime size of an object on t...
BuildArch:      noarch
%description -n %{name}+flexible-tests-devel

This package contains library source intended for building other packages which
use the "flexible-tests" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Infrastructure for measuring the total runtime size of an object on t...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-heapsize-devel -f %{oreon_filedir}/rust-heapsize-devel.list

%changelog

%autochangelog
