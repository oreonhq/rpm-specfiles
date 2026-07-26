%global source0_hash none

Name:           asymptote
Version:        3.06
Release:        1%{?dist}
Summary:        Descriptive vector graphics language

# LGPL-3.0-or-later: the project as a whole
# LGPL-2.0-only:
# - tr.{cc,h}
# LGPL-2.0-or-later:
# - rounding.h
# LGPL-2.1-or-later:
# - getopt.h
# - examples/cpkcolors.asy
# GPL-2.0-or-later:
# - doc/asy-latex.dtx
# - doc/asymptote.sty
# GPL-3.0-or-later WITH Bison-exception-2.2:
# - camp.tab.{cc,h}
# Apache-2.0:
# - base/smoothcontour3.asy
# - LspCpp/src/jsonrpc/Context.cpp
# - LspCpp/src/jsonrpc/RemoteEndPoint.cpp
# - LspCpp/src/lsp/Markup.cpp
# - LspCpp/include/LibLsp/JsonRpc/Context.h
# - LspCpp/include/LibLsp/JsonRpc/ScopeExit.h
# - LspCpp/include/LibLsp/JsonRpc/future.h
# - LspCpp/include/LibLsp/JsonRpc/traits.h
# BSL-1.0:
# - LspCpp/include/LibLsp/JsonRpc/macro_map.h
# MIT:
# - LspCpp (except for the Apache-2.0 and BSL-1.0 files above)
# - base/lmfit.asy
# - gl-matrix-2.4.0-pruned
# BSD-3-Clause:
# - cudareflect/tinyexr
License:        LGPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND Apache-2.0 AND BSL-1.0 AND MIT AND BSD-3-Clause
URL:            https://asymptote.sourceforge.io/
Source0:        https://download.sourceforge.net/sourceforge/asymptote/asymptote-%{version}.src.tgz
Source1:        io.github.vectorgraphics.asymptote.desktop
Source2:        io.github.vectorgraphics.asymptote.metainfo.xml
Patch0:         asymptote-2.84-settings.patch
# This doesn't need to go upstream. We put the info file in the topdir, not a subdir, so we need this fix.
Patch1:         asymptote-2.73-info-path-fix.patch
# Link with flexiblas instead of gslcblas
Patch2:         asymptote-3.00-flexiblas.patch
# Unbundle glew
Patch3:         asymptote-3.00-unbundle-glew.patch
# Fix gc linking
Patch4:		asymptote-3.00-gc-link-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  bison, flex
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  fftw-devel >= 3.0
BuildRequires:  gc-devel >= 6.8
BuildRequires:  gsl-devel
BuildRequires:  flexiblas-devel
BuildRequires:  tex(latex) tex(epsf.tex)
BuildRequires:  tex(media9.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(type1ec.sty)
BuildRequires:  texlive-dvisvgm
BuildRequires:  ghostscript >= 9.55
BuildRequires:  texinfo-tex
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  libglvnd-devel
BuildRequires:  emacs
BuildRequires:  libtirpc-devel
BuildRequires:  eigen3-static
BuildRequires:  libcurl-devel
BuildRequires:  libsigsegv-devel
%if 0%{?fedora} >= 42
BuildRequires:  mesa-compat-libOSMesa-devel
%else
BuildRequires:  mesa-libOSMesa-devel
%endif
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glm-devel
BuildRequires:  boost-devel, rapidjson-devel
BuildRequires:  cmake, make, python3-qt5

Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
Requires:       hicolor-icon-theme
Requires:       librsvg2-tools
Requires:       tex(latex)
Requires:       texlive-dvisvgm
Requires:       python3-qt5
Requires:       python3-cson
Requires:       python3-numpy
Recommends:     evince, xdg-utils

Provides:       bundled(LspCpp) = 1.0.0
Provides:       bundled(gl-matrix) = 2.4.0
Provides:       bundled(tinyexr) = 1.0.1

%global texpkgdir   %{_texmf}/tex/latex/%{name}

%description
Asymptote is a powerful descriptive vector graphics language for technical
drawings, inspired by MetaPost but with an improved C++-like syntax.
Asymptote provides for figures the same high-quality level of typesetting
that LaTeX does for scientific text.

%prep
%setup -q
%patch -P0 -p1 -b .settings
%patch -P1 -p1 -b .path-fix
%patch -P2 -p1 -b .flexiblas
%patch -P3 -p1 -b .glew
%patch -P4 -p1 -b .gcfix
sed -i 's/\r//' doc/CAD1.asy

# Make sure the bundled glew cannot be used
rm -rf GL

# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 -o examples/interpolate1.asy{.utf8,}
mv examples/interpolate1.asy{.utf8,}
autoreconf -i

# Remove useless shebangs
for f in GUI/*.py; do
  if [ "$f" != "GUI/xasy.py" ]; then
    sed -i.orig '/\/usr\/bin\/env python3/d' $f
    touch -r $f.orig $f
    rm $f.orig
  fi
done

%build
export CPPFLAGS='-I%{_includedir}/eigen3 -I%{_includedir}/tirpc'
export LIBS='-lflexiblas '
%configure --enable-gc --with-docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}/} --with-latex=%{_texmf}/tex/latex --with-context=%{_texmf}/tex/context/ --enable-lsp --enable-offscreen
%make_build
make doc/version.texi
cd doc/
make all

# Generate an SVG icon
../asy -dir ../base -config "" -render=0 -f svg -o icon icon.asy

%install
%make_install 

install -p -m 644 BUGS ChangeLog README ReleaseNotes TODO \
    %{buildroot}%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Emacs files
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/*.el %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_emacs_sitelispdir}/%{name}/asy-init.el %{buildroot}%{_emacs_sitestartdir}
for i in %{buildroot}%{_emacs_sitelispdir}/%{name}/*.el; do
   %{_emacs_bytecompile} $i
done

# Vim syntax file(s)
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/syntax
pushd %{buildroot}%{_datadir}/vim/vimfiles/syntax
ln -s ../../../%{name}/asy.vim .
popd
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
pushd %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
ln -s ../../../%{name}/asy_filetype.vim .
popd

# Move info file
mv %{buildroot}%{_infodir}/asymptote/asymptote.info %{buildroot}%{_infodir}/asymptote.info

# Copy icon to scalable icon dir
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p doc/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/asy.svg

# Install the desktop file
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.github.vectorgraphics.asymptote.metainfo.xml

# Clean up symlink
rm -rf %{buildroot}%{_bindir}/xasy
cd %{buildroot}%{_bindir}
ln -s ../share/%{name}/GUI/xasy.py xasy

# Fix executable bits
chmod 755 %{buildroot}%{_datadir}/%{name}/{asy-kate.sh,asymptote.py}

%files
%doc %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}/}
%license LICENSE LICENSE.LESSER
%{_bindir}/*
%{_datadir}/%{name}/
%{texpkgdir}/
%{_texmf}/tex/context/
%{_mandir}/man1/*.1*
%{_infodir}/*.info*
%{_datadir}/vim/vimfiles/syntax/asy.vim
%{_datadir}/vim/vimfiles/ftdetect/asy_filetype.vim
%{_datadir}/icons/hicolor/scalable/apps/asy.svg
%{_datadir}/applications/io.github.vectorgraphics.asymptote.desktop
%{_metainfodir}/io.github.vectorgraphics.asymptote.metainfo.xml
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{name}/

%changelog
%autochangelog
