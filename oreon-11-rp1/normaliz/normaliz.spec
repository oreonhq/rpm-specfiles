%global source0_hash 10af3bd1e4e44f543867b51e7678c4f5dca55050dae02835fda9f2668aac0d0a
%global giturl  https://github.com/Normaliz/Normaliz
Name:           normaliz
Version:        3.11.1
Release:        1%{?dist}
Summary:        A tool for discrete convex geometry
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Bitstream-Vera AND Knuth-CTAN AND GPL-1.0-or-later AND LicenseRef-DoubleStroke AND AGPL-3.0-only AND LicenseRef-Rsfs
URL:            https://www.normaliz.uni-osnabrueck.de/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-hash-library.patch
Patch:          %{name}-nauty2.9.patch
ExcludeArch:    %{ix86}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cocoalib-devel
BuildRequires:  e-antic-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libnauty)
# /oreon:deps
%description
Normaliz is a tool for computations in affine monoids, vector configurations,
rational polyhedra, and rational cones.  Normaliz now computes rational and
algebraic polyhedra, i.e., polyhedra defined over real algebraic extensions of
QQ.

Documentation and examples can be found in %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}},
in particular you may find Normaliz%{version}Documentation.pdf useful.  

%package -n libnormaliz
License:        GPL-3.0-or-later
Summary:        Normaliz internals as a library
%description -n libnormaliz
This package contains the normaliz internals as a library, often called
libnormaliz.

%package -n libnormaliz-devel
License:        GPL-3.0-or-later
Summary:        Developer files for libnormaliz
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       cocoalib-devel%{?_isa}
Requires:       e-antic-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
%description -n libnormaliz-devel
Header files and library links to develop applications that use the Normaliz
internals as a library (libnormaliz).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n Normaliz-%{version}

%conf
# Update the configuration for Fedora
sed -e 's|-funroll-loops|%{build_cxxflags} -I%{_includedir}/gfanlib|' \
    -e 's|-O3|-O2|' \
    -e 's|STRIP_FLAGS = .*|CXXFLAGS += -g|' \
    -i source/Makefile.configuration

# Do not strip the binary
sed -i 's|AM_LDFLAGS = -Wl,-s|AM_CXXFLAGS += -g|' source/Makefile.am

# Generate configure
autoreconf -fi .

%build

export CPPFLAGS="-I%{_includedir}/arb -I%{_includedir}/gfanlib"
%configure \
  --disable-silent-rules \
  --disable-static \
  --with-cocoalib=%{_prefix} \
  --with-hashlibrary=%{_prefix}
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
mkdir -p docs/example
pushd example
for file in *.in
do
    sed 's/\r//' "$file" > "../docs/example/$file"
    touch -r "$file" "../docs/example/$file"
done
popd
export LD_LIBRARY_PATH=$PWD/source/.libs
help2man -s 1 -o normaliz.1 -N -n 'A tool for discrete convex geometry' \
  source/.libs/normaliz
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_mandir}/man1
cp -p normaliz.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles libnormaliz usr/*/lib*.so.*
%oreon_autofiles libnormaliz-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x
LD_LIBRARY_PATH=$PWD/source/.libs make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n libnormaliz -f %{oreon_filedir}/libnormaliz.list
%files -n libnormaliz-devel -f %{oreon_filedir}/libnormaliz-devel.list

%changelog

%autochangelog
