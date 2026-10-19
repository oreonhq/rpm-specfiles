%global source0_hash 0e7edc5b9669349acfda99533e9e0bcf26a51862ab43b08ee7745c55d28eb134
%bcond check 0
%global debug_package %{nil}
%global crate freetype-sys
Name:           rust-freetype-sys0.20
Version:        0.20.1
Release:        1%{?dist}
Summary:        Low level binding for FreeType font library
License:        MIT
URL:            https://crates.io/crates/freetype-sys
Source0:        https://static.crates.io/crates/freetype-sys/freetype-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(freetype2) >= 24.3.18
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low level binding for FreeType font library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -vr freetype2
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
%files -n rust-freetype-sys0.20-devel -f %{oreon_filedir}/rust-freetype-sys0.20-devel.list

%changelog

%autochangelog
