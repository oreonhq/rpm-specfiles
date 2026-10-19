%global source0_hash e668a3c4acd50c41dc204c8a6dd98a611e0f26af89cf677577fa9be8a2698003
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%ifarch aarch64 x86_64
%bcond_without ucx
%else
%bcond_with ucx
%endif
%ifarch %{arm}
%bcond_with rdma
%else
%bcond_without rdma
%endif
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%if 0%{?oreon} >= 11
%bcond_with orangefs
%bcond_with sphinx
%elif %{defined rhel}
%bcond_with orangefs
%bcond_with sphinx
%else
%bcond_without orangefs
%bcond_without sphinx
%endif
%ifarch x86_64
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%bcond_with psm2
%else
%bcond_without psm2
%endif
%else
%bcond_with psm2
%endif
%bcond_without pmix
%bcond autogen 0
Name:           openmpi%{?_cc_name_suffix}
Version:        5.0.11
Release:        1%{?dist}
Summary:        Open Message Passing Interface
License:        BSD-3-Clause-Open-MPI AND mpich2 AND BSD-3-Clause AND LicenseRef-Public-Domain AND BSD-4-Clause-UC
URL:            http://www.open-mpi.org/
ExcludeArch:    %{ix86}
Source0:        https://www.open-mpi.org/software/ompi/v5.0/downloads/openmpi-%{version}.tar.bz2
Source1:        openmpi.module.in
Source3:        openmpi.pth.py3
Source4:        macros.openmpi
%if %{with autogen}
%endif
%ifarch %{valgrind_arches}
%endif
%if %{with rdma}
%endif
%if %{with java}
%else
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      %{name}-java-devel < %{version}-%{release}
%endif
%if !0%{?el7}
%endif
%ifnarch s390x
%endif
%if %{with orangefs}
%endif
%if %{with pmix}
%endif
%if %{with psm2}
%endif
%if %{with ucx}
%endif
%if !0%{?el7}
%endif
%if %{with sphinx}
%endif
Provides:       mpi
%if 0%{?rhel} == 7 || (0%{?oreon} >= 11)
Requires:       environment-modules
%endif
Requires:       environment(modules)
Requires:       prrte
Requires:       openssh-clients
%global __provides_exclude_from %{_libdir}/openmpi/lib/(lib(mca|ompi|open-(pal|rte|trace))|openmpi/).*.so
%global __requires_exclude lib(mca|ompi|open-(pal|rte|trace)|vt).*
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hwloc-devel
BuildRequires:  hwloc-gui
BuildRequires:  java-25-devel
BuildRequires:  libevent-devel
BuildRequires:  libfabric-devel
BuildRequires:  make
BuildRequires:  opensm-devel
BuildRequires:  orangefs-devel
BuildRequires:  papi-devel
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pmix-devel
BuildRequires:  prrte
BuildRequires:  prrte-devel
BuildRequires:  python3-devel
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  rdma-core-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  zlib-devel
# /oreon:deps
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
%if !0%{?el7}
Requires:	rpm-mpi-hooks
Requires:	python(abi)
%endif
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

# We set this to for convenience, since this is the unique dir we use for this
# particular package, version, compiler
%global namearch openmpi-%{_arch}%{?_cc_name_suffix}

%package -n python%{python3_pkgversion}-openmpi
Summary:        OpenMPI support for Python 3
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi)
%description -n python%{python3_pkgversion}-openmpi
OpenMPI support for Python 3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%if !0%{?el7}
	--with-libevent=external \
%if %{with pmix}
	--with-pmix=external \
%endif
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

fail=1
make check || ( cat test/*/test-suite.log && exit $fail )
%files -f %{oreon_filedir}/main.list
%files -n openmpi-devel -f %{oreon_filedir}/openmpi-devel.list
%files -n openmpi-doc -f %{oreon_filedir}/openmpi-doc.list
%files -n openmpi-java -f %{oreon_filedir}/openmpi-java.list
%files -n openmpi-java-devel -f %{oreon_filedir}/openmpi-java-devel.list
%files -n python3-openmpi -f %{oreon_filedir}/python3-openmpi.list

%changelog

%autochangelog
