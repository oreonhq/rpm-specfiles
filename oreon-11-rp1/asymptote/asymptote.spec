%global source0_hash 5cc861968fe8102fc5564b6075db2837dd5698672688b3bfb71406c0da0f8cef
Name:           asymptote
Version:        3.06
Release:        1%{?dist}
Summary:        Descriptive vector graphics language
License:        LGPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND Apache-2.0 AND BSL-1.0 AND MIT AND BSD-3-Clause
URL:            https://asymptote.sourceforge.io/
Source0:        https://download.sourceforge.net/sourceforge/asymptote/asymptote-%{version}.src.tgz
Source1:        io.github.vectorgraphics.asymptote.desktop
Source2:        io.github.vectorgraphics.asymptote.metainfo.xml
Patch0:         asymptote-2.84-settings.patch
Patch1:         asymptote-2.73-info-path-fix.patch
Patch2:         asymptote-3.00-flexiblas.patch
Patch3:         asymptote-3.00-unbundle-glew.patch
Patch4:		asymptote-3.00-gc-link-fix.patch
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
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-static
BuildRequires:  emacs
BuildRequires:  fftw-devel
BuildRequires:  flex
BuildRequires:  flexiblas-devel
BuildRequires:  freeglut-devel
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  gsl-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-compat-libOSMesa-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-qt5
BuildRequires:  rapidjson-devel
BuildRequires:  readline-devel
BuildRequires:  tex(epsf.tex)
BuildRequires:  tex(latex)
BuildRequires:  tex(media9.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(type1ec.sty)
BuildRequires:  texinfo-tex
BuildRequires:  texlive-dvisvgm
BuildRequires:  zlib-devel
# /oreon:deps
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
../asy -dir ../base -config "" -render=0 -f svg -o icon icon.asy
%install
%make_install 
install -p -m 644 BUGS ChangeLog README ReleaseNotes TODO \
    %{buildroot}%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/*.el %{buildroot}%{_emacs_sitelispdir}/%{name}
mv %{buildroot}%{_emacs_sitelispdir}/%{name}/asy-init.el %{buildroot}%{_emacs_sitestartdir}
for i in %{buildroot}%{_emacs_sitelispdir}/%{name}/*.el; do
   %{_emacs_bytecompile} $i
done
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/syntax
pushd %{buildroot}%{_datadir}/vim/vimfiles/syntax
ln -s ../../../%{name}/asy.vim .
popd
install -dm 755 %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
pushd %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
ln -s ../../../%{name}/asy_filetype.vim .
popd
mv %{buildroot}%{_infodir}/asymptote/asymptote.info %{buildroot}%{_infodir}/asymptote.info
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p doc/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/asy.svg
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.github.vectorgraphics.asymptote.metainfo.xml
rm -rf %{buildroot}%{_bindir}/xasy
cd %{buildroot}%{_bindir}
ln -s ../share/%{name}/GUI/xasy.py xasy
chmod 755 %{buildroot}%{_datadir}/%{name}/{asy-kate.sh,asymptote.py}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
