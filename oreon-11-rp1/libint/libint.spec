%global source0_hash 798015e81d4bc8235f3001b84bab06fdf0ad0f7fd1d2d6513ef109d9e6726727

# Please void making new releases of the package, because all depending
# packages will be needing rebuilds.

# RPM macro directory
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Commit hash
%global commit 29a6a6df4cd1242c54b5651fc0ac6dd563edf7c0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Version of flags used in configure. Increment always when changing the flags, since it will break the API and ABI.
%global apiversion 0

# LTO fails on Fedora 36 i686 (out of memory)
%if 0%{?fedora} == 36
%ifarch %{ix86}
%global _lto_cflags %nil
%endif
%endif

Name:           libint
Version:        1.2.1
Release:        26%{?dist}
Summary:        A library for computing electron repulsion integrals efficiently
# Libint is two things: a code generator, and a generated
# library. This package builds and runs the compiler (GPLv3), and
# builds and ships the generated library (LGPLv3). The license tag
# refers to the binaries, i.e. here the generated library.
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://sourceforge.net/p/libint
Source0:        https://github.com/evaleev/libint/archive/%{commit}/libint-%{commit}.tar.gz

# Increase maxnode
Patch1:         libint-1.2.1-maxnode.patch
# Use old-style soname
Patch2:         libint-1.2.1-soname.patch
# Compiler compatibility fixes
Patch3:         https://github.com/evaleev/libint/pull/353.patch

# Capabilities provided by library
Provides:       libint(api)%{?_isa} = %{apiversion}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%if 0%{?rhel} == 6
# Required to build documentation
BuildRequires:  /usr/bin/bibtex
BuildRequires:  /usr/bin/pdflatex
%endif

%if 0%{?fedora} > 17 || 0%{?rhel} > 6
# Required to build documentation
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  texlive-bibtex
%endif

%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package devel
Summary:  Development headers and libraries for libint
Requires: libint%{?_isa} = %{version}-%{release}
Requires: libderiv%{?_isa} = %{version}-%{release}
Requires: libr12%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers and libraries for libint.
It also contains a programmer's manual.

%package -n libr12
Summary:  A library for computing integrals that arise in Kutzelnigg’s linear R12 theories

%description -n libr12
libr12 computes types integrals that appear in Kutzelnigg’s linear R12 theories
for electronic structure. All linear R12 methods, such as MP2-R12, contain
terms in the wave function that are linear in the inter-electronic distances
r_{ij} (hence the name). Appearance of several types of two-body integrals is
due to the use of the approximate resolution of the identity to reduce three-
and four-body integrals to products of simpler integrals.

%package -n libderiv
Summary:  A library for computing derivatives of electron repulsion integrals
Requires: libint%{?_isa} = %{version}-%{release}

%description -n libderiv
libderiv computes first and second derivatives of ERIs with respect to the
coordinates of the basis function origin. This type of integrals are also very
common in electronic structure theory, where they appear in analytic gradient
expressions. The derivatives are typically used in the calculation of forces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P1 -p1 -b .maxnode
%patch -P2 -p1 -b .soname
%patch -P3 -p1 -b .gcc15
libtoolize --copy --force
aclocal -I lib/autoconf
autoconf

%build
# Disable stack size limit due to static allocation of arrays
ulimit -s unlimited
%configure --enable-shared --disable-static \
 --with-libint-max-am=10 --with-libint-opt-am=6 \
 --with-libderiv-max-am1=6 --with-libderiv-max-am2=5 \
 --with-libr12-max-am=5 --with-libr12-opt-am=4

# The generated library is already highly optimized for performance,
# so it's safe to use a lower level of compiler optimization here.
oflags=`echo %{optflags} | sed -E 's/(^| )-O(0|1|2|3|s|fast)( |$)/\1-O1\3/g'`
make V=0 CFLAGS="${oflags}" CXXFLAGS="${oflags}" %{?_smp_mflags} > build.log 2>&1 || {
  status=$?
  cat build.log
  exit $status
}

# Build documentation
cd doc/progman
pdflatex progman
bibtex progman
pdflatex progman
pdflatex progman

%install
rm -rf %{buildroot} 
make install DESTDIR=%{buildroot}
find %{buildroot} -name *.la -delete
find %{buildroot} -name *.so.*.* -exec chmod 755 {} \;

# Create macro file
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.libint << EOF
# Current version of libint is
%_libint_apiversion %{apiversion}
EOF

%ldconfig_scriptlets

%ldconfig_scriptlets -n libderiv

%ldconfig_scriptlets -n libr12

%files
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libint*.so.*

%files -n libderiv
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libderiv*.so.*

%files -n libr12
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libr12*.so.*

%files devel
%doc doc/progman/progman.pdf
%{macrosdir}/macros.libint
%{_includedir}/libint/
%{_includedir}/libderiv/
%{_includedir}/libr12/
%{_libdir}/*.so

%changelog
%autochangelog
