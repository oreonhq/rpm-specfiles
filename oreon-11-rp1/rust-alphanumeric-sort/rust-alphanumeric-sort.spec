%global source0_hash 774ffdfeac16e9b4d75e41225dc2545d9c2082a0634b5d7f6f70e168546eecb1
%bcond check 1
%global debug_package %{nil}
%global crate alphanumeric-sort
Name:           rust-alphanumeric-sort
Version:        1.5.5
Release:        1%{?dist}
Summary:        Can help you sort order for files and folders whose names contain numerals
License:        MIT
URL:            https://crates.io/crates/alphanumeric-sort
Source0:        https://static.crates.io/crates/alphanumeric-sort/alphanumeric-sort-%{version}.crate
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
Summary:        Can help you sort order for files and folders whose names contain numerals
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Can help you sort order for files and folders whose names contain numerals
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
%files -n rust-alphanumeric-sort-devel -f %{oreon_filedir}/rust-alphanumeric-sort-devel.list

%changelog

%autochangelog
