%global source0_hash none

# We need +x on these files
%global __brp_mangle_shebangs_exclude_from %{_libdir}/R/bin/

# The additional linker flags break binary R- packages
# https://bugzilla.redhat.com/show_bug.cgi?id=2046246
%undefine _package_note_flags

# EPEL-only issues in some architectures (gcc < 12?)
%if 0%{?rhel} && "%{_arch}" != "x86_64"
%bcond_with tests
%else
%bcond_without tests
%endif

# We don't want the tex provides that generate here
%global __provides_exclude tex\\\(.*\\\)

# We need at least gcc 10
%if 0%{?rhel} && 0%{?rhel} < 9
%global _lto_cflags %nil
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

# Should be the previous version, to make mass-rebuilds easier
%bcond_with bootstrap
%global bootstrap_abi 4.5

%global major_version 4
%global minor_version 6
%global patch_version 0

Name:           R
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        %autorelease
Summary:        A language for data analysis and graphics

License:        GPL-2.0-or-later
URL:            https://www.r-project.org
Source0:        https://cran.r-project.org/src/base/R-4/R-.tar.gz
# see https://bugzilla.redhat.com/show_bug.cgi?id=1324145
Patch0:         R-3.3.0-fix-java_path-in-javareconf.patch

BuildRequires:  gcc-gfortran
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  libcurl-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libzstd-devel
BuildRequires:  tre-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libICE-devel
BuildRequires:  libXt-devel
BuildRequires:  libXmu-devel
BuildRequires:  libicu-devel
BuildRequires:  libtirpc-devel
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
%ifarch %{java_arches}
BuildRequires:  java-devel
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  less
BuildRequires:  texlive
BuildRequires:  texinfo-tex
BuildRequires:  tex(upquote.sty)
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-times

%if 0%{?fedora} || 0%{?oreon}
# No inconsolata on RHEL tex
BuildRequires:  tex(inconsolata.sty)
%endif

# R-devel will pull everything else
Requires:       R-devel%{?_isa} = %{version}-%{release}

%description
This is a metapackage that provides both core R userspace and
all R development components.

R is a language and environment for statistical computing and graphics.
R is similar to the award-winning S system, which was developed at
Bell Laboratories by John Chambers et al. It provides a wide
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

%package core
Summary:        The minimal R components necessary for a functional runtime
Requires:       libRmath%{?_isa} = %{version}-%{release}
Requires:       tzdata
Requires:       less
Requires:       xdg-utils
Requires:       zip, unzip

%ifnarch %{java_arches}
Provides:       R-java = %{version}-%{release}
Obsoletes:      R-java < 4.1.3-3
%endif

# This is our ABI provides to prevent mismatched installs.
# R packages should autogenerate a Requires: R(ABI) based on the R they were built against.
Provides:       R(ABI) = %{major_version}.%{minor_version}
%if %{with bootstrap}
Provides:       R(ABI) = %{bootstrap_abi}
%endif

# These are the submodules that R-core provides. Sometimes R modules say they
# depend on one of these submodules rather than just R. These are provided for
# packager convenience.
%define add_submodule() %{lua:
  local name = rpm.expand("%1")
  local version = rpm.expand("%2")
  local rpm_version = string.gsub(version, "-", ".")
  print("Provides: R-" .. name .. " = " .. rpm_version .. "\\n")
  print("Provides: R(" .. name .. ") = " .. rpm_version)
}
%add_submodule  base %{version}
%add_submodule  boot 1.3-32
%add_submodule  class 7.3-23
%add_submodule  cluster 2.1.8.2
%add_submodule  codetools 0.2-20
%add_submodule  compiler %{version}
%add_submodule  datasets %{version}
%add_submodule  foreign 0.8-91
%add_submodule  graphics %{version}
%add_submodule  grDevices %{version}
%add_submodule  grid %{version}
%add_submodule  KernSmooth 2.23-26
%add_submodule  lattice 0.22-9
%add_submodule  MASS 7.3-65
%add_submodule  Matrix 1.7-5
Obsoletes:      R-Matrix < 0.999375-7
%add_submodule  methods %{version}
%add_submodule  mgcv 1.9-4
%add_submodule  nlme 3.1-169
%add_submodule  nnet 7.3-20
%add_submodule  parallel %{version}
%add_submodule  rpart 4.1.27
%add_submodule  spatial 7.3-18
%add_submodule  splines %{version}
%add_submodule  stats %{version}
%add_submodule  stats4 %{version}
%add_submodule  survival 3.8-6
%add_submodule  tcltk %{version}
%add_submodule  tools %{version}
%add_submodule  translations %{version}
%add_submodule  utils %{version}

%description core
A language and environment for statistical computing and graphics.
R is similar to the award-winning S system, which was developed at
Bell Laboratories by John Chambers et al. It provides a wide
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

