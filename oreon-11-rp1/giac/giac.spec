%global source0_hash none
%ifarch s390x
%bcond check 1
%else
%bcond check 1
%endif
%bcond_without flexiblas
%bcond_with fltk
%global _lto_cflags %{nil}
%global subversion .19
Name:          giac
Summary:        Computer Algebra System, Symbolic calculus, Geometry
Version:       2.0.0%{subversion}
Release:        1%{?dist}
License:       GPL-3.0-or-later AND GPL-3.0-only AND GPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LGPL-3.0-or-later AND LGPL-2.0-or-later AND MIT
URL:           https://www-fourier.univ-grenoble-alpes.fr/~parisse/giac.html
Source0:        %{name}-%{version}.tar.gz
Source1:       %{name}-makesrc.sh
Patch0:        %{name}-iszero.patch
Patch1:        %{name}-config.patch
Patch2:        %{name}-1.9.0-fix_micropy_compiler_flags.patch
Patch3:        %{name}-cocoalib.patch
Patch4:        %{name}-fix_graphe_file.patch
Patch5:        %{name}-pari2.15.patch
Patch6:        %{name}-undefine_GLIBCXX_ASSERTIONS.patch
Patch7:        %{name}-faking_mkjs.patch
ExcludeArch:   %{ix86}
%ifnarch %{ix86}
%endif
%if %{with flexiblas}
%else
%endif
%if %{with fltk}
%endif
Provides: bundled(tinymt32)
Provides: libmicropython-static = 1.12
Provides: libgiac-static = 1.9.0
Provides: libxcas-static = 1.9.0
%global majver %(cut -d. -f1-3 <<< %{version})
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  cliquer-devel
BuildRequires:  cocoalib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  gmp-ecm-devel
BuildRequires:  gsl-devel
BuildRequires:  hevea
BuildRequires:  libXinerama-devel
BuildRequires:  libao-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libnauty-devel
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mpfi-devel
BuildRequires:  mpfr-devel
BuildRequires:  ntl-devel
BuildRequires:  pari-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  tex(latex)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-stmaryrd
# /oreon:deps
%description
Giac is a Computer Algebra System made by Bernard Parisse. It  provides 
features from the C/C++ libraries PARI, NTL (arithmetic), GSL (numerics), 
GMP (big integers), MPFR (bigfloats) and also
  - Efficient algorithms for multivariate polynomial operations 
        (product, GCD, factorization, groebner bases),
  - Symbolic computations: solver, simplifications, limits/series, integration,
  - Linear algebra with numerical or symbolic coefficients.
  - Partial Maple and TI compatibility.
  - It has interfaces in texmacs and sagemath.

It consists of:
   - a C++ library (libgiac)
   - a command line interpreter (icas/giac)
   - an FLTK-based GUI (xcas) with interactive geometry and formal spreadsheets.

####################
%package devel
Summary: C++ development files for libgiac
Requires: %{name}%{?_isa} = %{version}-%{release}
%if %{with fltk}
Requires: fltk-devel%{?_isa}
%endif
Requires: gsl-devel%{?_isa}
Requires: mpfi-devel%{?_isa}
Requires: ntl-devel%{?_isa}
%description devel
Development files for libgiac.

####################
%package doc
Summary: Detailed HTML documentation for Giac/Xcas
BuildArch: noarch
%ifnarch %{ix86}
BuildRequires: hevea
%endif
BuildRequires: tex(latex), texinfo, texinfo-tex, texlive-stmaryrd
Requires: %{name} = %{version}-%{release}
Obsoletes: giac-doc < 0:2.0.0.18-8
Provides: bundled(CodeMirror)
Provides: bundled(FileSaver.js)
License:   GPL-3.0-or-later AND GFDL-1.1-or-later
%description doc
The detailed  documentation and examples for giac and xcas. It is directly
accessible from xcas in many ways (browser, context search, thematic indexes).
It is strongly recommended for xcas usage. Note that the french part has been 
removed from the original source due to non free Licence.

