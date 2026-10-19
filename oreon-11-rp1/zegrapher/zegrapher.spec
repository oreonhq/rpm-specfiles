%global source1_hash ab27d0d28b384013f27814be17dddbcc6abfd196e8db10e10652a26e7a4c4e9f
%global source0_hash e50c999903c66e7fbd204dcbc7e177aba0194d692977d7d8186b0452cc2ee1fc
%global gitdate 20260105
%global commit 70d26fbca881b99a0a58c16f3802339e38c924eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           zegrapher
Summary:        Free and opensource math graphing software
Version:        3.1.1^%{gitdate}git%{shortcommit}
Release:        1%{?dist}
License:        AGPL-3.0-or-later
URL:            https://www.zegrapher.com/
Source0:        https://github.com/AdelKS/ZeGrapher/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/AdelKS/ZeCalculator/archive/v0.12.3/ZeCalculator-v0.12.3.tar.gz
Provides:       bundled(zecalculator) = 0.12.3
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
ZeGrapher is a plotting program for functions, sequences, parametric equations,
and tabular data. It has been designed to be as easy to use as possible.

ZeGrapher supports importing and exporting of tabular data from and to CSV files
and polynomial (regression) fits, plotting of tangents (the point can be
selected interactively). Calculation and plotting of derivatives and integrals
is also possible.

Plots can be exported in various image formats and as PDF files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir -p subprojects/zecalculator
tar xf %{SOURCE1} -C subprojects/zecalculator --strip-components=1

sed -i "s|meson.project_version()|'%{version}'|" meson.build

%build

%meson --buildtype=debugoptimized -Dtest=true
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