%package core-devel
Summary:        Core files for development of R packages (no Java)
Requires:       R-core%{?_isa} = %{version}-%{release}
Requires:       libRmath-devel%{?_isa} = %{version}-%{release}
# R inherits the compiler flags it was built with, hence we need this on hardened systems
Requires:       redhat-rpm-config
# You need all the BuildRequires for the development version
Requires:       gcc-gfortran
Requires:       gcc-c++
Requires:       make
Requires:       pkgconfig
Requires:       pcre2-devel
Requires:       bzip2-devel
Requires:       xz-devel
Requires:       zlib-devel
Requires:       libdeflate-devel
Requires:       libzstd-devel
Requires:       tre-devel
Requires:       %{blaslib}-devel
Requires:       libX11-devel
Requires:       libicu-devel
Requires:       libtirpc-devel
Recommends:     texlive
Recommends:     texinfo-tex
Recommends:     tidy
Recommends:     devscripts-checkbashisms
%if 0%{?fedora} || 0%{?oreon}
# No inconsolata on RHEL tex
Recommends:     tex(inconsolata.sty)
# "‘qpdf’ is needed for checks on size reduction of PDFs"
# qpdf is not in epel, and since 99% of R doesn't use it, we'll let it slide.
Recommends:     qpdf
%endif

Provides:       R-Matrix-devel = 1.7.5
Obsoletes:      R-Matrix-devel < 0.999375-7

%ifarch %{java_arches}
%description core-devel
Install R-core-devel if you are going to develop or compile R packages.
This package does not configure the R environment for Java, install
R-java-devel if you want this.
%else
%description core-devel
Install R-core-devel if you are going to develop or compile R packages.
%endif

%package devel
Summary:        Full R development environment metapackage
Requires:       R-rpm-macros
Requires:       R-core-devel%{?_isa} = %{version}-%{release}
%ifarch %{java_arches}
Requires:       R-java-devel%{?_isa} = %{version}-%{release}
%else
Provides:       R-java-devel = %{version}-%{release}
Obsoletes:      R-java-devel < 4.1.3-3
%endif

%description devel
This is a metapackage to install a complete (with Java) R development
environment.

%ifarch %{java_arches}
%package java
Summary:        R with Java Runtime Environment from the distro
Requires(post): R-core%{?_isa} = %{version}-%{release}
Requires:       java-headless

%description java
A language and environment for statistical computing and graphics.
R is similar to the award-winning S system, which was developed at
Bell Laboratories by John Chambers et al. It provides a wide
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

This package also depends on java as packaged for this distribution.

%package java-devel
Summary:        Development package for use with Java enabled R components
Requires:       R-java%{?_isa} = %{version}-%{release}
Requires(post): R-core-devel%{?_isa} = %{version}-%{release}
Requires(post): java-devel

%description java-devel
Install R-java-devel if you are going to develop or compile R packages
that assume java is present and configured on the system.
%endif

%package -n libRmath
Summary:        Standalone math library from the R project

%description -n libRmath
A standalone library of mathematical and statistical functions derived
from the R project.  This package provides the shared libRmath library.

%package -n libRmath-devel
Summary:        Headers from the R Standalone math library
Requires:       libRmath%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libRmath-devel
A standalone library of mathematical and statistical functions derived
from the R project.  This package provides the libRmath header files.

%package -n libRmath-static
Summary:        Static R Standalone math library
Requires:       libRmath-devel%{?_isa} = %{version}-%{release}

%description -n libRmath-static
A standalone library of mathematical and statistical functions derived
from the R project.  This package provides the static libRmath library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1 -b .fixpath
# A bunch of macOS stuff in v4.5.2's archive
find . -name '._*' -delete

%build
# Comment out default R_LIBS_SITE (since R 4.2) and set our own as always
sed -i -e '/R_LIBS_SITE=/s/^/#/g' etc/Renviron.in
# Only packages which are needed as runtime dependencies are rebuilt for
# flatpaks in /app, build dependencies are from buildroot in /usr
echo 'R_LIBS_SITE=${R_LIBS_SITE-'"'/usr/local/lib/R/site-library:/usr/local/lib/R/library:%{_libdir}/R/library:%{_datadir}/R/library%{?flatpak::/usr/%{_lib}/R/library:/usr/share/R/library}'"'}' >> etc/Renviron.in
# Relax texi2any requirement for EPEL9
sed -i -e 's|texi2any_version_min} -lt 8|texi2any_version_min} -lt 7|' configure
# No inconsolata on RHEL tex
%if 0%{?rhel}
export R_RD4PDF="times,hyper"
sed -i 's|inconsolata,||g' etc/Renviron.in
%endif
export R_PDFVIEWER="%{_bindir}/xdg-open"
export R_BROWSER="%{_bindir}/xdg-open"

%ifarch %{java_arches}
export JAVA_HOME=%{_jvmdir}/jre
%endif

%configure \
  rdocdir=%{_pkgdocdir} \
  rincludedir=%{_includedir}/R \
  rsharedir=%{_datadir}/R \
  --with-system-tre \
  --with-blas=%{blaslib}%{blasvar} \
  --with-lapack \
  --with-tcl-config=/usr/%{_lib}/tclConfig.sh \
  --with-tk-config=/usr/%{_lib}/tkConfig.sh \
  --enable-R-shlib \
  --enable-prebuilt-html \
  --enable-R-profiling \
  --enable-memory-profiling \
  | tee CONFIGURE.log
