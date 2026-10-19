%global source0_hash 43bb73a7fa3799b198970490a51174027ba0d4ec504b03cd08caf513d40024bc
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate open
Name:           rust-open
Version:        5.3.3
Release:        1%{?dist}
Summary:        Open a path or URL using the program configured on the system
License:        MIT
URL:            https://crates.io/crates/open
Source0:        https://static.crates.io/crates/open/open-%{version}.crate
Patch:          open-fix-metadata-auto.diff
Patch:          open-fix-metadata.diff
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
Summary:        Open a path or URL using the program configured on the system
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
%files -n rust-open-devel -f %{oreon_filedir}/rust-open-devel.list

%changelog

%autochangelog
