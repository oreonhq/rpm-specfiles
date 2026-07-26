%global source0_hash 2f30f781d5f3334ccac353482a623ec0846314f7e3e1de7afc8823c24651d906

Name:          gimagereader
Version:       3.4.3
Release:       2%{?dist}
Summary:       A front-end to tesseract-ocr

License:       GPL-3.0-or-later
URL:           https://github.com/manisandro/gimagereader
Source0:       https://github.com/manisandro/gimagereader/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: djvulibre-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: make
BuildRequires: podofo-devel
BuildRequires: sane-backends-devel
BuildRequires: tesseract-devel

BuildRequires: cairomm-devel
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
%if 0%{fedora} > 26
BuildRequires: libxml++30-devel
%else
BuildRequires: libxml++-devel
%endif
BuildRequires: libuuid-devel
BuildRequires: libzip-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtksourceviewmm3-devel
BuildRequires: gtkspellmm30-devel
BuildRequires: json-glib-devel
BuildRequires: poppler-glib-devel
BuildRequires: python3-gobject
BuildRequires: gobject-introspection

BuildRequires: poppler-qt6-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qtspell-qt6-devel
BuildRequires: quazip-qt6-devel

Requires:      hicolor-icon-theme
Requires:      gvfs

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
# For glib networking operations
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

%autosetup -p1

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

%files common -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%doc %{_defaultdocdir}/%{name}-common/manual*.html

%files gtk
%{_bindir}/%{name}-gtk
%{_datadir}/metainfo/%{name}-gtk.appdata.xml
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%files qt
%{_bindir}/%{name}-qt6
%{_datadir}/metainfo/%{name}-qt6.appdata.xml
%{_datadir}/applications/%{name}-qt6.desktop

%changelog
%autochangelog