cat CONFIGURE.log | grep -A30 'R is now' - > CAPABILITIES
make V=1
(cd src/nmath/standalone; make)
make pdf
make compact-pdf
make info

# Convert to UTF-8
for i in doc/manual/R-intro.info doc/manual/R-FAQ.info doc/FAQ doc/manual/R-admin.info doc/manual/R-exts.info-1; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,}
  mv $i{.utf8,}
done

%install
make DESTDIR=%{buildroot} install install-pdf install-info

rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_pkgdocdir}
install -p CAPABILITIES %{buildroot}%{_pkgdocdir}

# Install libRmath files
(cd src/nmath/standalone; make install DESTDIR=%{buildroot})

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/R/lib" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

mkdir -p %{buildroot}%{_datadir}/R/library

# Fix multilib
touch -r README %{buildroot}%{_pkgdocdir}/CAPABILITIES
touch -r README doc/manual/*.pdf
touch -r README %{buildroot}%{_bindir}/R

# Fix html/packages.html
# We can safely use RHOME here, because all of these are system packages.
sed -i 's|\..\/\..|%{_libdir}/R|g' %{buildroot}%{_pkgdocdir}/html/packages.html

for i in %{buildroot}%{_libdir}/R/library/*/html/*.html; do
  sed -i 's|\..\/\..\/..\/doc|%{_pkgdocdir}|g' $i
done

# Fix exec bits
chmod +x %{buildroot}%{_datadir}/R/sh/echo.sh
chmod +x %{buildroot}%{_libdir}/R/bin/*
chmod -x %{buildroot}%{_libdir}/R/library/mgcv/CITATION %{buildroot}%{_pkgdocdir}/CAPABILITIES

# Symbolic link for convenience
if [ ! -d "%{buildroot}%{_libdir}/R/include" ]; then
	pushd %{buildroot}%{_libdir}/R
	ln -s ../../include/R include
	popd
fi

# Symbolic link for LaTeX
%{!?_texdir:  %global _texdir  %{_datadir}/texlive}
%{!?_texdist: %global _texdist %{_texdir}/texmf-dist}
for i in tex/latex bibtex/bib bibtex/bst; do
  mkdir -p %{buildroot}%{_texdist}/$i
  (cd %{buildroot}%{_texdist}/$i && ln -s %{_datadir}/R/texmf/$i R)
done

%if 0%{?flatpak}
# keep compatibility with shebang dependencies
mkdir -p %{buildroot}/usr/bin
ln -s /app/bin/Rscript %{buildroot}/usr/bin/Rscript
%endif

%check
%if %{with tests}
# Needed by tests/ok-error.R, which will smash the stack on PPC64.
# This is the purpose of the test.
ulimit -s 16384
TZ="Europe/Paris" make check
%endif

%files
# Metapackage

%files core
%{_bindir}/R
%{_bindir}/Rscript
%{_datadir}/R/
# Links to LaTeX stuff
%dir %{_texdir}
%dir %{_texdist}
%dir %{_texdist}/tex/
%dir %{_texdist}/tex/latex/
%{_texdist}/tex/latex/R
%dir %{_texdist}/bibtex/
%dir %{_texdist}/bibtex/bib/
%{_texdist}/bibtex/bib/R
%dir %{_texdist}/bibtex/bst/
%{_texdist}/bibtex/bst/R
# Have to break this out for the translations
%dir %{_libdir}/R/
%{_libdir}/R/bin/
%dir %{_libdir}/R/etc
%config %{_libdir}/R/etc/Makeconf
%config %{_libdir}/R/etc/javaconf
%config(noreplace) %{_libdir}/R/etc/Renviron
%config(noreplace) %{_libdir}/R/etc/ldpaths
%config(noreplace) %{_libdir}/R/etc/repositories
%{_libdir}/R/lib/
%dir %{_libdir}/R/library/
%dir %{_libdir}/R/library/translations/
%{_libdir}/R/library/translations/DESCRIPTION
%lang(ar) %{_libdir}/R/library/translations/ar/
%lang(bn) %{_libdir}/R/library/translations/bn/
%lang(ca) %{_libdir}/R/library/translations/ca/
%lang(da) %{_libdir}/R/library/translations/da/
%lang(de) %{_libdir}/R/library/translations/de/
%lang(en) %{_libdir}/R/library/translations/en*/
%lang(es) %{_libdir}/R/library/translations/es/
%lang(fa) %{_libdir}/R/library/translations/fa/
%lang(fr) %{_libdir}/R/library/translations/fr/
%lang(hi) %{_libdir}/R/library/translations/hi/
%lang(hu) %{_libdir}/R/library/translations/hu/
%lang(id) %{_libdir}/R/library/translations/id/
%lang(it) %{_libdir}/R/library/translations/it/
%lang(ja) %{_libdir}/R/library/translations/ja/
%lang(ko) %{_libdir}/R/library/translations/ko/
%lang(lt) %{_libdir}/R/library/translations/lt/
%lang(ne) %{_libdir}/R/library/translations/ne/
%lang(nn) %{_libdir}/R/library/translations/nn/
%lang(pl) %{_libdir}/R/library/translations/pl/
%lang(pt) %{_libdir}/R/library/translations/pt*/
%lang(ru) %{_libdir}/R/library/translations/ru/
%lang(sq) %{_libdir}/R/library/translations/sq/
%lang(tr) %{_libdir}/R/library/translations/tr/
%lang(ur) %{_libdir}/R/library/translations/ur/
%lang(zh) %{_libdir}/R/library/translations/zh*/
# base
%dir %{_libdir}/R/library/base/
%{_libdir}/R/library/base/CITATION
%{_libdir}/R/library/base/demo/
%{_libdir}/R/library/base/DESCRIPTION
%{_libdir}/R/library/base/help/
%doc %{_libdir}/R/library/base/html/
%{_libdir}/R/library/base/INDEX
%{_libdir}/R/library/base/Meta/
%{_libdir}/R/library/base/R/
# boot
%dir %{_libdir}/R/library/boot/
%{_libdir}/R/library/boot/bd.q
%{_libdir}/R/library/boot/CITATION
%{_libdir}/R/library/boot/data/
%{_libdir}/R/library/boot/DESCRIPTION
%{_libdir}/R/library/boot/help/
%doc %{_libdir}/R/library/boot/html/
%{_libdir}/R/library/boot/INDEX
%{_libdir}/R/library/boot/Meta/
%{_libdir}/R/library/boot/NAMESPACE
%dir %{_libdir}/R/library/boot/po/
%lang(de) %{_libdir}/R/library/boot/po/de/
%lang(en) %{_libdir}/R/library/boot/po/en*/
%lang(fr) %{_libdir}/R/library/boot/po/fr/
%lang(it) %{_libdir}/R/library/boot/po/it/
%lang(ko) %{_libdir}/R/library/boot/po/ko/
%lang(pl) %{_libdir}/R/library/boot/po/pl/
%lang(ru) %{_libdir}/R/library/boot/po/ru/
%{_libdir}/R/library/boot/R/
# class
%dir %{_libdir}/R/library/class/
%{_libdir}/R/library/class/CITATION
%{_libdir}/R/library/class/DESCRIPTION
%{_libdir}/R/library/class/help/
%doc %{_libdir}/R/library/class/html/
%{_libdir}/R/library/class/INDEX
%{_libdir}/R/library/class/libs/
%{_libdir}/R/library/class/Meta/
%{_libdir}/R/library/class/NAMESPACE
%doc %{_libdir}/R/library/class/NEWS
%dir %{_libdir}/R/library/class/po/
%lang(de) %{_libdir}/R/library/class/po/de/
%lang(en) %{_libdir}/R/library/class/po/en*/
%lang(fr) %{_libdir}/R/library/class/po/fr/
%lang(it) %{_libdir}/R/library/class/po/it/
%lang(ko) %{_libdir}/R/library/class/po/ko/
%lang(pl) %{_libdir}/R/library/class/po/pl/
%{_libdir}/R/library/class/R/
# cluster
%dir %{_libdir}/R/library/cluster/
%{_libdir}/R/library/cluster/CITATION
%{_libdir}/R/library/cluster/data/
%{_libdir}/R/library/cluster/DESCRIPTION
%{_libdir}/R/library/cluster/help/
%doc %{_libdir}/R/library/cluster/html/
%{_libdir}/R/library/cluster/INDEX
%{_libdir}/R/library/cluster/libs/
%{_libdir}/R/library/cluster/Meta/
%{_libdir}/R/library/cluster/NAMESPACE
%doc %{_libdir}/R/library/cluster/NEWS.Rd
%dir %{_libdir}/R/library/cluster/po/
%lang(de) %{_libdir}/R/library/cluster/po/de/
%lang(en) %{_libdir}/R/library/cluster/po/en*/
%lang(fr) %{_libdir}/R/library/cluster/po/fr/
%lang(it) %{_libdir}/R/library/cluster/po/it/
%lang(ko) %{_libdir}/R/library/cluster/po/ko/
%lang(lt) %{_libdir}/R/library/cluster/po/lt/
%lang(pl) %{_libdir}/R/library/cluster/po/pl/
%{_libdir}/R/library/cluster/R/
%{_libdir}/R/library/cluster/test-tools.R
# codetools
%dir %{_libdir}/R/library/codetools/
%{_libdir}/R/library/codetools/DESCRIPTION
%{_libdir}/R/library/codetools/help/
%doc %{_libdir}/R/library/codetools/html/
%{_libdir}/R/library/codetools/INDEX
%{_libdir}/R/library/codetools/Meta/
%{_libdir}/R/library/codetools/NAMESPACE
%{_libdir}/R/library/codetools/R/
# compiler
%dir %{_libdir}/R/library/compiler/
%{_libdir}/R/library/compiler/DESCRIPTION
%{_libdir}/R/library/compiler/help/
%doc %{_libdir}/R/library/compiler/html/
%{_libdir}/R/library/compiler/INDEX
%{_libdir}/R/library/compiler/Meta/
%{_libdir}/R/library/compiler/NAMESPACE
%{_libdir}/R/library/compiler/R/
# datasets
%dir %{_libdir}/R/library/datasets/
%{_libdir}/R/library/datasets/data/
%{_libdir}/R/library/datasets/DESCRIPTION
%{_libdir}/R/library/datasets/help/
%doc %{_libdir}/R/library/datasets/html
%{_libdir}/R/library/datasets/INDEX
%{_libdir}/R/library/datasets/Meta/
%{_libdir}/R/library/datasets/NAMESPACE
# foreign
%dir %{_libdir}/R/library/foreign/
%license %{_libdir}/R/library/foreign/COPYRIGHTS
%{_libdir}/R/library/foreign/DESCRIPTION
%{_libdir}/R/library/foreign/files/
%{_libdir}/R/library/foreign/help/
%doc %{_libdir}/R/library/foreign/html/
%{_libdir}/R/library/foreign/INDEX
%{_libdir}/R/library/foreign/libs/
%{_libdir}/R/library/foreign/Meta/
%{_libdir}/R/library/foreign/NAMESPACE
%dir %{_libdir}/R/library/foreign/po/
%lang(de) %{_libdir}/R/library/foreign/po/de/
%lang(en) %{_libdir}/R/library/foreign/po/en*/
%lang(fr) %{_libdir}/R/library/foreign/po/fr/
%lang(it) %{_libdir}/R/library/foreign/po/it/
%lang(pl) %{_libdir}/R/library/foreign/po/pl/
%{_libdir}/R/library/foreign/R/
# graphics
%dir %{_libdir}/R/library/graphics/
%{_libdir}/R/library/graphics/demo/
%{_libdir}/R/library/graphics/DESCRIPTION
%{_libdir}/R/library/graphics/help/
%doc %{_libdir}/R/library/graphics/html/
%{_libdir}/R/library/graphics/INDEX
%{_libdir}/R/library/graphics/libs/
%{_libdir}/R/library/graphics/Meta/
%{_libdir}/R/library/graphics/NAMESPACE
%{_libdir}/R/library/graphics/R/
# grDevices
%dir %{_libdir}/R/library/grDevices/
%{_libdir}/R/library/grDevices/afm/
%{_libdir}/R/library/grDevices/demo/
%{_libdir}/R/library/grDevices/DESCRIPTION
%{_libdir}/R/library/grDevices/enc/
%{_libdir}/R/library/grDevices/fonts/
%{_libdir}/R/library/grDevices/help/
%doc %{_libdir}/R/library/grDevices/html/
%{_libdir}/R/library/grDevices/icc/
%{_libdir}/R/library/grDevices/INDEX
%{_libdir}/R/library/grDevices/libs/
%{_libdir}/R/library/grDevices/Meta/
%{_libdir}/R/library/grDevices/NAMESPACE
%{_libdir}/R/library/grDevices/R/
# grid
%dir %{_libdir}/R/library/grid/
%{_libdir}/R/library/grid/DESCRIPTION
%doc %{_libdir}/R/library/grid/doc/
%{_libdir}/R/library/grid/help/
%doc %{_libdir}/R/library/grid/html/
%{_libdir}/R/library/grid/INDEX
%{_libdir}/R/library/grid/libs/
%{_libdir}/R/library/grid/Meta/
%{_libdir}/R/library/grid/NAMESPACE
%{_libdir}/R/library/grid/R/
# KernSmooth
%dir %{_libdir}/R/library/KernSmooth/
%{_libdir}/R/library/KernSmooth/DESCRIPTION
%{_libdir}/R/library/KernSmooth/help/
%doc %{_libdir}/R/library/KernSmooth/html/
%{_libdir}/R/library/KernSmooth/INDEX
%{_libdir}/R/library/KernSmooth/libs/
%{_libdir}/R/library/KernSmooth/Meta/
%{_libdir}/R/library/KernSmooth/NAMESPACE
%dir %{_libdir}/R/library/KernSmooth/po/
%lang(de) %{_libdir}/R/library/KernSmooth/po/de/
%lang(en) %{_libdir}/R/library/KernSmooth/po/en*/
%lang(fr) %{_libdir}/R/library/KernSmooth/po/fr/
%lang(it) %{_libdir}/R/library/KernSmooth/po/it/
%lang(ko) %{_libdir}/R/library/KernSmooth/po/ko/
%lang(pl) %{_libdir}/R/library/KernSmooth/po/pl/
%{_libdir}/R/library/KernSmooth/R/
# lattice
%dir %{_libdir}/R/library/lattice/
%{_libdir}/R/library/lattice/CITATION
%{_libdir}/R/library/lattice/data/
%{_libdir}/R/library/lattice/demo/
%{_libdir}/R/library/lattice/DESCRIPTION
%doc %{_libdir}/R/library/lattice/doc/
%{_libdir}/R/library/lattice/help/
%doc %{_libdir}/R/library/lattice/html/
%{_libdir}/R/library/lattice/INDEX
%{_libdir}/R/library/lattice/libs/
%{_libdir}/R/library/lattice/Meta/
%{_libdir}/R/library/lattice/NAMESPACE
%doc %{_libdir}/R/library/lattice/NEWS.md
%dir %{_libdir}/R/library/lattice/po/
%lang(de) %{_libdir}/R/library/lattice/po/de/
%lang(en) %{_libdir}/R/library/lattice/po/en*/
%lang(fr) %{_libdir}/R/library/lattice/po/fr/
%lang(it) %{_libdir}/R/library/lattice/po/it/
%lang(ko) %{_libdir}/R/library/lattice/po/ko/
%lang(pl) %{_libdir}/R/library/lattice/po/pl*/
%{_libdir}/R/library/lattice/R/
%doc %{_libdir}/R/library/lattice/README.md
# MASS
%dir %{_libdir}/R/library/MASS/
%{_libdir}/R/library/MASS/CITATION
%{_libdir}/R/library/MASS/data/
%{_libdir}/R/library/MASS/DESCRIPTION
%{_libdir}/R/library/MASS/help/
%doc %{_libdir}/R/library/MASS/html/
%{_libdir}/R/library/MASS/INDEX
%{_libdir}/R/library/MASS/libs/
%{_libdir}/R/library/MASS/Meta/
%{_libdir}/R/library/MASS/NAMESPACE
%doc %{_libdir}/R/library/MASS/NEWS
%dir %{_libdir}/R/library/MASS/po
%lang(de) %{_libdir}/R/library/MASS/po/de/
%lang(en) %{_libdir}/R/library/MASS/po/en*/
%lang(fr) %{_libdir}/R/library/MASS/po/fr/
%lang(it) %{_libdir}/R/library/MASS/po/it/
%lang(ko) %{_libdir}/R/library/MASS/po/ko/
%lang(pl) %{_libdir}/R/library/MASS/po/pl/
%{_libdir}/R/library/MASS/R/
%{_libdir}/R/library/MASS/scripts/
# Matrix
%dir %{_libdir}/R/library/Matrix/
%{_libdir}/R/library/Matrix/data/
%{_libdir}/R/library/Matrix/DESCRIPTION
%doc %{_libdir}/R/library/Matrix/doc/
%{_libdir}/R/library/Matrix/external/
%{_libdir}/R/library/Matrix/help/
%doc %{_libdir}/R/library/Matrix/html/
%{_libdir}/R/library/Matrix/include/
%{_libdir}/R/library/Matrix/INDEX
%{_libdir}/R/library/Matrix/libs/
%license %{_libdir}/R/library/Matrix/LICENCE
%{_libdir}/R/library/Matrix/Meta/
%{_libdir}/R/library/Matrix/NAMESPACE
%doc %{_libdir}/R/library/Matrix/NEWS.Rd
%dir %{_libdir}/R/library/Matrix/po/
%lang(de) %{_libdir}/R/library/Matrix/po/de/
%lang(en) %{_libdir}/R/library/Matrix/po/en*/
%lang(fr) %{_libdir}/R/library/Matrix/po/fr/
%lang(it) %{_libdir}/R/library/Matrix/po/it/
%lang(ko) %{_libdir}/R/library/Matrix/po/ko/
%lang(lt) %{_libdir}/R/library/Matrix/po/lt/
%lang(pl) %{_libdir}/R/library/Matrix/po/pl/
%{_libdir}/R/library/Matrix/R/
%{_libdir}/R/library/Matrix/scripts/
%{_libdir}/R/library/Matrix/test-tools.R
%{_libdir}/R/library/Matrix/test-tools-1.R
%{_libdir}/R/library/Matrix/test-tools-Matrix.R
# methods
%dir %{_libdir}/R/library/methods/
%{_libdir}/R/library/methods/DESCRIPTION
%{_libdir}/R/library/methods/help/
%doc %{_libdir}/R/library/methods/html/
%{_libdir}/R/library/methods/INDEX
%{_libdir}/R/library/methods/libs/
%{_libdir}/R/library/methods/Meta/
%{_libdir}/R/library/methods/NAMESPACE
%{_libdir}/R/library/methods/R/
# mgcv
%dir %{_libdir}/R/library/mgcv/
%{_libdir}/R/library/mgcv/CITATION
%{_libdir}/R/library/mgcv/data/
%{_libdir}/R/library/mgcv/DESCRIPTION
%{_libdir}/R/library/mgcv/help/
%doc %{_libdir}/R/library/mgcv/html/
%{_libdir}/R/library/mgcv/INDEX
%{_libdir}/R/library/mgcv/libs/
%{_libdir}/R/library/mgcv/Meta/
%{_libdir}/R/library/mgcv/NAMESPACE
%dir %{_libdir}/R/library/mgcv/po/
%lang(de) %{_libdir}/R/library/mgcv/po/de/
%lang(en) %{_libdir}/R/library/mgcv/po/en*/
%lang(fr) %{_libdir}/R/library/mgcv/po/fr/
%lang(ko) %{_libdir}/R/library/mgcv/po/ko/
%lang(pl) %{_libdir}/R/library/mgcv/po/pl/
%{_libdir}/R/library/mgcv/R/
# nlme
%dir %{_libdir}/R/library/nlme/
%{_libdir}/R/library/nlme/CITATION
%{_libdir}/R/library/nlme/data/
%{_libdir}/R/library/nlme/DESCRIPTION
%{_libdir}/R/library/nlme/help/
%doc %{_libdir}/R/library/nlme/html/
%{_libdir}/R/library/nlme/INDEX
%{_libdir}/R/library/nlme/libs/
%{_libdir}/R/library/nlme/Meta/
%{_libdir}/R/library/nlme/mlbook/
%{_libdir}/R/library/nlme/NAMESPACE
%dir %{_libdir}/R/library/nlme/po/
%lang(de) %{_libdir}/R/library/nlme/po/de/
%lang(en) %{_libdir}/R/library/nlme/po/en*/
%lang(fr) %{_libdir}/R/library/nlme/po/fr/
%lang(ko) %{_libdir}/R/library/nlme/po/ko/
%lang(pl) %{_libdir}/R/library/nlme/po/pl/
%{_libdir}/R/library/nlme/R/
%{_libdir}/R/library/nlme/scripts/
# nnet
%dir %{_libdir}/R/library/nnet/
%{_libdir}/R/library/nnet/CITATION
%{_libdir}/R/library/nnet/DESCRIPTION
%{_libdir}/R/library/nnet/help/
%doc %{_libdir}/R/library/nnet/html/
%{_libdir}/R/library/nnet/INDEX
%{_libdir}/R/library/nnet/libs/
%{_libdir}/R/library/nnet/Meta/
%{_libdir}/R/library/nnet/NAMESPACE
%doc %{_libdir}/R/library/nnet/NEWS
%dir %{_libdir}/R/library/nnet/po
%lang(de) %{_libdir}/R/library/nnet/po/de/
%lang(en) %{_libdir}/R/library/nnet/po/en*/
%lang(fr) %{_libdir}/R/library/nnet/po/fr/
%lang(it) %{_libdir}/R/library/nnet/po/it/
%lang(ko) %{_libdir}/R/library/nnet/po/ko/
%lang(pl) %{_libdir}/R/library/nnet/po/pl/
%{_libdir}/R/library/nnet/R/
# parallel
%dir %{_libdir}/R/library/parallel/
%{_libdir}/R/library/parallel/DESCRIPTION
%doc %{_libdir}/R/library/parallel/doc/
%{_libdir}/R/library/parallel/help/
%doc %{_libdir}/R/library/parallel/html/
%{_libdir}/R/library/parallel/INDEX
%{_libdir}/R/library/parallel/libs/
%{_libdir}/R/library/parallel/Meta/
%{_libdir}/R/library/parallel/NAMESPACE
%{_libdir}/R/library/parallel/R/
# rpart
%dir %{_libdir}/R/library/rpart/
%{_libdir}/R/library/rpart/data/
%{_libdir}/R/library/rpart/DESCRIPTION
%doc %{_libdir}/R/library/rpart/doc/
%{_libdir}/R/library/rpart/help/
%doc %{_libdir}/R/library/rpart/html/
%{_libdir}/R/library/rpart/INDEX
%{_libdir}/R/library/rpart/libs/
%{_libdir}/R/library/rpart/Meta/
%{_libdir}/R/library/rpart/NAMESPACE
%doc %{_libdir}/R/library/rpart/NEWS.Rd
%dir %{_libdir}/R/library/rpart/po
%lang(de) %{_libdir}/R/library/rpart/po/de/
%lang(en) %{_libdir}/R/library/rpart/po/en*/
%lang(fr) %{_libdir}/R/library/rpart/po/fr/
%lang(ko) %{_libdir}/R/library/rpart/po/ko/
%lang(pl) %{_libdir}/R/library/rpart/po/pl/
%lang(ru) %{_libdir}/R/library/rpart/po/ru/
%{_libdir}/R/library/rpart/R/
%doc %{_libdir}/R/library/rpart/README.md
# spatial
%dir %{_libdir}/R/library/spatial/
%{_libdir}/R/library/spatial/CITATION
%{_libdir}/R/library/spatial/DESCRIPTION
%{_libdir}/R/library/spatial/help/
%doc %{_libdir}/R/library/spatial/html/
%{_libdir}/R/library/spatial/INDEX
%{_libdir}/R/library/spatial/libs/
%{_libdir}/R/library/spatial/Meta/
%{_libdir}/R/library/spatial/NAMESPACE
%doc %{_libdir}/R/library/spatial/NEWS
%dir %{_libdir}/R/library/spatial/po
%lang(de) %{_libdir}/R/library/spatial/po/de/
%lang(en) %{_libdir}/R/library/spatial/po/en*/
%lang(fr) %{_libdir}/R/library/spatial/po/fr/
%lang(it) %{_libdir}/R/library/spatial/po/it/
%lang(ko) %{_libdir}/R/library/spatial/po/ko/
%lang(pl) %{_libdir}/R/library/spatial/po/pl/
%{_libdir}/R/library/spatial/ppdata/
%{_libdir}/R/library/spatial/PP.files
%{_libdir}/R/library/spatial/R/
# splines
%dir %{_libdir}/R/library/splines/
%{_libdir}/R/library/splines/DESCRIPTION
%{_libdir}/R/library/splines/help/
%doc %{_libdir}/R/library/splines/html/
%{_libdir}/R/library/splines/INDEX
%{_libdir}/R/library/splines/libs/
%{_libdir}/R/library/splines/Meta/
%{_libdir}/R/library/splines/NAMESPACE
%{_libdir}/R/library/splines/R/
# stats
%dir %{_libdir}/R/library/stats/
%license %{_libdir}/R/library/stats/COPYRIGHTS.modreg
%{_libdir}/R/library/stats/demo/
%{_libdir}/R/library/stats/DESCRIPTION
%doc %{_libdir}/R/library/stats/doc/
%{_libdir}/R/library/stats/help/
%doc %{_libdir}/R/library/stats/html/
%{_libdir}/R/library/stats/INDEX
%{_libdir}/R/library/stats/libs/
%{_libdir}/R/library/stats/Meta/
%{_libdir}/R/library/stats/NAMESPACE
%{_libdir}/R/library/stats/R/
%{_libdir}/R/library/stats/SOURCES.ts
# stats4
%dir %{_libdir}/R/library/stats4/
%{_libdir}/R/library/stats4/DESCRIPTION
%{_libdir}/R/library/stats4/help/
%doc %{_libdir}/R/library/stats4/html/
%{_libdir}/R/library/stats4/INDEX
%{_libdir}/R/library/stats4/Meta/
%{_libdir}/R/library/stats4/NAMESPACE
%{_libdir}/R/library/stats4/R/
# survival
%dir %{_libdir}/R/library/survival/
%{_libdir}/R/library/survival/CITATION
%license %{_libdir}/R/library/survival/COPYRIGHTS
%{_libdir}/R/library/survival/data/
%{_libdir}/R/library/survival/DESCRIPTION
%doc %{_libdir}/R/library/survival/doc/
%{_libdir}/R/library/survival/help
%doc %{_libdir}/R/library/survival/html/
%{_libdir}/R/library/survival/INDEX
%{_libdir}/R/library/survival/libs/
%{_libdir}/R/library/survival/Meta/
%{_libdir}/R/library/survival/NAMESPACE
%doc %{_libdir}/R/library/survival/NEWS.Rd*
%{_libdir}/R/library/survival/R/
# tcltk
%dir %{_libdir}/R/library/tcltk/
%{_libdir}/R/library/tcltk/demo/
%{_libdir}/R/library/tcltk/DESCRIPTION
%{_libdir}/R/library/tcltk/exec/
%{_libdir}/R/library/tcltk/help/
%doc %{_libdir}/R/library/tcltk/html/
%{_libdir}/R/library/tcltk/INDEX
%{_libdir}/R/library/tcltk/libs/
%{_libdir}/R/library/tcltk/Meta/
%{_libdir}/R/library/tcltk/NAMESPACE
%{_libdir}/R/library/tcltk/R/
# tools
%dir %{_libdir}/R/library/tools/
%{_libdir}/R/library/tools/DESCRIPTION
%{_libdir}/R/library/tools/help/
%doc %{_libdir}/R/library/tools/html/
%{_libdir}/R/library/tools/INDEX
%{_libdir}/R/library/tools/libs/
%{_libdir}/R/library/tools/Meta/
%{_libdir}/R/library/tools/misc/
%{_libdir}/R/library/tools/NAMESPACE
%{_libdir}/R/library/tools/R/
# utils
%dir %{_libdir}/R/library/utils/
%{_libdir}/R/library/utils/DESCRIPTION
%doc %{_libdir}/R/library/utils/doc/
%{_libdir}/R/library/utils/help/
%doc %{_libdir}/R/library/utils/html/
%{_libdir}/R/library/utils/iconvlist
%{_libdir}/R/library/utils/INDEX
%{_libdir}/R/library/utils/libs/
%{_libdir}/R/library/utils/Meta/
%{_libdir}/R/library/utils/misc/
%{_libdir}/R/library/utils/NAMESPACE
%{_libdir}/R/library/utils/R/
%{_libdir}/R/library/utils/Sweave/
# end of packages
%{_libdir}/R/modules
%license %{_libdir}/R/COPYING
# %%doc %%{_libdir}/R/NEWS*
%{_libdir}/R/SVN-REVISION
%{_infodir}/R-*.info*
%{_mandir}/man1/*
%{_pkgdocdir}
%docdir %{_pkgdocdir}
%{_sysconfdir}/ld.so.conf.d/*
%if 0%{?flatpak}
/usr/bin/Rscript
%endif

%files core-devel
%{_libdir}/pkgconfig/libR.pc
%{_includedir}/R
# Symlink to %%{_includedir}/R/
%{_libdir}/R/include

%files devel
# Nothing, all files provided by R-core-devel

%ifarch %{java_arches}
%files java
# Nothing, all files provided by R-core

%files java-devel
# Nothing, all files provided by R-core-devel
%endif

%files -n libRmath
%license doc/COPYING
%{_libdir}/libRmath.so

%files -n libRmath-devel
%{_includedir}/Rmath.h
%{_libdir}/pkgconfig/libRmath.pc

%files -n libRmath-static
%{_libdir}/libRmath.a

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.6.0-1
- Import R for Oreon 11 RP1

