%global source0_hash 18f162ca9cb8b3b05372b0ec3d02b4b8a4a7aabfc7b2abead350ddef8f048ecc

Name:           mpqc
Summary:        Ab-inito chemistry program
Version:        2.3.1
Release:        67%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.mpqc.org/
Source0:        http://downloads.sourceforge.net/mpqc/%{name}-%{version}.tar.bz2
Source1:        bash-script-noarch
Patch0:         mpqc-2.3.1-mdv-fix-wfn-lib.patch
Patch1:         mpqc-2.3.1-format-security.patch
# C++11 build fix
Patch2:         mpqc-2.3.1-cpp11-constexpr.patch
# C23 strict function prototype fix
Patch3:         mpqc-2.3.1-c23-function-prototype.patch
# C++17 build fix: remove deprecated exception specification
Patch4:         mpqc-2.3.1-cpp17-exception-specification.patch
# C++20 fix: std::istream operator>>(char *) removal
Patch5:         mpqc-2.3.1-cpp20-std_istream-redirect.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool flex bison
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-gfortran perl-generators
BuildRequires:  doxygen
BuildRequires:  /usr/bin/wish
BuildRequires:  libint-devel
BuildRequires:  flexiblas-devel

%description
MPQC is the Massively Parallel Quantum Chemistry Program. It computes
properties of atoms and molecules from first principles using the time
independent Schrödinger equation. It runs on a wide range of
architectures ranging from individual workstations to symmetric
multiprocessors to massively parallel computers. Its design is object
oriented, using the C++ programming language.

%package data
Summary:    Atom info and basis sets from MPQC
#Requires:   %{name}-doc = %{version}-%{release}
BuildArch:  noarch

%description data
Atom info and basis sets from MPQC.

%package doc
Summary:    HTML documentation for MPQC
BuildArch:  noarch

%description doc
This package contains the full documentation for MPQC that can be viewed
with a graphical browser like Mozilla.

%package libs
Summary:    Main libraries for %{name}
Requires:   %{name}-data = %{version}-%{release}
# Libint can have API breakage between releases
Requires:   libint(api)%{?_isa} = %{_libint_apiversion}

%description libs
This package contains the shared libraries needed to run programs
dynamically linked with %{name}, the scientific computing toolkit,
based on mpqc computational chemistry package from Sandia Labs.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and static libraries needed to
build programs linked with %{name}, the scientific computing toolkit,
based on mpqc computational chemistry package from Sandia Labs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .cpp11
%patch -P3 -p1 -b .c23
%patch -P4 -p1 -b .cpp17
%patch -P5 -p1 -b .cpp20

sed -i -e 's,molrender.in,%{_datadir}/molrender/molrender.in,g' src/bin/molrender/tkmolrender.in
sed -i -e 's,prefix/lib,prefix/%{_lib},g' configure.in
# fixup for modern autoreconf
mv configure.in configure.ac
sed -i -r -e 's/AC_DEFINE\(([^)]*)\)/AC_DEFINE([\1],1,[\1])/g' configure.ac
sed -i -r -e 's/AC_DEFINE_UNQUOTED\(([^,]*),([^)]*)\)/AC_DEFINE_UNQUOTED([\1],\2,[\1])/g' configure.ac
sed -i -r -e 's/AC_DEFINE_DIR\(([^,]*),([^)]*)\)/AC_DEFINE_DIR([\1],\2,[\1])/g' configure.ac
sed -i -r -e 's/AC_CANONICAL_SYSTEM/AC_CANONICAL_SYSTEM\nAC_DEFINE([SHMTYPE], [void *], [data type for shmat])/g' configure.ac
sed -i -r -e 's/AC_DEFINE\(\[CXX_RESTRICT\],1,\[CXX_RESTRICT\]\)/AC_DEFINE([restrictxx],[restrict],[have restrict keyword]),AC_DEFINE([restrictxx],[],[do not have restrict keyword])/g' configure.ac
# Make configure.ac c99 conformant, -Werror=implicit-int -Werror=implicit-function-declaration
sed -i -e '\@main.*FF@s|main|extern void FF(void); int main|' configure.ac
rm -f lib/autoconf/libtool.m4
# end autoreconf fixup
cat >molrender.desktop << EOF
[Desktop Entry]
Name=Molrender
Comment=Graphically render 3D molecules
Exec=%{_bindir}/tkmolrender
Icon=applications-science
Terminal=false
Type=Application
Categories=Education;Science;Chemistry;Physics;
Version=1.0
EOF

