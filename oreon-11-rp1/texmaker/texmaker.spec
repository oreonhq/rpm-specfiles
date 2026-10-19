%global source0_hash 25ecbb16d156ed1528b31511d37c9da7858a2def328b87f17fc877f57f5139cf
Summary:        LaTeX editor
Name:		texmaker
Version:	6.0.2
Release:        1%{?dist}
Epoch:		1
License:	GPL-2.0-or-later
URL:		http://www.xm1math.net/texmaker/
Source0:        http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2
ExclusiveArch: %{qt6_qtwebengine_arches}
Requires:	tetex-latex
Patch0:		%{name}-unbundle.patch
Patch1:		%{name}-%{version}-viewfiles.patch
Patch2:		texmaker-fix-build-against-qt-6-10.patch
Provides: bundled(encodingprober)
Provides: bundled(pdfium)
Provides: bundled(synctex)
Provides: bundled(agg23)
Provides: bundled(base)
Provides: bundled(bigint)
Provides: bundled(libopenjpeg) = 2.0
# oreon:deps
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  hunspell-devel
BuildRequires:  lcms2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  poppler-qt6-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  turbojpeg
BuildRequires:  zlib-devel
# /oreon:deps
%description
Texmaker is a program, that integrates many tools needed to develop 
documents with LaTeX, in just one application. 
Texmaker runs on unix, macosx and windows systems and is released under the GPL
license

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .unbundle
%patch -P1 -p0
%patch -P2 -p1

# remove bundled stuff (hunspell and qtsingleapplication)
# libtiff, pymock appear to be unused by anything
rm -r 3rdparty/{hunspell,singleapp,pdfium/third_party/{lcms,libjpeg,libpng,libtiff,pymock,zlib}*}
# pdfium needs an internal freetype header pstables.h
find 3rdparty/pdfium/third_party/freetype -name pstables.h -o -type f -delete

%build

export CXXFLAGS="%{optflags} -DUSE_SYSTEM_LIBJPEG"
%cmake
%cmake_build
%install
%cmake_install
install -Dp -m 0644 datas/distrib/linux/texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker22x22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/texmaker.png
rm -r %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,tex*.png}
rm -f %{buildroot}%{_datadir}/applications/texmaker.desktop
desktop-file-install 		\
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category Publishing			\
	--remove-category X-SuSE-Core-Office		\
	--remove-category X-Mandriva-Office-Publishing	\
	--remove-category X-Misc			\
	datas/distrib/linux/texmaker.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
