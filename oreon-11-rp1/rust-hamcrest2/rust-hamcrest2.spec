%global source0_hash 49f837c62de05dc9cc71ff6486cd85de8856a330395ae338a04bfcefe5e91075
%bcond check 0
%global debug_package %{nil}
%global crate hamcrest2
Name:           rust-hamcrest2
Version:        0.3.0
Release:        1%{?dist}
Summary:        Port of the Hamcrest testing library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hamcrest2
Source0:        https://static.crates.io/crates/hamcrest2/hamcrest2-%{version}.crate
Patch:          hamcrest2-fix-metadata.diff
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
Summary:        Port of the Hamcrest testing library
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
%files -n rust-hamcrest2-devel -f %{oreon_filedir}/rust-hamcrest2-devel.list

%changelog

%autochangelog
