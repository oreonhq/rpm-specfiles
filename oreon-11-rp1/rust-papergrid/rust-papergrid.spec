%global source0_hash c7419ad52a7de9b60d33e11085a0fe3df1fbd5926aa3f93d3dd53afbc9e86725
%bcond check 1
%global debug_package %{nil}
%global crate papergrid
Name:           rust-papergrid
Version:        0.12.0
Release:        1%{?dist}
Summary:        Core library to print a table
License:        MIT
URL:            https://crates.io/crates/papergrid
Source0:        https://static.crates.io/crates/papergrid/papergrid-%{version}.crate
Patch:          papergrid-fix-metadata.diff
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
Summary:        Core library to print a table
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Core library to print a table
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-str-devel
Summary:        Core library to print a table
BuildArch:      noarch
%description -n %{name}+ansi-str-devel

This package contains library source intended for building other packages which
use the "ansi-str" feature of the "%{crate}" crate.

%package     -n %{name}+ansitok-devel
Summary:        Core library to print a table
BuildArch:      noarch
%description -n %{name}+ansitok-devel

This package contains library source intended for building other packages which
use the "ansitok" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Core library to print a table
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
%files -n rust-papergrid-devel -f %{oreon_filedir}/rust-papergrid-devel.list

%changelog

%autochangelog
