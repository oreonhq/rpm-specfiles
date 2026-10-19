%global source0_hash d8748972699ec5b99570e031841f449612e266d2106de7482ad76de003cfddba
%bcond check 1
%global debug_package %{nil}
%global crate fb_procfs
Name:           rust-fb_procfs
Version:        0.9.0
Release:        1%{?dist}
Summary:        A crate for reading procfs
License:        Apache-2.0
URL:            https://crates.io/crates/fb_procfs
Source0:        https://static.crates.io/crates/fb_procfs/fb_procfs-%{version}.crate
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
Summary:        A crate for reading procfs
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
%files -n rust-fb_procfs-devel -f %{oreon_filedir}/rust-fb_procfs-devel.list

%changelog

%autochangelog
