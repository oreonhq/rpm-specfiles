%global source0_hash bbce5753a1e08b871a5cf16c665eb060700aaab9a6a379dc63f4c4d9b3b8856e
%global source1_hash 09f6eccc35df0e2a9c28cc40b15e1a280e253a5851ce6d610a40311ac04178de
%global source10_hash b532dc469e6dfb996b4a9a223a88f69eeb854918af63f0961c53348aee558010
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%bcond_with check
%bcond_with toolchain_clang
%if %{with toolchain_clang}
%global toolchain clang
%endif
%global inkscape_date 2023-11-16
%global date %(d=%{inkscape_date}; echo ${d//-/})
%global commit 91b66b078370477bd794fe0e1db149c34333dae8
%global shortcommit %(c=%{commit}; echo ${c:0:10})
Name:           inkscape
Version:        1.4.4
Release:        1%{?dist}
Summary:        Vector-based drawing program using SVG
License:        GPL-2.0-or-later AND CC-BY-3.0
URL:            https://inkscape.org/
Source0:        https://media.inkscape.org/dl/resources/file/inkscape-%{version}.tar.xz
Source1:        https://media.inkscape.org/media/resources/sigs/inkscape-1.4.4_2026-05-05_dcaf3e7d9e.tar.xz.sig
Source10:       https://inkscape.org/~MarcJeanmougin/gpg/#/MarcJeanmougin.gpg
Source100:      Fedora-Color-Palette.gpl
Patch:          inkscape-1.4.4-poppler-26.08.0.patch
Provides: bundled(libcroco) = 0.6.99~gitb9e4b47
Provides: bundled(autotrace) = 0.40.0~git0de6201
Provides: bundled(libdepixelize) = 0~git19b7601
Provides: bundled(libuemf) = 0.2.8
Provides: bundled(adaptagrams) = 0~gitc8e3196
%if %{with toolchain_clang}
%else
%endif
%if %{with check}
%endif
%global gtk3_version 3.24
%if %{with imagemagick}
%endif
%if %{with graphicsmagick}
%endif
%if %{with toolchain_clang}
%endif
Requires:       python%{python3_pkgversion}-libs >= 3.7
Requires:       %{py3_dist inkex}
Requires:       python%{python3_pkgversion}-appdirs
Suggests:       pstoedit
Suggests:       tex(latex)
Suggests:       tex(dvips)
Suggests:       texlive-amsmath
Suggests:       texlive-amsfonts
Suggests:       texlive-standalone
# oreon:deps
BuildRequires:  //bin/bc
BuildRequires:  //bin/convert
BuildRequires:  boost-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  cmake(double-conversion)
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libomp-devel
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  potrace-devel
BuildRequires:  python3-rpm-macros
# /oreon:deps
%description
Inkscape is a vector graphics editor, with capabilities similar to
Illustrator, CorelDraw, or Xara X, using the W3C standard Scalable Vector
Graphics (SVG) file format.  It is therefore a very useful tool for web
designers and as an interchange format for desktop publishing.

Inkscape supports many advanced SVG features (markers, clones, alpha
blending, etc.) and great care is taken in designing a streamlined
interface. It is very easy to edit nodes, perform complex path operations,
trace bitmaps and much more.

%package libs
Summary:        Shared libraries for Inkscape
%description libs
This package provides base libraries to share between Inkscape and Inkview.

%package view
Summary:        Viewing program for SVG files
%description view
Viewer for files in W3C standard Scalable Vector Graphics (SVG) file
format.

%package docs
Summary:        Documentation for Inkscape
%description docs
Tutorial and examples for Inkscape, a graphics editor for vector
graphics in W3C standard Scalable Vector Graphics (SVG) file format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE10}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n inkscape-1.4.4_2026-05-05_dcaf3e7d9e -p1
%py3_shebang_fix .

# https://bugs.launchpad.net/inkscape/+bug/314381
# A couple of files have executable bits set,
# despite not being executable
find . -name '*.cpp' -print0 | xargs -0 chmod -x
find . -name '*.h' -print0 | xargs -0 chmod -x

%build

%cmake \
        -DWITH_GRAPHICS_MAGICK=%{?with_graphicsmagick:ON}%{!?with_graphicsmagick:OFF} \
        -DWITH_IMAGE_MAGICK=%{?with_imagemagick:ON}%{!?with_imagemagick:OFF} \
        -DBUILD_TESTING:BOOL=%{?with_check:ON}%{!?with_check:OFF}
%cmake_build
%install
%cmake_install
install -pm 644 %{SOURCE100} %{buildroot}%{_datadir}/inkscape/palettes/
%find_lang %{name} --with-man
rm -rf %{buildroot}%{_datadir}/inkscape/doc
rm -f %{buildroot}%{_datadir}/doc/inkscape/copyright
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/inkex
ln -s %{python3_sitelib}/inkex %{buildroot}%{_datadir}/inkscape/extensions/inkex
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
%ctest
%endif
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%pretrans -p <lua>

-- Remove directories that will become symlinks
dirs = {"%{_datadir}/inkscape/extensions/inkex"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
%files -f %{oreon_filedir}/main.list
%files -n inkscape-libs -f %{oreon_filedir}/inkscape-libs.list
%files -n inkscape-view -f %{oreon_filedir}/inkscape-view.list
%files -n inkscape-docs -f %{oreon_filedir}/inkscape-docs.list

%changelog

%autochangelog
