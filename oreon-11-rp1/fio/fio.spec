%global source0_hash cc1b5c8ef9efa20d44fe90b59515fddf8b4e884d782a0b33b26a70ab48ec04c1

Name:		fio
Version:	3.40
Release:	3%{?dist}
Summary:	Multithreaded IO generation tool

License:	GPL-2.0-only
URL:		http://git.kernel.dk/?p=fio.git;a=summary
Source0:        http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
Source1:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2.asc
Source2:	https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/F7D358FB2971E0A6.asc

%if 0%{?rhel} && 0%{?rhel} < 10
%bcond_without nbd
%ifarch x86_64 ppc64le
%bcond_without pmem
%endif
%ifnarch %{arm} %{ix86}
%bcond_without rbd
%bcond_without rados
%endif
%bcond_with tcmalloc
%else
%bcond nbd 1
%ifarch x86_64 ppc64le
%bcond pmem %{undefined rhel}
%endif
%ifnarch %{arm} %{ix86}
%bcond rbd 1
%bcond rados 1
%endif
# set to %%{undefined rhel} if enabling for Fedora
%bcond tcmalloc 0
%endif

%bcond_with xnvme
%bcond_with cuda

BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	libaio-devel
BuildRequires:	zlib-devel
BuildRequires:	python3-devel
%if %{with nbd}
BuildRequires:	libnbd-devel
%endif
BuildRequires:	libcurl-devel
BuildRequires:	openssl-devel
%if %{with pmem}
BuildRequires:	libpmem-devel
%endif

%if %{with rbd}
BuildRequires:	librbd1-devel
%endif

%if %{with tcmalloc}
BuildRequires:	gperftools-devel
%endif

%if %{with xnvme}
BuildRequires:	xnvme-devel
%endif

%if %{with cuda}
BuildRequires:	libcufile.so.0()(64bit)
%endif

%ifnarch %{arm}
BuildRequires:	numactl-devel
BuildRequires:	librdmacm-devel
BuildRequires:  libnl3-devel
%endif
BuildRequires: make

# Don't create automated dependencies for the fio engines.
# https://bugzilla.redhat.com/show_bug.cgi?id=1884954
%global __provides_exclude_from ^%{_libdir}/fio/

# Main fio package has soft dependencies on all the engine
# subpackages, but allows the engines to be uninstalled if not needed
# or if the dependencies are too onerous.
Recommends:     %{name}-engine-libaio
Recommends:     %{name}-engine-http
%if %{with nbd}
Recommends:     %{name}-engine-nbd
%endif
%if %{with pmem}
Recommends:     %{name}-engine-dev-dax
Recommends:     %{name}-engine-libpmem
%endif
%if %{with rados}
Recommends:     %{name}-engine-rados
%endif
%if %{with rbd}
Recommends:     %{name}-engine-rbd
%endif
%if %{with xnvme}
Recommends:     %{name}-engine-xnvme
%endif
%if %{with cuda}
Recommends:     %{name}-engine-cuda
%endif
%ifnarch %{arm}
Recommends:     %{name}-engine-rdma
%endif

%description
fio is an I/O tool that will spawn a number of threads or processes doing
a particular type of io action as specified by the user.  fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%package engine-libaio
Summary:        Linux libaio engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-libaio
Linux libaio engine for %{name}.

%package engine-http
Summary:        HTTP engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-http
HTTP engine for %{name}.

%if %{with nbd}
%package engine-nbd
Summary:        Network Block Device engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-nbd
Network Block Device (NBD) engine for %{name}.
%endif

%if %{with pmem}
%package engine-dev-dax
Summary:        PMDK dev-dax engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-dev-dax
dev-dax engine for %{name}.
Read and write using device DAX to a persistent memory device
(e.g., /dev/dax0.0) through the PMDK libpmem library.
%endif

%if %{with pmem}
%package engine-libpmem
Summary:        PMDK pmemblk engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-libpmem
libpmem engine for %{name}.
Read and write using mmap I/O to a file on a filesystem mounted with DAX
on a persistent memory device through the PMDK libpmem library.
%endif

%if %{with rados}
%package engine-rados
Summary:        Rados engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-rados
Rados engine for %{name}.
%endif

%if %{with rbd}
%package engine-rbd
Summary:        Rados Block Device engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-rbd
Rados Block Device (RBD) engine for %{name}.
%endif

%if %{with xnvme}
%package engine-xnvme
Summary:        XNVME engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-xnvme
XNVME engine for %{name}.
%endif

%if %{with cuda}
%package engine-cuda
Summary:        cuda engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-cuda
cuda engine for %{name}.
%endif


%ifnarch %{arm}
%package engine-rdma
Summary:        RDMA engine for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description engine-rdma
RDMA engine for %{name}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn \
 tools/fio_jsonplus_clat2csv \
 tools/fiologparser.py \
 tools/hist/*.py \
 tools/plot/fio2gnuplot \
 t/steadystate_tests.py

# Edit /usr/local/lib path in os/os-linux.h to match Fedora conventions.
sed -e 's,/usr/local/lib/,%{_libdir}/,g' -i os/os-linux.h

%build

%if %{with cuda}
export C_INCLUDE_PATH=/usr/local/cuda/include
export CPLUS_INCLUDE_PATH=/usr/local/cuda/include
export LIBRARY_PATH=/usr/local/cuda/lib64
%endif

./configure \
 %{?with_nbd:--enable-libnbd} \
 %{!?with_xnvme:--disable-xnvme} \
 %{?with_cuda:--enable-cuda --enable-libcufile} \
 --disable-optimizations \
 --dynamic-libengines 

EXTFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" make V=1 %{?_smp_mflags}

%install
make install prefix=%{_prefix} mandir=%{_mandir} libdir=%{_libdir}/fio DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc README.rst REPORTING-BUGS HOWTO.rst examples
%doc MORAL-LICENSE GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_libdir}/fio/
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}/*

%if %{with pmem}
%files engine-dev-dax
%{_libdir}/fio/fio-dev-dax.so
%endif

%files engine-http
%{_libdir}/fio/fio-http.so

%files engine-libaio
%{_libdir}/fio/fio-libaio.so

%if %{with pmem}
%files engine-libpmem
%{_libdir}/fio/fio-libpmem.so
%endif

%if %{with nbd}
%files engine-nbd
%{_libdir}/fio/fio-nbd.so
%endif

%if %{with rados}
%files engine-rados
%{_libdir}/fio/fio-rados.so
%endif

%if %{with rbd}
%files engine-rbd
%{_libdir}/fio/fio-rbd.so
%endif

%if %{with xnvme}
%files engine-xnvme
%{_libdir}/fio/fio-xnvme.so
%endif

%ifnarch %{arm}
%files engine-rdma
%{_libdir}/fio/fio-rdma.so
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.40-3
- Prepare for Oreon 11 (RP1)
