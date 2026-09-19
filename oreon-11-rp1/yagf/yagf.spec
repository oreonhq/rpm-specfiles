%global source0_hash c0e9fe4b16d39378319fe37772403104a81c58084aa918e78347f56456ed5ebc

%global __cmake_in_source_build 1

Name:           yagf
Version:        0.9.5
Release:        27%{?dist}
Summary:        Graphical front-end for cuneiform

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/yagf-ocr/
Source:         https://downloads.sourceforge.net/yagf-ocr/files/%{name}-%{version}.tar.gz

# fix .desktop file
Patch1:         yagf-0.9.1-Source-desktop.patch
Patch2:         yagf-0.9.5-nothreads.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  aspell-devel
BuildRequires:  qt4-devel
BuildRequires:  dos2unix
Requires:       tesseract

%description
YAGF is a graphical interface for the cuneiform text
recognition program. With YAGF you can scan images via
XSane, perform images preprocessing and recognize
texts using cuneiform from a single command center.
YAGF also makes it easy to scan and recognize
several images sequentially.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .desktop
%patch -P2 -p1 -b .nothreads

# fix line brake for debug package
dos2unix src/mainform.cpp src/mainform.h

# fix permisions
chmod 644 src/mainform.cpp src/mainform.h src/main.cpp

%build
# TODO: Please submit an issue to upstream (rhbz#2381646)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# CMakeLists.txt constructed in such a way that
# translations can't be installed from %%{_target_platform}
%cmake
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/YAGF.desktop

%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING DESCRIPTION README
%{_bindir}/%{name}
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/applications/YAGF.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/YAGF.appdata.xml

%changelog
%autochangelog