%build
export F77=gfortran
autoreconf -v -f -i -I lib/autoconf

%configure --enable-shared --disable-static \
    --enable-threads --disable-parallel \
    --includedir="%{_includedir}/mpqc"  \
    --with-cxx-optflags="$CXXFLAGS"     \
    --with-cc-optflags="$CFLAGS" \
    --with-libs="-lflexiblas"
sed -i 's|.rpath .libdir||g' bin/sc-config
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
cd doc
make
make man1
make man3

%install
make installroot="%{buildroot}" INSTALL="install -p" install
make installroot="%{buildroot}" INSTALL="install -p" install_devel
# rename some man pages with sc_ prefix
find doc/man/man3 -type f | grep -v '/sc' | while read a; do
    m=$(basename $a)
    d=$(dirname $a)
    mv "$a" "$d/sc_$m"
done
# install the man pages
mkdir %{buildroot}%{_mandir}
cp -r -p doc/man/* %{buildroot}%{_mandir}
install -D -p -m 644  src/bin/molrender/molrender.in %{buildroot}%{_datadir}/molrender/molrender.in
install -D -p -m 644  molrender.desktop %{buildroot}%{_datadir}/applications/molrender.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/molrender.desktop
find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;
find %{buildroot}%{_libdir} -name *.so.* -exec chmod 755 {} \;
sed -i -e "1,1s,^.*$,#!/usr/bin/perl," %{buildroot}%{_bindir}/sc-mkf77sym
sed -i -e "1,1s,^.*$,#!/usr/bin/perl -I%{_datadir}/mpqc/${_version}/perl," %{buildroot}%{_bindir}/chkmpqcout
chmod 755 %{buildroot}%{_bindir}/chkmpqcout

# Fix up sc-config all_libs
sed -i %{buildroot}%{_bindir}/sc-config \
	-e 's|^LIBSUF=la$|LIBSUF=so|' \
	-e '\@all_sclibs@s|\(lib[^ \t][^ \t]*\)\.la|\1.so|g' \
	-e 's|-L[^ \t]*gcc[^ \t]*||g' \
	%{nil}

# And rename arch-dependent script to arch-dependent name
for f in \
	sc-config \
	sc-libtool \
	%{nil}
do
	mv %{buildroot}%{_bindir}/${f}{,-$(arch)}
	cat %{SOURCE1} | sed -e "s|@BINARY@|$f|" > %{buildroot}%{_bindir}/${f}
	chmod 0755 %{buildroot}%{_bindir}/${f}
done

%ldconfig_scriptlets libs

%files
%doc CHANGES CITATION README
%{_bindir}/mpqc
%{_bindir}/chkmpqcout
%{_bindir}/scls
%{_bindir}/scpr
%{_bindir}/*run
%{_mandir}/man1/mpqc*
%{_mandir}/man1/scls*
%{_mandir}/man1/scpr*
%{_bindir}/molrender
%{_bindir}/tkmolrender
%{_datadir}/molrender
%{_datadir}/applications/molrender.desktop
%{_mandir}/man1/molrender*

%files data
%{_datadir}/mpqc
%license LICENSE COPYING COPYING.LIB

%files doc
%doc doc/html
%license LICENSE COPYING COPYING.LIB

%files libs
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/sc-*
%{_libdir}/lib*.so
%{_includedir}/mpqc
%{_mandir}/man1/sc-*
%{_mandir}/man3/sc*

%changelog
%autochangelog
