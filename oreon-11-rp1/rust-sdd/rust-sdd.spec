%global source0_hash a31877eee03686b905845993b5d9809a220c9dd5a10e9d6021d7ca67384c9070
%bcond check 0
%global debug_package %{nil}
%global crate sdd
Name:           rust-sdd
Version:        4.8.11
Release:        1%{?dist}
Summary:        Scalable lock-free delayed memory reclaimer
License:        Apache-2.0
URL:            https://crates.io/crates/sdd
Source0:        https://static.crates.io/crates/sdd/sdd-%{version}.crate
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
Summary:        Scalable lock-free delayed memory reclaimer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+loom-devel
Summary:        Scalable lock-free delayed memory reclaimer
BuildArch:      noarch
%description -n %{name}+loom-devel

This package contains library source intended for building other packages which
use the "loom" feature of the "%{crate}" crate.

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
%files -n rust-sdd-devel -f %{oreon_filedir}/rust-sdd-devel.list

%changelog

%autochangelog
