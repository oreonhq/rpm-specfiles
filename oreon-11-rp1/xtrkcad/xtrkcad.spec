%global source0_hash 5b02a0352c23f90b0011029c7e2c3f12a6f6779425c4c47c1f75d6b8a0db572c

Name: xtrkcad
Summary: CAD for Model Railroad layout
Version: 5.3.1
Release: 2%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://sourceforge.net/projects/xtrkcad-fork
Source0: https://sourceforge.net/projects/xtrkcad-fork/files/XTrackCad/Version%20%{version}/xtrkcad-source-%{version}GA.tar.gz
# fix build to use dynamic libzip
Patch0: xtrkcad-5.3.1GA.libzip.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 2.4.7
BuildRequires: pkgconfig
BuildRequires: gtk2-devel
BuildRequires: libzip-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRequires: glibc-devel
BuildRequires: pandoc
BuildRequires: doxygen
BuildRequires: cjson-devel
BuildRequires: mxml
BuildRequires: mxml-devel
BuildRequires: freeimage
BuildRequires: freeimage-devel
BuildRequires: inkscape
BuildRequires: inkscape-libs

Requires: xdg-utils

%description
XTrkCad is a CAD program for designing Model Railroad layouts.
XTrkCad supports any scale, has libraries of popular brands of x
turnouts and sectional track (plus you add your own easily), can
automatically use spiral transition curves when joining track
XTrkCad lets you manipulate track much like you would with actual
flex-track to modify, extend and join tracks and turnouts.
Additional features include tunnels, 'post-it' notes, on-screen
ruler, parts list, 99 drawing layers, undo/redo commands,
benchwork, 'Print to BitMap', elevations, train simulation and
car inventory. Documents/help is in xtrkcad-doc rpm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n xtrkcad-source-%{version}GA -q
%patch 0 -p1

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains user documentation and help for XTrkCAD,
in HTML format. It also contains demos, and examples.

%build
%cmake -DBUILD_SHARED_LIBS=OFF -DXTRKCAD_USE_DOXYGEN=ON
%cmake_build

%install
%cmake_install

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications \
	%{buildroot}/%{_datadir}/%{name}/applications/xtrkcad.desktop
rm %{buildroot}/%{_datadir}/%{name}/applications/xtrkcad.desktop

mkdir -p %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}/%{_datadir}/%{name}/pixmaps/xtrkcad.png \
	%{buildroot}/%{_datadir}/pixmaps/xtrkcad.png
rm -rf %{buildroot}/%{_datadir}/%{name}/pixmaps

mkdir -p %{buildroot}/%{_datadir}/mime/packages
mv %{buildroot}/%{_datadir}/%{name}/applications/xtrkcad.xml \
	%{buildroot}/%{_datadir}/mime/packages/xtrkcad.xml

# Tests require a feature in the next release
#%check
#%ctest

%files
%license app/COPYING
%{_bindir}/%{name}
%{_datadir}/applications/xtrkcad.desktop
%{_datadir}/pixmaps/xtrkcad.png
%{_datadir}/mime/packages/xtrkcad.xml
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/demos
%exclude %{_datadir}/%{name}/examples
%exclude %{_datadir}/%{name}/html

%files doc
%{_datadir}/%{name}/demos
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/html
%{_datadir}/locale/cy_GB/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/de_DE/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/fr_FR/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ru/LC_MESSAGES/%{name}.mo

%changelog
%autochangelog