####################
%package xcas
Summary: GUI application for Giac
Provides: xcas%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme
%description xcas
Xcas is the Fltk graphic user interface to the computer algebra system giac. 
It supports formal computations, interactive 2D geometry, 3D plotting, 
spreadsheets with formal calculus and a Logo mode. There is also a programming 
editor, and many ways to consult the HTML help.

####################
%package -n pgiac
Summary:   Perl script for the computer algebra system Giac
URL:       http://melusine.eu.org/syracuse/giac/pgiac
BuildArch: noarch
BuildRequires: perl-generators
Requires:  %{name} = %{version}-%{release}
%description -n pgiac
The pgiac command is a Perl script to mix Latex documents
with Giac computations.

%prep

%autosetup -n %{name}-%{majver} -N

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p0 -b .backup
%patch -P 3 -p0 -b .backup
%patch -P 4 -p1 -b .backup
%patch -P 5 -p1 -b .backup
%patch -P 6 -p1 -b .backup
%patch -P 7 -p1 -b .backup

# Remove local intl (already bundled in fedora)
rm -rf intl/*.h
rm -rf intl/*.cc

# Remove unecessary files and force the rebuild of info. 
rm -f doc/pari/gphtml
rm -f doc/*/texinfo.tex
rm -f doc/*/giac_*.info

# Some files in the upstream source have unnecessary executable rights
chmod -x src/*.h
chmod -x src/*.cc
find examples -type f -name '*.xws' -exec chmod -x '{}' \;
find examples -type f -name '*.cas' -exec chmod -x '{}' \;
find examples -type f -name '*.cxx' -exec chmod -x '{}' \;
chmod -x examples/lewisw/fermat*
# Clean backups in doc
find doc -name *~ -delete

# Unbundle texinfo file
sed -i 's|config/texinfo.tex|%{_texmf_main}/tex/texinfo/texinfo.tex|g' Makefile.in
rm -f config/texinfo.tex

# Remove hidden files
rm -f examples/Exemples/demo/._*
rm -f examples/Exemples/analyse/._*

%if %{with flexiblas}
sed -e 's|LIB(blas|LIB(flexiblas|g' -e 's|LIB(lapack|LIB(flexiblas|g' \
 -e 's|-lgslcblas|-lflexiblas|' -i configure.ac
%endif

# Prepare Micropython lib's License
cp -p micropython-1.12/LICENSE micropython-1.12/micropython-LICENSE

# Update configure.ac obsolete macros
autoupdate -vf

# Re-configuration
autoreconf -ivf

%build

OPT_FLAGS=$(echo "%build_cxxflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
export CXXFLAGS="$OPT_FLAGS -fpermissive -std=gnu++17"
export CFLAGS_FEDORA="$OPT_FLAGS -std=gnu17"
%configure --enable-static=yes --with-included-gettext=no --enable-nls=no \
 --enable-tommath=no --enable-debug=no --enable-gc=no --enable-sscl=no \
 --enable-dl=yes --enable-gsl=yes --enable-lapack=yes --enable-pari=yes \
 --enable-ntl=yes --enable-gmpxx=yes --enable-cocoa=autodetect \
 --enable-gui=yes --disable-rpath \
%ifarch %{power64}
 --disable-micropy \
%endif
%if %{without fltk}
 --disable-fltk
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export OPT_FLAGS=$(echo "%build_cxxflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
g++ $OPT_FLAGS -fpermissive -std=gnu++17 src/mkjs.cc -o src/mkjs
OPT_FLAGS=$(echo "%build_cflags" | %{__sed} -e 's/-Werror=format-security/-Wno-error=format-security/')
export CXXFLAGS="$OPT_FLAGS -fpermissive -std=gnu++17"
export CFLAGS_FEDORA="$OPT_FLAGS -std=gnu17"
export LDFLAGS_FEDORA="$OPT_FLAGS"
%make_build
(cd doc ; make)
for i in doc/*/giac_*.info doc/en/html_* ; do 
   iconv -f ISO-8859-1 -t UTF-8 -o $i.new $i && \
   touch -r $i $i.new && \
   mv $i.new $i
