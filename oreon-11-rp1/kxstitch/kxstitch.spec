%global source0_hash 4c230b47873b660f3232f74e536a1cb3e6f32bbd0ec436b36b1d9a8fd9a6cbe0

%undefine __cmake_in_source_build

Name: kxstitch
Summary: Program to create cross stitch patterns
Version: 2.2.0
Release: 9%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://userbase.kde.org/KXStitch
Source0: http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  extra-cmake-modules

%description
KXStitch can be used to create cross stitch patterns from scratch. It is also
possible to convert existing images to a cross stitch pattern or scan one with 
a Sane supported scanner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde || touch %{name}.lang

# move docs to Fedora standard directory
mkdir -p %{buildroot}/%{_docdir}/%{name}/
mv %{buildroot}/%{_datadir}/doc/HTML %{buildroot}/%{_docdir}/%{name}/
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/{128x128,16x16,256x256,48x48,64x64,scalable}/
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/

%check
desktop-file-validate "%{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop"

%find_lang %{name} --with-kde

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_docdir}/%{name}/HTML/
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/22x22/actions/*
%{_datadir}/kxmlgui5/%{name}/
%{_datadir}/config.kcfg/%{name}.kcfg
%{_mandir}/*

%changelog
%autochangelog
