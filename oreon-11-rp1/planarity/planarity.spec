%global source0_hash 76fe578ff18f11d9acdd05299ffcad5f57915174e0634d4665dd5e2c1ad22639
Name:		planarity
Summary:        Implementations of several planarity-related graph algorithms
Version:	5.1.0.0
Release:        1%{?dist}
License:	BSD-3-Clause
URL:		https://github.com/graph-algorithms/edge-addition-planarity-suite
VCS:		git:%{url}.git
Source0:        https://github.com/graph-algorithms/edge-addition-%{name}-suite/archive/Version_%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	%{ix86}
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This code project provides a library for implementing graph algorithms as well
as implementations of several planarity-related graph algorithms.  The origin
of this project is the reference implementation for the Edge Addition
Planarity Algorithm, which is now the fastest and simplest linear-time method
for planar graph embedding and planarity obstruction isolation (i.e.
Kuratowski subgraph isolation).

The software in this code project provides a graph algorithm framework and
library, including an updated version of the edge addition combinatorial
planar graph embedder and planar obstruction isolator (i.e., a Kuratowski
subgraph isolator). This code project also includes several extensions that
implement planarity-related algorithms such as a planar graph drawing
algorithm, an outerplanar graph embedder and outerplanar obstruction isolator,
and a number of subgraph homeomorphism search algorithms.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
This package contains the header files and development documentation for
%{name}.

%package	samples
Summary:	Sample files for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description	samples
This package contains sample files for planarity.  For example:

planarity -test /usr/share/doc/planarity/samples

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n edge-addition-%{name}-suite-Version_%{version}

%conf
# Generate the configure script
autoreconf -fi .

%build

%configure --enable-static=false
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool
%make_build
%install
%make_install
rm -rf %{buildroot}%{_docdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n planarity-devel -f %{oreon_filedir}/planarity-devel.list
%files -n planarity-samples -f %{oreon_filedir}/planarity-samples.list

%changelog

%autochangelog
