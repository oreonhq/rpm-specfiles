%global source0_hash 7bf8160ba4f261b8fa14bf8ceab318912b8b8d8a1d8e653c6fbdd45eb27a51c7
%global forgeurl https://github.com/INCF/MUSIC/
%bcond_without mpich
%bcond_without openmpi
%global lname music
Name:           MUSIC
Version:        1.2.1
Release:        1%{?dist}
Summary:        The MUltiSimulation Coordinator
%global tag %{version}
%forgemeta
License:        GPL-3.0-or-later
URL:            %forgeurl
Source0:        %{forgeurl}archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Patch:         0001-Disable-sysguess.patch
Patch:         0002-Enable-tests-and-extras.patch
Patch:         0003-Make-python-bits-ourselves.patch
Patch:         0004-Make-bundled-rudeconfig-also-follow-all-flags.patch
Patch:         0005-Remove-src-flags.patch
Provides:       bundled(rudeconfig) = 5.0.5-1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  patch
BuildRequires:  python3-devel
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(looseversion)
BuildRequires:  python3dist(setuptools)
BuildRequires:  rpm-mpi-hooks
# /oreon:deps
%description
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%package common
Summary:    Architecture independent test and example files for %{name}
BuildArch:  noarch
%description common
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
%description mpich
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%package mpich-devel
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
Development files for %{name} built with MPICH.

%package -n python3-%{name}-mpich
Summary:        Python3 support for %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich
Requires:       python3-mpi4py-mpich
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description -n python3-%{name}-mpich
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%package openmpi
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
%description openmpi
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%package openmpi-devel
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
Development files for %{name} built with MPICH.

%package -n python3-%{name}-openmpi
Summary:        Python3 support for %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi
Requires:       python3-mpi4py-openmpi
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description -n python3-%{name}-openmpi
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -n %{name}-%{version} -N
# Unable to use autosetup directly because we need three copies of the source
# in here now
# Apply patches
pushd %{name}-%{version}
%patch -p1 -P 0 1 2 3 4
# on Fedora, we have mpichversion, not mpich2version
sed -i 's|mpich2version|mpichversion|' configure.ac
popd

cp %{name}-%{version}/LICENSE .
cp %{name}-%{version}/README .

%if %{with mpich}
    cp -a %{name}-%{version} %{name}-%{version}-mpich
%endif

%if %{with openmpi}
    cp -a %{name}-%{version} %{name}-%{version}-openmpi
%endif

%build

%global do_build %{expand:
echo "** BUILDING $MPI_COMPILE_TYPE **"
pushd %{name}-%{version}$MPI_COMPILE_TYPE
./autogen.sh &&
%{set_build_flags}
MPI_CXXFLAGS="$CXXFLAGS $(pkg-config --cflags $MPI_VARIANT)"
MPI_CFLAGS="$CFLAGS $(pkg-config --cflags $MPI_VARIANT)"
MPI_LDFLAGS="$LDFLAGS $(pkg-config --libs $MPI_VARIANT | sed 's|-Lsystem/lib||')"
./configure LAUNCHSTYLE="_mpirun" SYSGUESS="$SYSGUESS" CXX=mpicxx CC=mpicc MPI_CXXFLAGS="$MPI_CXXFLAGS" MPI_CFLAGS="$MPI_CFLAGS" MPI_LDFLAGS="$MPI_LDFLAGS" PYTHON="$PYTHON_BIN" \\\
--disable-static \\\
--prefix=$MPI_HOME \\\
--libdir=$MPI_LIB \\\
--includedir=$MPI_INCLUDE \\\
--bindir=$MPI_BIN \\\
--mandir=$MPI_MAN
%make_build
pushd pymusic
%{py3_build}
popd
popd
}
%if %{with mpich}
%{_mpich_load}
MPI_VARIANT="mpich"
SYSGUESS="mpich"
MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
PYTHON_BIN="%{python3}"
%{do_build}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
MPI_VARIANT="ompi-cxx"
SYSGUESS="openmpi"
MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
PYTHON_BIN="%{python3}"
%{do_build}
%{_openmpi_unload}
%endif
%install
%global do_install %{expand:
%make_install -C %{name}-%{version}$MPI_COMPILE_TYPE
mv $RPM_BUILD_ROOT/$MPI_HOME/lib/%{lname}-%{version}/* $RPM_BUILD_ROOT/$MPI_BIN/ -v && rm -vrf $RPM_BUILD_ROOT/$MPI_HOME/lib/%{lname}-%{version}
for f in contsink eventcounter eventgenerator eventlogger eventselect eventsink eventsource messagesource music viewevents waveconsumer waveproducer clocksource constsource contdelay eventdelay launchtest multiport musicrun test_ag
do
    if [ -e  "$RPM_BUILD_ROOT/$MPI_BIN/$f" ]; then
        echo "Renaming $f"
        mv "$RPM_BUILD_ROOT/$MPI_BIN/$f" "$RPM_BUILD_ROOT/$MPI_BIN/$f$MPI_SUFFIX" -v
    fi
done
rm -f "$RPM_BUILD_ROOT/$MPI_BIN/music_tests.sh"
pushd %{name}-%{version}$MPI_COMPILE_TYPE/pymusic
%{python3} setup.py install --skip-build --root $RPM_BUILD_ROOT --install-lib=$MPI_PYTHON3_SITEARCH
popd
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/config" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}/"
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/pymusic.so" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}"
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/pybuffer.so" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}"
}
%if %{with mpich}
%{_mpich_load}
MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{_openmpi_unload}
%endif
%if %{with mpich} || %{with openmpi}
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/%{lname}/
mv $RPM_BUILD_ROOT/%{_libdir}/mpich/share/%{lname}-%{version}/tests $RPM_BUILD_ROOT/%{_datadir}/%{lname}/ || exit 0
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/doc/%{lname}/
mv $RPM_BUILD_ROOT/%{_libdir}/mpich/share/%{lname}-%{version}/examples $RPM_BUILD_ROOT/%{_datadir}/doc/%{lname}/ || exit 0
rm -vrf $RPM_BUILD_ROOT/%{_libdir}/mpich/share || exit 0
rm -vrff $RPM_BUILD_ROOT/%{_libdir}/openmpi/share || exit 0
%endif
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles MUSIC-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles MUSIC-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles MUSIC-mpich-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-MUSIC-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles MUSIC-openmpi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles MUSIC-openmpi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-MUSIC-openmpi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n MUSIC-common -f %{oreon_filedir}/MUSIC-common.list
%files -n MUSIC-mpich -f %{oreon_filedir}/MUSIC-mpich.list
%files -n MUSIC-mpich-devel -f %{oreon_filedir}/MUSIC-mpich-devel.list
%files -n python3-MUSIC-mpich -f %{oreon_filedir}/python3-MUSIC-mpich.list
%files -n MUSIC-openmpi -f %{oreon_filedir}/MUSIC-openmpi.list
%files -n MUSIC-openmpi-devel -f %{oreon_filedir}/MUSIC-openmpi-devel.list
%files -n python3-MUSIC-openmpi -f %{oreon_filedir}/python3-MUSIC-openmpi.list

%changelog

%autochangelog
