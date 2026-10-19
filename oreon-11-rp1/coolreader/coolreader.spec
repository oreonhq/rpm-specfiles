%global source0_hash 54253ce3da8f3575d7e64f0afd3d2e9d369ca4e785584cfad4462eead1b8f51e
Name:           coolreader
Version:        3.2.59
Release:        1%{?dist}
Summary:        Cross platform open source e-book reader
%global forgeurl https://github.com/buggins/coolreader
%global tag cr%{version}
%forgemeta
License:        GPL-2.0-or-later
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:        cr3.appdata.xml
Patch:          0001-Set-CMake-policy-version-lower-bound-to-3.5.patch
ExcludeArch:    %{ix86}
Provides:       bundled(antiword) = 0.37
Provides:       bundled(chmlib) = 0.38
Provides:       bundled(qt5-qtbase-private)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libunibreak)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
CoolReader is fast and small cross-platform XML/CSS based eBook reader for
desktops and handheld devices. Supported formats: FB2, TXT, RTF, DOC, TCR,
HTML, EPUB, CHM, PDB, MOBI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

mkdir -p %{_vpath_builddir}
%cmake \
  -DGUI=QT5 \
  -DCMAKE_BUILD_TYPE=Release \
  -DMAX_IMAGE_SCALE_MUL=2 \
  -DDOC_DATA_COMPRESSION_LEVEL=3 \
  -DDOC_BUFFER_SIZE=0x1400000 \
  -D CMAKE_INSTALL_PREFIX=/usr \
  .
%cmake_build
%install
%cmake_install
install -D -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/cr3.appdata.xml
%find_lang cr3 --with-qt --without-mo
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/cr3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/cr3.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
