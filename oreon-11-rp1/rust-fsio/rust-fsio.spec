%global source0_hash f4944f16eb6a05b4b2b79986b4786867bb275f52882adea798f17cc2588f25b2
%bcond check 1
%global debug_package %{nil}
%global crate fsio
Name:           rust-fsio
Version:        0.4.1
Release:        1%{?dist}
Summary:        File System and Path utility functions
License:        Apache-2.0
URL:            https://crates.io/crates/fsio
Source0:        https://static.crates.io/crates/fsio/fsio-%{version}.crate
Patch:          fsio-fix-metadata-auto.diff
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
Summary:        File System and Path utility functions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        File System and Path utility functions
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+temp-path-devel
Summary:        File System and Path utility functions
BuildArch:      noarch
%description -n %{name}+temp-path-devel

This package contains library source intended for building other packages which
use the "temp-path" feature of the "%{crate}" crate.

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
%files -n rust-fsio-devel -f %{oreon_filedir}/rust-fsio-devel.list

%changelog

%autochangelog
