%global source0_hash 4da6e61d2c0aac5f14a2e7e432cb5fcc269efe83da4293050ba7f03dff4e2cf4
%global __brp_mangle_shebangs_exclude_from %{_libdir}/R/bin/
%undefine _package_note_flags
%bcond_without tests
%global __provides_exclude tex\\\(.*\\\)
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif
%bcond_with bootstrap
%global bootstrap_abi 4.5
%global major_version 4
%global minor_version 6
%global patch_version 1
Name:           R
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        1%{?dist}
Summary:        A language for data analysis and graphics
License:        GPL-2.0-or-later
URL:            https://www.r-project.org
Source0:        https://cran.r-project.org/src/base/R-4/R-%{version}.tar.gz
Patch0:         R-3.3.0-fix-java_path-in-javareconf.patch
%ifarch %{valgrind_arches}
%endif
%ifarch %{java_arches}
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
%endif
Requires:       R-devel%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  cairo-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  java-devel
BuildRequires:  less
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  pcre2-devel
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  tex(inconsolata.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  texinfo-tex
BuildRequires:  texlive
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-times
BuildRequires:  tk-devel
BuildRequires:  tre-devel
BuildRequires:  valgrind-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
Provides:       R(ABI) = %{major_version}.%{minor_version}
%if %{with bootstrap}
Provides:       R(ABI) = %{bootstrap_abi}
%endif
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
Requires:       redhat-rpm-config
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
%if 0%{?fedora} || (0%{?oreon} >= 11)
Recommends:     tex(inconsolata.sty)
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .fixpath
# A bunch of macOS stuff in v4.5.2's archive
find . -name '._*' -delete

%build

sed -i -e '/R_LIBS_SITE=/s/^/#/g' etc/Renviron.in
echo 'R_LIBS_SITE=${R_LIBS_SITE-'"'/usr/local/lib/R/site-library:/usr/local/lib/R/library:%{_libdir}/R/library:%{_datadir}/R/library%{?flatpak::/usr/%{_lib}/R/library:/usr/share/R/library}'"'}' >> etc/Renviron.in
sed -i -e 's|texi2any_version_min} -lt 8|texi2any_version_min} -lt 7|' configure
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
for i in doc/manual/R-intro.info doc/manual/R-FAQ.info doc/FAQ doc/manual/R-admin.info doc/manual/R-exts.info-1; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,}
  mv $i{.utf8,}
done
%install
make DESTDIR=%{buildroot} install install-pdf install-info
rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_pkgdocdir}
install -p CAPABILITIES %{buildroot}%{_pkgdocdir}
(cd src/nmath/standalone; make install DESTDIR=%{buildroot})
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/R/lib" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
mkdir -p %{buildroot}%{_datadir}/R/library
touch -r README %{buildroot}%{_pkgdocdir}/CAPABILITIES
touch -r README doc/manual/*.pdf
touch -r README %{buildroot}%{_bindir}/R
sed -i 's|\..\/\..|%{_libdir}/R|g' %{buildroot}%{_pkgdocdir}/html/packages.html
for i in %{buildroot}%{_libdir}/R/library/*/html/*.html; do
  sed -i 's|\..\/\..\/..\/doc|%{_pkgdocdir}|g' $i
done
chmod +x %{buildroot}%{_datadir}/R/sh/echo.sh
chmod +x %{buildroot}%{_libdir}/R/bin/*
chmod -x %{buildroot}%{_libdir}/R/library/mgcv/CITATION %{buildroot}%{_pkgdocdir}/CAPABILITIES
if [ ! -d "%{buildroot}%{_libdir}/R/include" ]; then
	pushd %{buildroot}%{_libdir}/R
	ln -s ../../include/R include
	popd
fi
%{!?_texdir:  %global _texdir  %{_datadir}/texlive}
%{!?_texdist: %global _texdist %{_texdir}/texmf-dist}
for i in tex/latex bibtex/bib bibtex/bst; do
  mkdir -p %{buildroot}%{_texdist}/$i
  (cd %{buildroot}%{_texdist}/$i && ln -s %{_datadir}/R/texmf/$i R)
done
%if 0%{?flatpak}
mkdir -p %{buildroot}/usr/bin
ln -s /app/bin/Rscript %{buildroot}/usr/bin/Rscript
%oreon_autofiles R-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles R-core-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles R-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles R-java usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles R-java-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libRmath usr/*/lib*.so.*
%oreon_autofiles libRmath-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libRmath-static usr/*/lib*.so.*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%endif
%check

%if %{with tests}
ulimit -s 16384
TZ="Europe/Paris" make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n R-core -f %{oreon_filedir}/R-core.list
%files -n R-core-devel -f %{oreon_filedir}/R-core-devel.list
%files -n R-devel -f %{oreon_filedir}/R-devel.list
%files -n R-java -f %{oreon_filedir}/R-java.list
%files -n R-java-devel -f %{oreon_filedir}/R-java-devel.list
%files -n libRmath -f %{oreon_filedir}/libRmath.list
%files -n libRmath-devel -f %{oreon_filedir}/libRmath-devel.list
%files -n libRmath-static -f %{oreon_filedir}/libRmath-static.list

%changelog

%autochangelog
