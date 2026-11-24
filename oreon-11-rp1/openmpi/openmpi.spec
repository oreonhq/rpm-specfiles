# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e668a3c4acd50c41dc204c8a6dd98a611e0f26af89cf677577fa9be8a2698003
%global source1_hash c6b9d0d95967f4dba6613c14ec03a01f19d93e23f44906fc3cb8276ce737f114
%global source3_hash 2acaeda51628ea81b01876497dc4c84fe056317391262cab92e9dd40b0721e74
%global source4_hash b21c8d8819ed6cb4d69ad0b8054bc6e60fbab93eee6347f259ddc9229fa53f2a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%ifarch aarch64 x86_64
%bcond_without ucx
%else
%bcond_with ucx
%endif

%bcond_without rdma

%if 0%{?oreon}
%bcond_with java
%else
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%endif

%if 0%{?rhel}
%bcond_with orangefs
%bcond_with sphinx
%else
%if 0%{?oreon}
%bcond_without orangefs
%bcond_with sphinx
%else
%bcond_without orangefs
%bcond_without sphinx
%endif
%endif

%ifarch x86_64
%if 0%{?rhel} >= 10
%bcond_with psm2
%else
%bcond_without psm2
%endif
%else
%bcond_with psm2
%endif

%bcond_without pmix

%bcond autogen 1

Name:           openmpi%{?_cc_name_suffix}
Version:        5.0.11
Release:        %{autorelease}
Summary:        Open Message Passing Interface
License:        BSD-3-Clause-Open-MPI AND mpich2 AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain AND BSD-4-Clause-UC
URL:            http://www.open-mpi.org/
ExcludeArch:    %{ix86}

Source0:        https://www.open-mpi.org/software/ompi/v5.0/downloads/openmpi-%{version}.tar.bz2
Source1:        openmpi.module.in
Source3:        openmpi.pth.py3
Source4:        macros.openmpi
Patch:          openmpi-drop-recommonmark.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
%if %{with autogen}
BuildRequires:  libtool
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
%endif
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
%if %{with rdma}
BuildRequires:  rdma-core-devel
%endif
BuildRequires:  hwloc-devel
%if %{with java}
BuildRequires:  java-25-devel
%else
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      %{name}-java-devel < %{version}-%{release}
%endif
BuildRequires:  libevent-devel
BuildRequires:  libfabric-devel
%ifnarch s390x
BuildRequires:  papi-devel
%endif
%if %{with orangefs}
BuildRequires:  orangefs-devel
%endif
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
%if %{with pmix}
BuildRequires:  pmix-devel >= 4.2.7
%endif
BuildRequires:  prrte-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with psm2}
BuildRequires:  libpsm2-devel
%endif
%if %{with ucx}
BuildRequires:  ucx-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  rpm-mpi-hooks
%if %{with sphinx}
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  python3-sphinx_rtd_theme
%endif

Provides:       mpi
Requires:       environment(modules)
Requires:       prrte
Requires:       openssh-clients

%global __provides_exclude_from %{_libdir}/openmpi/lib/(lib(mca|ompi|open-(pal|rte|trace))|openmpi/).*.so
%global __requires_exclude lib(mca|ompi|open-(pal|rte|trace)|vt).*

%description
Open MPI is an open source, freely available implementation of both the
MPI-1 and MPI-2 standards, combining technologies and resources from
several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in
order to build the best MPI library available.  A completely new MPI-2
compliant implementation, Open MPI offers advantages for system and
software vendors, application developers, and computer science
researchers. For more information, see http://www.open-mpi.org/ .

%package devel
Summary:	Development files for openmpi
Requires:	%{name} = %{version}-%{release}, gcc-gfortran
Provides:	mpi-devel
Requires:	rpm-mpi-hooks
Requires:	(python(abi) = %{python3_version} if python3)

%description devel
Contains development headers and libraries for openmpi.

%package doc
Summary:        HTML documentation for openmpi
License:        BSD-3-Clause AND BSD-3-Clause-Open-MPI AND mpich2 AND MIT AND (MIT OR GPL-2.0-or-later) AND (OFL-1.1 AND MIT)
BuildArch:      noarch

