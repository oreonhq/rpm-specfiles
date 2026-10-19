%global source0_hash 798015e81d4bc8235f3001b84bab06fdf0ad0f7fd1d2d6513ef109d9e6726727
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global commit 29a6a6df4cd1242c54b5651fc0ac6dd563edf7c0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global apiversion 0
Name:           libint
Version:        1.2.1
Release:        26%{?dist}
Summary:        A library for computing electron repulsion integrals efficiently
License:        LGPL-3.0-only
URL:            http://sourceforge.net/p/libint
Source0:        https://github.com/evaleev/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch1:         libint-1.2.1-maxnode.patch
Patch2:         libint-1.2.1-soname.patch
Patch3:         https://github.com/evaleev/libint/pull/353.patch
Provides:       libint(api)%{?_isa} = %{apiversion}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-collection-latexrecommended
# /oreon:deps
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

ulimit -s unlimited
%configure --enable-shared --disable-static \
 --with-libint-max-am=10 --with-libint-opt-am=6 \
 --with-libderiv-max-am1=6 --with-libderiv-max-am2=5 \
 --with-libr12-max-am=5 --with-libr12-opt-am=4
oflags=`echo %{optflags} | sed -E 's/(^| )-O(0|1|2|3|s|fast)( |$)/\1-O1\3/g'`
make V=0 CFLAGS="${oflags}" CXXFLAGS="${oflags}" %{?_smp_mflags} > build.log 2>&1 || {
  status=$?
  cat build.log
  exit $status
}
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
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.libint << EOF
%_libint_apiversion %{apiversion}
EOF
%ldconfig_scriptlets
%ldconfig_scriptlets -n libderiv
%ldconfig_scriptlets -n libr12
%oreon_autofiles libr12 usr/*/lib*.so.*
%oreon_autofiles libderiv usr/*/lib*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libint-devel -f %{oreon_filedir}/libint-devel.list
%files -n libr12 -f %{oreon_filedir}/libr12.list
%files -n libderiv -f %{oreon_filedir}/libderiv.list

%changelog

%autochangelog
