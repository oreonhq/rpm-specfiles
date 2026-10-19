%global source0_hash ab833757e1e4d4a98662f4aa691394013ea9a226f6416b8f8565356d6fcc989e
Name:           gfan
Version:        0.7
Release:        1%{?dist}
Summary:        Software for Computing Gröbner Fans and Tropical Varieties
License:        GPL-2.0-or-later
URL:            https://math.au.dk/~jensen/software/gfan/gfan.html
Source0:        https://math.au.dk/~jensen/software/%{name}/%{name}%{version}.tar.gz
Patch:          %{name}-warning.patch
Patch:          %{name}-shared.patch
Patch:          %{name}-soplex.patch
Patch:          %{name}-c++20.patch
Patch:          %{name}-gcd.patch
Patch:          %{name}-multiplicities.patch
ExcludeArch:    %{ix86}
Requires:       libgfan%{_isa} = %{version}-%{release}
Recommends:     TOPCOM
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  TOPCOM
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glibc-langpack-en
BuildRequires:  gmp-devel
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)
# /oreon:deps
%description
The software computes all marked reduced Gröbner bases of an ideal.  Their
union is a universal Gröbner basis. Gfan contains algorithms for computing
this complex for general ideals and specialized algorithms for tropical
curves, tropical hypersurfaces and tropical varieties of prime ideals.  In
addition to the above core functions the package contains many tools which are
useful in the study of Gröbner bases, initial ideals and tropical geometry.
Among these are an interactive traversal program for Gröbner fans and programs
for graphical renderings.

%package        doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Gfan examples and documentation files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    doc
Gfan examples and documentation files.

%package        -n libgfan
Summary:        Polyhedral computations related to polynomial rings
%description    -n libgfan
Gfanlib has two major features:
1) high-level exact polyhedral cone and polyhedral fan classes;
2) fast exact mixed volume computation for lattice polytopes with overflow
   checking.

In particular, gfanlib is missing the Gröbner basis part of gfan.

%package        -n libgfan-devel
Summary:        Development files for libgfan
Requires:       libgfan%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description    -n libgfan-devel
The libgfan-devel package contains libraries and header files for developing
applications that use libgfan.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}%{version} -p1

%conf
# Point to where the TOPCOM binaries will be installed
sed -i.orig "s|^\(#define MINKOWSKIPROGRAM \).*|\1\"%{_bindir}/essai\"|" \
  src/minkowskisum.cpp
touch -r src/minkowskisum.cpp.orig src/minkowskisum.cpp
rm -f src/minkowskisum.cpp.orig

# No need to install a simple upstream Makefile to rsync homepage
# directory to upstream page.
rm -f homepage/Makefile

%build

sed -e 's|^\(SOPLEX_PATH = \).*|\1%{_prefix}|' \
    -e 's|^\(SOPLEX_LINKOPTIONS = \).*|\1%{build_ldflags} -lsoplex -lclusol -lmpfr -ltbb -lz-ng|' \
    -e 's|^\(SOPLEX_INCLUDEOPTIONS = \).*|\1|' \
    -i Makefile
%make_build CC=gcc CXX=g++ \
  OPTFLAGS='%{build_cxxflags} -DGMPRATIONAL -DNDEBUG -I%{_includedir}/cddlib' \
  PREFIX=%{_prefix} \
  soplex=true
cd doc
latex manual.tex
bibtex manual
latex manual.tex
latex manual.tex
dvipdf manual.dvi manual.pdf
cd -
%install
mkdir -p %{buildroot}%{_libdir}
cp -p src/libgfan.so.0.0.0 %{buildroot}%{_libdir}
ln -s libgfan.so.0.0.0 %{buildroot}%{_libdir}/libgfan.so.0
ln -s libgfan.so.0 %{buildroot}%{_libdir}/libgfan.so
mkdir -p %{buildroot}%{_includedir}/gfanlib
cp -p src/gfanlib*.h %{buildroot}%{_includedir}/gfanlib
for fil in %{buildroot}%{_includedir}/gfanlib/*.h; do
  sed -i.orig 's,#include "\(.*\)",#include <\1>,' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make install PREFIX=%{buildroot}%{_prefix}
cd %{buildroot}%{_bindir}
    ./%{name} installlinks
cd -
%oreon_autofiles libgfan usr/*/lib*.so.*
%oreon_autofiles libgfan-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LC_ALL=en_US.UTF-8
rm -fr testsuite/0009RenderStairCase
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
./gfan _test
%files -f %{oreon_filedir}/main.list
%files -n gfan-doc -f %{oreon_filedir}/gfan-doc.list
%files -n libgfan -f %{oreon_filedir}/libgfan.list
%files -n libgfan-devel -f %{oreon_filedir}/libgfan-devel.list

%changelog

%autochangelog
