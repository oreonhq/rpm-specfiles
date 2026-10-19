%global source0_hash b6277f0217056f77f1d8f49f2950ac6c278c0d607c45f5ee99328d792ede24ec
%bcond check 0
%global debug_package %{nil}
%global crate sctk-adwaita
Name:           rust-sctk-adwaita
Version:        0.10.1
Release:        1%{?dist}
Summary:        Adwaita-like SCTK Frame
License:        MIT
URL:            https://crates.io/crates/sctk-adwaita
Source0:        https://static.crates.io/crates/sctk-adwaita/sctk-adwaita-%{version}.crate
Patch2:        sctk-adwaita-0.5.4-unbundle-cantarell-font.patch
# oreon:deps
BuildRequires:  abattis-cantarell-fonts
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
Summary:        Adwaita-like SCTK Frame
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ab_glyph-devel
Summary:        Adwaita-like SCTK Frame
BuildArch:      noarch
Requires:       abattis-cantarell-fonts
%description -n %{name}+ab_glyph-devel

This package contains library source intended for building other packages which
use the "ab_glyph" feature of the "%{crate}" crate.

%package     -n %{name}+crossfont-devel
Summary:        Adwaita-like SCTK Frame
BuildArch:      noarch
%description -n %{name}+crossfont-devel

This package contains library source intended for building other packages which
use the "crossfont" feature of the "%{crate}" crate.

%package     -n %{name}+memmap2-devel
Summary:        Adwaita-like SCTK Frame
BuildArch:      noarch
%description -n %{name}+memmap2-devel

This package contains library source intended for building other packages which
use the "memmap2" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -f src/title/*.ttf
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
%files -n rust-sctk-adwaita-devel -f %{oreon_filedir}/rust-sctk-adwaita-devel.list

%changelog

%autochangelog
