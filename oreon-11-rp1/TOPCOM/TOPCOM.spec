%global source0_hash 4fb10754ee5b76056441fea98f2c8dee5db6f2984d8c14283b49239ad4378ab6

Name:           TOPCOM
Version:        1.1.2
Release:        12%{?dist}
Summary:        Triangulations Of Point Configurations and Oriented Matroids

%global upver %(tr . _ <<< %{version})

License:        GPL-2.0-or-later
URL:            https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/
VCS:            git:%{url}.git
Source0:        https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM-Downloads/%{name}-%{upver}.tgz
# A replacement Makefile.  See the %%build section for more information.
Source1:        %{name}-Makefile
# Remove a pessimizing call to std::move
Patch:          %{name}-pessimizing-move.patch
# Add virtual destructors where needed
Patch:          %{name}-virtual-destructor.patch
# Adapt to SoPlex 8.0.0
Patch:          %{name}-soplex.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cddlib)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  qsopt-ex-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global topcom_major %(cut -d. -f1 <<< %{version})
%global topcom_minor %(cut -d. -f2 <<< %{version})

%description
TOPCOM is a package for computing Triangulations Of Point Configurations and
Oriented Matroids.  It was very much inspired by the maple program PUNTOS,
which was written by Jesus de Loera.  TOPCOM is entirely written in C++, so
there is a significant speed up compared to PUNTOS.

%package devel
Summary:        Header files needed to build with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cddlib-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       qsopt-ex-devel%{?_isa}

%description devel
Header files needed to build applications that use the %{name} library.

%package libs
Summary:        Core %{name} functionality in a library

%description libs
Command line tools that expose %{name} library functionality.

%package examples
Summary:        Example inputs and outputs for TOPCOM
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example input and output files for TOPCOM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n topcom-%{version} -p1

%conf
# Fix character encoding
iconv -f iso8859-1 -t utf8 -o README.utf8 README
touch -r README README.utf8
mv -f README.utf8 README

# Mimic upstream's modification of gmpxx.h, using the system gmpxx.h
mkdir -p external/include
sed "s|// \(q\.canonicalize\)|\1|" %{_includedir}/gmpxx.h > \
  external/include/gmpxx.h

%build
# We cannot use upstream's build system.  It has the following problems.
# (1) It builds two static libraries, libTOPCOM.a and libCHECKREG.a, then
#     includes both libraries in each of the 60 binaries that it installs in
#     %%{_bindir}.
# (2) Each of libTOPCOM.a and libCHECKREG.a refers to symbols defined by the
#     other.
# (3) It builds static cddlib and qsopt_ex libraries, which are also linked into
#     all of the constructed binaries.  There is no way to make it use the
#     installed versions of those libraries instead.
# We could fix (3) with a little build system hackery.  We could fix (1) by
# building shared libraries, but that doesn't help with (2).  Instead, we pull
# in our own evilly constructed Makefile to build a single shared library
# containing all of the object files in both libTOPCOM.a and libCHECKREG.a,
# and link the binaries against that and the system cddlib and qsopt_ex
# libraries.
sed -e 's|@RPM_OPT_FLAGS@|%{build_cxxflags}|' \
    -e 's|@RPM_LD_FLAGS@|%{build_ldflags}|' \
    -e 's|@bindir@|%{_bindir}|' \
    -e 's|@libdir@|%{_libdir}|' \
    -e 's|@includedir@|%{_includedir}|' \
    -e 's|@version@|%{version}|' \
    -e 's|@major@|%{topcom_major}|' \
    -e 's|@minor@|%{topcom_minor}|' \
    -e 's|#version#|@version@|' \
    %{SOURCE1} > Makefile
%make_build

%install
%make_install

# Get rid of the Makefiles in the examples dir before packaging
rm -f examples/Makefile*

# Rename binaries with common names
for bin in cross cube cyclic hypersimplex lattice; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/TOPCOM-$bin
done

# Do not package the check executable
rm %{buildroot}%{_bindir}/check

%check
LD_LIBRARY_PATH=$PWD src/check

%files
%{_bindir}/B_A
%{_bindir}/B_A_center
%{_bindir}/B_D
%{_bindir}/B_D_center
%{_bindir}/B_S
%{_bindir}/B_S_center
%{_bindir}/TOPCOM*
%{_bindir}/binomial
%{_bindir}/checkregularity
%{_bindir}/chiro2*
%{_bindir}/cocircuits2facets
%{_bindir}/Dnxk
%{_bindir}/kDn
%{_bindir}/permutahedron
%{_bindir}/points2*
%{_bindir}/santos_*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libTOPCOM.so

%files libs
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/libTOPCOM.so.1{,.*}

%files examples
%doc examples

%changelog
%autochangelog