%description doc
HTML documentation for openmpi.

%if %{with java}
%package java
Summary:        Java library
License:        Apache-2.0
Requires:       %{name} = %{version}-%{release}
Requires:       java-25-headless

%description java
Java library.

%package java-devel
Summary:        Java development files for openmpi
License:        Apache-2.0
Requires:       %{name}-java = %{version}-%{release}
Requires:       java-25-devel

%description java-devel
Contains development wrapper for compiling Java with openmpi.
%endif

%global namearch openmpi-%{_arch}%{?_cc_name_suffix}

%package -n python%{python3_pkgversion}-openmpi
Summary:        OpenMPI support for Python 3
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi) = %{python3_version}

%description -n python%{python3_pkgversion}-openmpi
OpenMPI support for Python 3.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
%autosetup -p1 -n %{name}-%{version}
%if %{with autogen}
./autogen.pl --force
%endif

%build
%set_build_flags
./configure --prefix=%{_libdir}/%{name} \
	--mandir=%{_mandir}/%{namearch} \
	--includedir=%{_includedir}/%{namearch} \
	--sysconfdir=%{_sysconfdir}/%{namearch} \
	--disable-silent-rules \
	--enable-builtin-atomics \
	--enable-ipv6 \
%if %{with java}
	--enable-mpi-java \
%endif
	--enable-mpi1-compatibility \
%if %{with sphinx}
	--enable-sphinx \
%endif
	--with-prrte=external \
	--with-sge \
%ifarch %{valgrind_arches}
	--with-valgrind \
	--enable-memchecker \
%endif
	--with-hwloc=/usr \
	--with-libevent=external \
%if %{with pmix}
	--with-pmix=external \
%endif

%make_build V=1

%install
%make_install
find %{buildroot}%{_libdir}/%{name}/lib -name \*.la | xargs rm
find %{buildroot}%{_mandir}/%{namearch} -type f | xargs gzip -9

mkdir -p %{buildroot}%{_datadir}/modulefiles/mpi
sed 's#@LIBDIR@#%{_libdir}/%{name}#;
     s#@ETCDIR@#%{_sysconfdir}/%{namearch}#;
     s#@FMODDIR@#%{_fmoddir}/%{name}#;
     s#@INCDIR@#%{_includedir}/%{namearch}#;
     s#@MANDIR@#%{_mandir}/%{namearch}#;
     s#@PY3SITEARCH@#%{python3_sitearch}/%{name}#;
     s#@COMPILER@#openmpi-%{_arch}%{?_cc_name_suffix}#;
     s#@SUFFIX@#%{?_cc_name_suffix}_openmpi#' \
     <%{SOURCE1} \
     >%{buildroot}%{_datadir}/modulefiles/mpi/%{namearch}

install -Dpm 644 %{SOURCE4} %{buildroot}/%{macrosdir}/macros.%{namearch}

mkdir -p %{buildroot}%{_fmoddir}/%{name}
for mod in %{buildroot}%{_libdir}/%{name}/lib/*.mod
do
  modname=$(basename $mod)
  ln -s ../../../%{name}/lib/${modname} %{buildroot}/%{_fmoddir}/%{name}/
done

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cd %{buildroot}%{_libdir}/pkgconfig
ln -s ../%{name}/lib/pkgconfig/*.pc .
cd -

mkdir -p %{buildroot}%{_libdir}/%{name}/lib/cmake/

mkdir -p %{buildroot}%{_libdir}/%{name}/lib/openmpi/cmake
mkdir -p %{buildroot}%{_libdir}/%{name}/include

sed -i -e s/-ldl// -e s/-lhwloc// \
  %{buildroot}%{_libdir}/%{name}/share/openmpi/*-wrapper-data.txt

mkdir -p %{buildroot}/%{python3_sitearch}/%{name}
install -pDm0644 %{SOURCE3} %{buildroot}/%{python3_sitearch}/openmpi.pth

%check
fail=1
make check || ( cat test/*/test-suite.log && exit $fail )

