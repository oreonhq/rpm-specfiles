%global source1_hash 6725d1437fc6c77301f2ff0e7d52914cf4f9509213e1078dc77d9356dbe6eac5
%global source0_hash 6184e33543162437515c2e2b48714794e37845ec9851711914eec9d308f6ebe8
%bcond check 0
%global debug_package %{nil}
%global crate difflib
Name:           rust-difflib
Version:        0.4.0
Release:        1%{?dist}
Summary:        Port of Python's difflib library to Rust
License:        MIT
URL:            https://crates.io/crates/difflib
Source0:        https://static.crates.io/crates/difflib/difflib-%{version}.crate
Source1:        https://github.com/DimaKudosh/difflib/raw/f035fb8/LICENSE
Patch:          difflib-fix-metadata.diff
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
Summary:        Port of Python's difflib library to Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-difflib-devel -f %{oreon_filedir}/rust-difflib-devel.list

%changelog

%autochangelog
