%global source0_hash b1acbc46b960480c4959213714511e22f9a2e0d361520693bcf5057b5924f53e
%bcond check 0
%global debug_package %{nil}
%global crate encase
Name:           rust-encase
Version:        0.12.1
Release:        1%{?dist}
Summary:        Provides a mechanism to lay out data into GPU buffers ensuring WGSL's...
License:        MIT-0
URL:            https://crates.io/crates/encase
Source0:        https://static.crates.io/crates/encase/encase-%{version}.crate
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
Summary:        Provides a mechanism to lay out data into GPU buffers ensuring WGSL's...
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
%files -n rust-encase-devel -f %{oreon_filedir}/rust-encase-devel.list

%changelog

%autochangelog