done
%install
%make_install
%ifnarch %{power64}
install -pm 644 libmicropython.a %{buildroot}%{_libdir}/
%endif
install -pm 644 src/.libs/libxcas.a %{buildroot}%{_libdir}/
install -pm 644 src/.libs/libgiac.a %{buildroot}%{_libdir}/
cp -p src/tinymt32_license.h LICENSE.tinymt32
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/application-registry
rm -f %{buildroot}%{_libdir}/libgiac.la 
find %{buildroot} -size 0 -delete
rm -f %{buildroot}%{_bindir}/xcasnew
rm -f %{buildroot}%{_docdir}/giacwasm.wasm
install -pm 644 -D debian/giac.sharedmimeinfo \
                     %{buildroot}%{_datadir}/mime/packages/giac.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc doc/en/cas*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/en doc/en/*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/el doc/el/*.pdf
install -pm 644 -t %{buildroot}%{_datadir}/giac/doc/es doc/es/*.pdf
find %{buildroot}%{_datadir}/giac -name 'Makefile*' -exec rm {} \;
mkdir -p %{buildroot}%{_datadir}/giac/doc/fr
ln -sf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/fr/aide_cas
ln -sf -T %{_datadir}/giac/doc/aide_cas %{buildroot}%{_datadir}/giac/doc/en/aide_cas
ln -sf -T %{_datadir}/giac/doc/en/casinter/index.html %{buildroot}%{_datadir}/giac/doc/en/casinter/casinter.html
ln -sf -T %{_datadir}/giac/doc/en/cascmd_en/index.html %{buildroot}%{_datadir}/giac/doc/en/cascmd_en/cascmd_en.html
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 debian/giac.1 %{buildroot}%{_mandir}/man1
install -pm 644 debian/cas_help.1 %{buildroot}%{_mandir}/man1
install -pm 644 debian/pgiac.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libexecdir}/giac
cp -p %{buildroot}%{_datadir}/giac/doc/khicas.nwa %{buildroot}%{_libexecdir}/giac/
ln -sfv %{_libexecdir}/giac/khicas.nwa %{buildroot}%{_datadir}/giac/doc/khicas.nwa
desktop-file-install --vendor="" --remove-key=Encoding \
                     --set-key=Version --set-value=1.0 \
                     --dir=%{buildroot}%{_datadir}/applications/ \
                     %{buildroot}%{_datadir}/applications/xcas.desktop
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type f| \
             grep  -E "%{_datadir}/giac/doc/[a-z]{2}/" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/keywords$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/xcasmenu$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}/xcasex$" | \
             sed -e "s:%{buildroot}::" >giacdoclist
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 1 -type f| \
             grep  -v -E "%{_datadir}/giac/doc/aide_cas$" | \
             sed -e "s:%{buildroot}::" >>giacdoclist
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type d| \
             grep  -E "%{_datadir}/giac/doc/[a-z]{2}/" | \
             grep  -v -E "%{_datadir}/giac/doc$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}$" | \
             sed -e "s:%{buildroot}::" | \
             sed -e "s:$:/:" >>giacdoclist
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 1 -type d| \
             grep  -v -E "%{_datadir}/giac/doc$" | \
             grep  -v -E "%{_datadir}/giac/doc/[a-z]{2}$" | \
             sed -e "s:%{buildroot}::" | \
             sed -e "s:$:/:" >>giacdoclist
find  %{buildroot}%{_datadir}/giac/doc -maxdepth 2 -type l| \
             grep  -v -E "%{_datadir}/giac/doc/aide_cas$" | \
             sed -e "s:%{buildroot}::" >>giacdoclist
chmod a+x %{buildroot}%{_datadir}/giac/doc/send18
chmod a+x %{buildroot}%{_datadir}/giac/doc/send19
%fdupes -s %{buildroot}%{_datadir}
%oreon_autofiles pgiac usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C check check
%endif
%files -f %{oreon_filedir}/main.list
%files -n giac-devel -f %{oreon_filedir}/giac-devel.list
%files -n giac-doc -f %{oreon_filedir}/giac-doc.list
%files -n giac-xcas -f %{oreon_filedir}/giac-xcas.list
%files -n pgiac -f %{oreon_filedir}/pgiac.list

%changelog

%autochangelog
