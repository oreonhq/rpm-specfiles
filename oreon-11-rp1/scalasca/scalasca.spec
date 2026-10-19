%global source0_hash 17e72fd908be43879955e4ed49c2732d4dbda7d295fec2d8b3af7ddafe1202a0
%bcond_without mpich
%define shortver %(awk -F. '{print $1 "." $2}' <<<%version)
Name:		scalasca
Version:	2.6.2
Release:        1%{?dist}
Summary:        Toolset for performance analysis of large-scale parallel applications
License:	BSD-3-Clause AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:		http://www.scalasca.org/
Source0:        http://apps.fz-juelich.de/%{name}/releases/%{name}/2.6/dist/%{name}-%{version}.tar.gz
%if %{with mpich}
%endif
Requires:	scorep-config
ExcludeArch: s390 s390x armv7hl i686
%global desc \
Scalasca is a software tool that supports the performance optimization\
of parallel programs by measuring and analyzing their runtime\
behavior. The analysis identifies potential performance bottlenecks –\
in particular those concerning communication and synchronization – and\
offers guidance in exploring their causes.\
\
Scalasca targets mainly scientific and engineering applications based\
on the programming interfaces MPI and OpenMP, including hybrid\
applications based on a combination of the two. The tool has been\
specifically designed for use on large-scale systems, but is also well\
suited for small- and medium-scale HPC platforms.
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cube-libs-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  otf2-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%desc

%package openmpi
Summary:	Toolset for performance analysis of large-scale parallel applications - openmpi
Requires:	openmpi%{?_isa}
Requires:	scorep-openmpi-config
%description openmpi
%desc

%if 0%{?el7}
%package openmpi3
Summary:	Toolset for performance analysis of large-scale parallel applications - openmpi3
BuildRequires:	openmpi3-devel
Requires:	openmpi3%{?_isa}
Requires:	scorep-openmpi3-config
%description openmpi3
%desc

This is the openmpi3 version.
%endif

%if %{with mpich}
%package mpich
Summary:	Toolset for performance analysis of large-scale parallel applications - mpich
Requires:	mpich%{?_isa}
Requires:	scorep-mpich-config
%description mpich
%desc

This is the mpich version.
%endif

%package doc
Summary: Documentation for %name
BuildArch: noarch
%description doc
Documentation for %name

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mkdir openmpi mpich simple %{?el7:openmpi3}
rm -r vendor/cubew vendor/otf2	# bundled libraries

%build

%global _configure ../configure
%global do_build \
%configure --with-otf2 --with-cube --enable-shared --libdir=$MPI_LIB \\\
	   --bindir=$MPI_BIN --datadir=$MPI_HOME/share LDFLAGS=-Wl,--as-needed \\\
	   --enable-backend-test-runs --disable-silent-rules \\\
	   --mandir=$MPI_MAN --docdir=%_pkgdocdir \
	   %make_build
pushd openmpi
%_openmpi_load
%do_build
%_openmpi_unload
popd
%if 0%{?el7}
pushd openmpi3
%_openmpi3_load
%do_build
%_openmpi3_unload
popd
%endif
%if %{with mpich}
pushd mpich
%_mpich_load
%do_build
%_mpich_unload
popd
%endif
pushd simple
%configure --with-otf2 --with-cube --enable-shared LDFLAGS=-Wl,--as-needed \
	   --enable-backend-test-runs --disable-silent-rules --without-mpi \
	   --docdir=%_pkgdocdir
%make_build
popd
%install
%make_install -C openmpi
%{?el7:%make_install -C openmpi3}
%if %{with mpich}
%make_install -C mpich
%endif
%make_install -C simple
find $RPM_BUILD_ROOT%_libdir \( -name \*.la -o -name \*.a \) -exec rm -f {} \;
chrpath -d $RPM_BUILD_ROOT%_bindir/scout.{ser,omp}
chrpath -d $RPM_BUILD_ROOT%_libdir/{openmpi,mpich}/bin/scout.{ser,omp}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_openmpi_load
cd openmpi
OMPI_MCA_rmaps_base_oversubscribe=1 \
make check VERBOSE=1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n scalasca-openmpi -f %{oreon_filedir}/scalasca-openmpi.list
%files -n scalasca-mpich -f %{oreon_filedir}/scalasca-mpich.list
%files -n scalasca-doc -f %{oreon_filedir}/scalasca-doc.list

%changelog

%autochangelog
