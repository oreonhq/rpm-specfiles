%global source0_hash a08c7e5bb280cdda02807628c1e805e8401c476aa8f121c579b6010cf4741f15
%global commit afc003fede96be54ebcd32f5cbf32eb570ede1b2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%bcond_without mpich
%bcond_without openmpi
Name:           libneurosim
Version:        1.2.0
Release:        1%{?dist}
Summary:        Common interfaces for neuronal simulators
License:        GPL-3.0-or-later
URL:            https://github.com/INCF/%{name}
Source0:        https://github.com/INCF/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         libneurosim-afc003f-py312-disutils-removal.patch
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  python3-devel
BuildRequires:  rpm-mpi-hooks
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        common
Summary:        Common files for %{name}
BuildArch:      noarch
%description    common
The %{name}-common package contains files required by all sub packages.

%if %{with openmpi}
%package openmpi
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-common = %{version}-%{release}
%description openmpi

%package openmpi-devel
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel

%endif

%if %{with mpich}
%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
Requires:       %{name}-common = %{version}-%{release}
%description mpich

%package mpich-devel
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires: make
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -n %{name}-%{commit} -N
(
cd %{name}-%{commit}
%patch -P0 -p1
)

# Do not build bundled libltdl
# sed -i -e '/AC_CONFIG_SUBDIRS(libltdl)/ d' -e '/LTDL_DIR/ d' -e '/_LTDL_CON/ d' %{name}-%{commit}/configure.ac
# sed -i 's/libltdl//' %{name}-%{commit}/Makefile.am

# Make these accessible here
cp -v %{name}-%{commit}/COPYING .
cp -v %{name}-%{commit}/README.md .

# Default is py3
%if %{with mpich}
    cp -a %{name}-%{commit} %{name}-%{commit}-mpich
%endif

%if %{with openmpi}
    cp -a %{name}-%{commit} %{name}-%{commit}-openmpi
%endif

%build

%global do_build %{expand:
pushd %{name}-%{commit}$MPI_COMPILE_TYPE && \
./autogen.sh && \
%{set_build_flags} \
./configure CC=$MPICC CXX=$MPICXX --disable-static \\\
--disable-silent-rules \\\
--with-python=$PYTHON_VERSION \\\
--with-mpi=$MPI_YES \\\
--prefix=$MPI_HOME \\\
--libdir=$MPI_LIB \\\
--includedir=$MPI_INCLUDE \\\
--bindir=$MPI_BIN \\\
--mandir=$MPI_MAN && \
%make_build STRIP=/bin/true && \
popd || exit -1
}
MPI_COMPILE_TYPE=""
PYTHON_VERSION=3
MPI_YES="no"
MPI_HOME=%{_prefix}
MPI_LIB=%{_libdir}
MPI_INCLUDE=%{_includedir}
MPI_BIN=%{_bindir}
MPI_MAN=%{_mandir}
MPICC=%{__cc}
MPICXX=%{__cxx}
%{do_build}
%if %{with mpich}
%{_mpich_load}
MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
MPI_YES="yes"
MPICC=mpicc
MPICXX=mpicxx
%{do_build}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
MPI_YES="yes"
MPICC=mpicc
MPICXX=mpicxx
%{do_build}
%{_openmpi_unload}
%endif
%install
%global do_install \
%make_install -C %{name}-%{commit}$MPI_COMPILE_TYPE STRIP=/bin/true || exit -1
MPI_COMPILE_TYPE=""
PYTHON_VERSION=3
%{do_install}
%if %{with mpich}
%{_mpich_load}
MPI_TYPE="mpich"
MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
PY_VERSION=%{python3_version}
%{do_install}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
MPI_TYPE="openmpi"
MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
PY_VERSION=%{python3_version}
%{do_install}
%{_openmpi_unload}
%endif
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libneurosim-devel -f %{oreon_filedir}/libneurosim-devel.list
%files -n libneurosim-common -f %{oreon_filedir}/libneurosim-common.list
%files -n libneurosim-openmpi -f %{oreon_filedir}/libneurosim-openmpi.list
%files -n libneurosim-openmpi-devel -f %{oreon_filedir}/libneurosim-openmpi-devel.list
%files -n libneurosim-mpich -f %{oreon_filedir}/libneurosim-mpich.list
%files -n libneurosim-mpich-devel -f %{oreon_filedir}/libneurosim-mpich-devel.list

%changelog

%autochangelog
