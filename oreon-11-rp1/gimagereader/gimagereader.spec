%global source0_hash 4604b53e8d952c68ce4198d7b8d864327ef6afaf597e7909f6b31f0eb9b4c425
Name:          gimagereader
Version:       3.4.3
Release:        2%{?dist}
Summary:        A front-end to tesseract-ocr
License:       GPL-3.0-or-later
URL:           https://github.com/manisandro/gimagereader
Source0:        https://github.com/manisandro/gimagereader/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires:      hicolor-icon-theme
Requires:      gvfs
# oreon:deps
BuildRequires:  cairomm-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceviewmm3-devel
BuildRequires:  gtkspellmm30-devel
BuildRequires:  intltool
BuildRequires:  json-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml++-devel
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  podofo-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  poppler-qt6-devel
BuildRequires:  python3-gobject
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qtspell-qt6-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  sane-backends-devel
BuildRequires:  tesseract-devel
# /oreon:deps
%description
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents

%package gtk
Summary:       A Gtk+ front-end to tesseract-ocr
Requires:      gvfs-client
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{name} < 2.94-1
%description gtk
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Gtk+ front-end.

%package qt
Summary:       A Qt front-end to tesseract-ocr
Requires:      %{name}-common = %{version}-%{release}
%description qt
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Qt front-end.

%package common
Summary:       Common files for %{name}
BuildArch:     noarch
%description common
Common files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _vpath_builddir %{_target_platform}-gtk
%cmake -DINTERFACE_TYPE=gtk -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common"
%cmake_build
%define _vpath_builddir %{_target_platform}-qt
%cmake -DINTERFACE_TYPE=qt6 -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common"
%cmake_build
%install
%define _vpath_builddir %{_target_platform}-gtk
%cmake_install
%define _vpath_builddir %{_target_platform}-qt
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-gtk.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt6.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-gtk.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-qt6.appdata.xml
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gimagereader-gtk -f %{oreon_filedir}/gimagereader-gtk.list
%files -n gimagereader-qt -f %{oreon_filedir}/gimagereader-qt.list
%files -n gimagereader-common -f %{oreon_filedir}/gimagereader-common.list

%changelog

%autochangelog