%files
%license LICENSE
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{namearch}
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/lib
%dir %{_libdir}/%{name}/lib/openmpi
%dir %{_libdir}/%{name}/include
%dir %{_mandir}/%{namearch}
%dir %{_mandir}/%{namearch}/man*
%config(noreplace) %{_sysconfdir}/%{namearch}/*
%{_libdir}/%{name}/bin/mpi[er]*
%{_libdir}/%{name}/bin/ompi*
%if %{with ucx}
%{_libdir}/%{name}/bin/oshmem_info
%endif
%{_libdir}/%{name}/bin/oshrun
%if %{without pmix}
%{_libdir}/%{name}/bin/pattrs
%{_libdir}/%{name}/bin/pctrl
%{_libdir}/%{name}/bin/pevent
%{_libdir}/%{name}/bin/plookup
%{_libdir}/%{name}/bin/pmix_info
%{_libdir}/%{name}/bin/pmixcc
%{_libdir}/%{name}/bin/pps
%{_libdir}/%{name}/bin/pquery
%{_libdir}/%{name}/lib/libpmix.so.2*
%{_libdir}/%{name}/lib/pmix/
%{_libdir}/%{name}/share/pmix/
%{_mandir}/%{namearch}/man1/pmix_info.1*
%{_mandir}/%{namearch}/man5/openpmix.5*
%endif
%{_mandir}/%{namearch}/man7/Open-MPI.7*
%{_libdir}/%{name}/lib/*.so.40*
%{_libdir}/%{name}/lib/*.so.80*
%{_mandir}/%{namearch}/man1/mpirun.1*
%{_mandir}/%{namearch}/man1/mpisync.1*
%{_mandir}/%{namearch}/man1/ompi*
%if %{with ucx}
%{_mandir}/%{namearch}/man1/oshmem_info*
%endif
%{_libdir}/%{name}/lib/openmpi/*
%{_datadir}/modulefiles/mpi/
%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/openmpi
%{_libdir}/%{name}/share/openmpi/amca-param-sets
%{_libdir}/%{name}/share/openmpi/help*.txt

%files devel
%dir %{_includedir}/%{namearch}
%{_libdir}/%{name}/bin/mpi[cCf]*
%{_libdir}/%{name}/bin/opal_*
%if %{with ucx}
%{_libdir}/%{name}/bin/osh[cCf]*
%endif
%if %{with ucx}
%{_libdir}/%{name}/bin/shmem[cCf]*
%endif
%{_includedir}/%{namearch}/*
%{_fmoddir}/%{name}/
%{_libdir}/%{name}/lib/*.so
%{_libdir}/%{name}/lib/*.mod
%{_libdir}/%{name}/lib/cmake/
%{_libdir}/%{name}/lib/pkgconfig/
%{_libdir}/pkgconfig/*.pc
%{_mandir}/%{namearch}/man1/mpi[cCf]*
%if %{with ucx}
%{_mandir}/%{namearch}/man1/osh[cCf]*
%{_mandir}/%{namearch}/man1/oshmem-wrapper-compiler.1*
%{_mandir}/%{namearch}/man1/shmem[cCf]*
%endif
%{_mandir}/%{namearch}/man1/opal_*
%{_mandir}/%{namearch}/man3/*
%{_libdir}/%{name}/share/openmpi/openmpi-valgrind.supp
%{_libdir}/%{name}/share/openmpi/*-wrapper-data.txt
%{macrosdir}/macros.%{namearch}

%files doc
%license LICENSE
%doc %{_libdir}/%{name}/share/doc/
%exclude %{_libdir}/%{name}/share/doc/openmpi/javadoc-openmpi

%if %{with java}
%files java
%{_libdir}/%{name}/lib/mpi.jar

%files java-devel
%{_libdir}/%{name}/bin/mpijavac
%{_libdir}/%{name}/bin/mpijavac.pl
%doc %{_libdir}/%{name}/share/doc/openmpi/javadoc-openmpi
%{_mandir}/%{namearch}/man1/mpijavac.1.gz
%endif

%files -n python%{python3_pkgversion}-openmpi
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/openmpi.pth

%changelog
%autochangelog
