%global source0_hash 0686af6afec4c745d2f4193330ba3cfbcf5e36db6635df1cb1fd013c756cb307
%global singulardir	%{_libdir}/Singular
%global upstreamver	4-4-1
%global downstreamver	%{gsub %upstreamver - .}
%global patchver	p5
%global giturl		https://github.com/Singular/Singular
%bcond python 0
%if %{with python}
%global _python_bytecompile_extra 0
%endif
%bcond bootstrap 0
%ifarch %{arm64} %{x86_64} %{power64}
%bcond docs 1
%else
%bcond docs 0
%endif
Name:		Singular
Version:	%{downstreamver}%{?patchver}
Release:        1%{?dist}
Summary:        Computer Algebra System for polynomial computations
License:	(GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause AND HPND
URL:		https://www.singular.uni-kl.de/
VCS:		git:%{giturl}.git
Source0:        %{giturl}/archive/Release-%{upstreamver}%{patchver}.tar.gz
%if %{with python}
%endif
%if %{with python}
%endif
%if %{without bootstrap}
%endif
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	environment(modules)
Requires:	less
Requires:	qepcad-B
Requires:	TOPCOM%{_isa}
ExcludeArch:	%{ix86}
Patch:		%{name}-arches.patch
Patch:		%{name}-link.patch
Patch:		%{name}-desktop.patch
Patch:		%{name}-format.patch
Patch:		%{name}-parens.patch
Patch:		%{name}-gfanlib.patch
Patch:		%{name}-emacs.patch
Patch:		%{name}-use-after-free.patch
Patch:		%{name}-endian.patch
Patch:		%{name}-doc-hang.patch
Patch:		%{name}-polymake-lib.patch
# oreon:deps
BuildRequires:  4ti2
BuildRequires:  TOPCOM
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  ccluster-devel
BuildRequires:  cddlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  emacs
BuildRequires:  environment(modules)
BuildRequires:  flex
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gfan
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libgfan-devel
BuildRequires:  libspasm-devel
BuildRequires:  libtool
BuildRequires:  lrcalc
BuildRequires:  make
BuildRequires:  normaliz
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mathicgb)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ntl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qepcad-B
BuildRequires:  tex(latex)
BuildRequires:  texinfo-tex
# /oreon:deps
%description
Singular is a computer algebra system for polynomial computations, with
special emphasis on commutative and non-commutative algebra, algebraic
geometry, and singularity theory.

%package	libs
Summary:	Singular library
Requires:	%{name}-libpolys%{?_isa} = %{version}-%{release}
%description	libs
This package contains the main Singular library.

%package	devel
Summary:	Singular development files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-libpolys-devel%{?_isa} = %{version}-%{release}
%description	devel
This package contains the Singular development files.

%package	doc
Summary:	Singular documentation files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	doc
This package contains the Singular documentation files.

%package	emacs
Summary:	Emacs interface to Singular
Requires:	emacs-common
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	emacs
Emacs interface to Singular.

%package	-n factory
Summary:	C++ class library for multivariate polynomial data
Requires:	factory-gftables = %{version}-%{release}
%description	-n factory
Factory is a C++ class library that implements a recursive representation of
multivariate polynomial data.  It handles sparse multivariate polynomials over
different coefficient domains, such as Z, Q and GF(q), as well as algebraic
extensions over Q and GF(q) in an efficient way.  Factory includes algorithms
for computing univariate and multivariate gcds, resultants, chinese
remainders, and algorithms to factorize multivariate polynomials and to
compute the absolute factorization of multivariate polynomials with integer
coefficients.

%package	-n factory-devel
Summary:	Development files for the Singular factory
Requires:	factory%{?_isa} = %{version}-%{release}
Requires:	gmp-devel%{?_isa}
%description	-n factory-devel
Development files for the Singular factory.

%package	-n factory-gftables
Summary:	Singular factory addition tables
BuildArch:	noarch
%description	-n factory-gftables
Factory uses addition tables to calculate in GF(p^n) in an efficient way.

%package	libpolys
Summary:	C++ class library for polynomials in Singular
Requires:	factory%{?_isa} = %{version}-%{release}
%description	libpolys
Libpolys contains the data structures and basic algorithms for polynomials in
Singular.

%package	libpolys-devel
Summary:	Development files for libpolys
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	factory-devel%{?_isa} = %{version}-%{release}
Requires:	flint-devel%{?_isa}
%description	libpolys-devel
Development files for libpolys.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-Release-%{upstreamver}%{?patchver}

%if %{with python}
# Fix the name of the boost_python library
sed -ri 's/(lboost_python)-\$\{PYTHON_VERSION\}/\1%{python2_version_nodots}/' \
    Singular/dyn_modules/python/Makefile.am
%endif

