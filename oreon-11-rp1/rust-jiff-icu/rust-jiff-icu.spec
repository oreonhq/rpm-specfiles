%global source0_hash 0e67c2beaae8b10a82d849b9aabb698a43a682f32b17bcdc035d5ecadb44d646
%bcond check 1
%global debug_package %{nil}
%global crate jiff-icu
Name:           rust-jiff-icu
Version:        0.2.2
Release:        1%{?dist}
Summary:        Conversion routines between Jiff and ICU4X
License:        Unlicense OR MIT
URL:            https://crates.io/crates/jiff-icu
Source0:        https://static.crates.io/crates/jiff-icu/jiff-icu-%{version}.crate
Patch:          jiff-icu-fix-metadata.diff
Patch10:        0001-Downstream-only-ignore-doctests-that-would-require-t.patch
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
Summary:        Conversion routines between Jiff and ICU4X
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Conversion routines between Jiff and ICU4X
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Conversion routines between Jiff and ICU4X
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Conversion routines between Jiff and ICU4X
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+zoned-devel
Summary:        Conversion routines between Jiff and ICU4X
BuildArch:      noarch
%description -n %{name}+zoned-devel

This package contains library source intended for building other packages which
use the "zoned" feature of the "%{crate}" crate.

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
%files -n rust-jiff-icu-devel -f %{oreon_filedir}/rust-jiff-icu-devel.list

%changelog

%autochangelog
