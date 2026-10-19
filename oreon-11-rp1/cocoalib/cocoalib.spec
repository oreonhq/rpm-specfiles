%global source0_hash d3e7af0153c6950f83f4e3556540f0177fedf5179f0f7667b7d6d670268fd445
%global baseurl https://cocoa.altervista.org/cocoalib
Name:           cocoalib
Version:        0.99850
Release:        1%{?dist}
Summary:        C++ library for computations in commutative algebra
License:        GPL-3.0-or-later
URL:            %{baseurl}/index.shtml
VCS:            git:https://github.com/cocoa-official/CoCoALib.git
Source0:        %{baseurl}/tgz/CoCoALib-%{version}.tgz
Patch:          %{name}-shared.patch
Patch:          %{name}-ffelem.patch
Patch:          %{name}-vec.patch
Patch:          %{name}-uninit.patch
Patch:          %{name}-cvc5.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libfrobby-devel
BuildRequires:  libgfan-devel
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)
# /oreon:deps
%description
The CoCoA C++ library offers functions to perform calculations in
Computational Commutative Algebra, and some other related areas.  The library
is designed to be pleasant to use while offering good run-time performance.

%package devel
Summary:        Headers and library links for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       gsl-devel%{?_isa}
Requires:       libgfan-devel%{?_isa}
%description devel
Headers and library links for developing applications that use %{name}.

%package doc
License:        GFDL-1.2-no-invariants-only AND Knuth-CTAN
Summary:        Documentation for %{name}
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n CoCoALib-%{version}

%conf
# Use FlexiBLAS instead of the reference lapack/blas implementation.
# Do not throw away our choice of compiler flags.
# Fix the location of the cddlib headers.
sed -e 's,-lgslcblas  -llapack,-lflexiblas,' \
    -e 's/ -Wall  -pedantic/ $CXXFLAGS/' \
    -e 's,\(CDD_INC_DIR=\)".*",\1"%{_includedir}/cddlib",' \
    -i configure

# Do not suppress compiler command lines
sed -i 's/\$(MAKE) -s/\$(MAKE)/' Makefile doc/Makefile src/Makefile \
    src/AlgebraicCore/Makefile src/AlgebraicCore/TmpFactorDir/Makefile

%build

sed -i 's|@RPM_LD_FLAGS@|%{build_ldflags}|' src/AlgebraicCore/Makefile
./configure --prefix=%{_prefix} --only-cocoalib --threadsafe-hack \
  --with-cxxflags='%{build_cxxflags} -fPIC -I%{_includedir}/frobby -I%{_includedir}/gfanlib %{build_ldflags}' \
  --with-libcddgmp=%{_libdir}/libcddgmp.so \
  --with-libfrobby=%{_libdir}/libfrobby.so \
  --with-libgfan=%{_libdir}/libgfan.so \
  --with-libgsl=%{_libdir}/libgsl.so
%make_build library
%make_build doc
%install
mkdir -p %{buildroot}%{_libdir}
cp -p src/AlgebraicCore/libcocoa.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcocoa.so.0.0.0 %{buildroot}%{_libdir}/libcocoa.so.0
ln -s libcocoa.so.0 %{buildroot}%{_libdir}/libcocoa.so
mkdir -p %{buildroot}%{_includedir}
cp -a include/CoCoA %{buildroot}%{_includedir}
rm -f %{buildroot}%{_includedir}/{MakeUnifiedHeader.sh,PREPROCESSOR_DEFNS.H-old}
rm -f doc/CoCoALib-tasks/{HTMLTasks,HTMLTasks.C,Makefile,tasks.xml}
rm -f examples/CopyInfo
chmod a-x examples/*.sh
%oreon_autofiles cocoalib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cocoalib-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$PWD/lib
make check
%files -f %{oreon_filedir}/main.list
%files -n cocoalib-devel -f %{oreon_filedir}/cocoalib-devel.list
%files -n cocoalib-doc -f %{oreon_filedir}/cocoalib-doc.list

%changelog

%autochangelog