# Do not force the use of c++11, since the polymake code requires c++14
sed -i 's/"-std=c++11"/""/' m4/ntl-check.m4

# Do not add an rpath for ccluster
sed -i 's@ -Wl,-rpath,\${CCLUSTER_HOME}/lib@@' m4/ccluster-check.m4

# Make sure we do not use the bundled gfanlib
rm -fr gfanlib

# Regenerate configure due to patches
autoreconf -fi

# The file countedref.cc needs to be built without strict aliasing
sed -i '/countedref\.cc/s/\$(CXXFLAGS)/& -fno-strict-aliasing/g' Singular/Makefile.in

%build

export CPPFLAGS='-I%{_includedir}/flint -I%{_includedir}/gfanlib'
%if %{with python}
pyincdir=$(python2 -Esc "import sysconfig; print(sysconfig.get_paths()['include'])")
CPPFLAGS="$CPPFLAGS -I$pyincdir"
%endif
export CFLAGS='%{build_cflags} -fPIC'
export CXXFLAGS='%{build_cxxflags} -fPIC'
export LDFLAGS='%{build_ldflags} -Wl,-z,lazy'
module load 4ti2-%{_arch}
module load lrcalc-%{_arch}
%configure \
	--bindir=%{singulardir} \
	--disable-silent-rules \
	--disable-optimizationflags \
	--disable-static \
	--enable-p-procs-dynamic \
	--enable-bigintm-module \
	--enable-gfanlib \
	--enable-gfanlib-module \
	--enable-Order-module \
	--enable-polymake-module \
%if %{with python}
	--enable-python-module \
%else
	--disable-python-module \
%endif
	--enable-sispasm-module \
	--enable-streamio \
	--with-gmp \
	--with-ntl \
	--with-flint \
	--with-mathicgb \
%if %{with python}
	--with-python=%{__python2} \
%else
	--without-python \
%endif
	--with-readline \
%if %{with docs}
	--enable-doc-build \
%endif
	--with-malloc=system
%make_build
%make_build -C dox html
%install
%make_install
mv %{buildroot}%{_libexecdir}/singular/MOD/* %{buildroot}%{_libdir}/singular/MOD
rm -fr %{buildroot}%{_libexecdir}
desktop-file-validate %{buildroot}%{_datadir}/applications/Singular.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/Singular-manual.desktop
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lntl -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/factory.pc
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/libpolys.pc
rm -f %{buildroot}%{_datadir}/singular/emacs/{ChangeLog,COPYING,NEWS}
rm -fr %{buildroot}%{_docdir}/singular
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{singulardir}/*-config %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
for cmd in ESingular Singular TSingular; do
  cp -p Singular/$cmd.man %{buildroot}%{_mandir}/man1/$cmd.1
done
%if %{with docs}
cp -a doc/{html,singular.idx} %{buildroot}%{_datadir}/singular
mkdir -p %{buildroot}%{_infodir}
cp -p doc/singular.info %{buildroot}%{_infodir}
%endif
rm -f %{buildroot}%{singulardir}/singularsurf
cat > %{buildroot}%{_bindir}/Singular << EOF
. /etc/profile.d/modules.sh
export SINGULAR_DATA_DIR=%{_datadir}
exec %{singulardir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/Singular
cat > %{buildroot}%{_bindir}/TSingular << EOF
. /etc/profile.d/modules.sh
exec %{singulardir}/TSingular --singular %{_bindir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/TSingular
cat > %{buildroot}%{_bindir}/ESingular << EOF
. /etc/profile.d/modules.sh
export ESINGULAR_EMACS_DIR=%{_datadir}/singular/emacs
exec %{singulardir}/ESingular --singular %{_bindir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/ESingular
%if %{with python}
%py_byte_compile %{__python2} %{buildroot}%{_datadir}/singular/LIB
%oreon_autofiles Singular-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Singular-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Singular-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Singular-emacs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles factory usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles factory-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles factory-gftables usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Singular-libpolys usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Singular-libpolys-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check
%files -f %{oreon_filedir}/main.list
%files -n Singular-libs -f %{oreon_filedir}/Singular-libs.list
%files -n Singular-devel -f %{oreon_filedir}/Singular-devel.list
%files -n Singular-doc -f %{oreon_filedir}/Singular-doc.list
%files -n Singular-emacs -f %{oreon_filedir}/Singular-emacs.list
%files -n factory -f %{oreon_filedir}/factory.list
%files -n factory-devel -f %{oreon_filedir}/factory-devel.list
%files -n factory-gftables -f %{oreon_filedir}/factory-gftables.list
%files -n Singular-libpolys -f %{oreon_filedir}/Singular-libpolys.list
%files -n Singular-libpolys-devel -f %{oreon_filedir}/Singular-libpolys-devel.list

%changelog

%autochangelog
