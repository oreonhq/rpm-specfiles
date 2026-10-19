%global source0_hash e3e64c58c4c88fc1045e8fe98a1b7cec3643187e3dd678f9bbcdd8f12a6933d6
%bcond check 0
%global debug_package %{nil}
%global crate quick-junit
Name:           rust-quick-junit
Version:        0.6.0
Release:        1%{?dist}
Summary:        Data model, serializer, and deserializer for JUnit/XUnit XML
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/quick-junit
Source0:        https://static.crates.io/crates/quick-junit/quick-junit-%{version}.crate
Patch:          quick-junit-fix-metadata.diff
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
Summary:        Data model, serializer, and deserializer for JUnit/XUnit XML
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
%files -n rust-quick-junit-devel -f %{oreon_filedir}/rust-quick-junit-devel.list

%changelog

%autochangelog
