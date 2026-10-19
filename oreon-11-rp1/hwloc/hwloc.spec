%global source0_hash 0084b926fff9a960ddbf175654db39054ed60afbb830d2039d8a60686ca06a7f
Summary:        Portable Hardware Locality - portable abstraction of hierarchical architectures
Name:      hwloc
Version:   2.15.0
Release:        1%{?dist}
License:   BSD-2-Clause
URL:       http://www.open-mpi.org/projects/hwloc/
Source0:        https://download.open-mpi.org/release/%{name}/v2.15/%{name}-%{version}.tar.bz2
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%if %{undefined rhel} || (0%{?oreon} >= 11)
%ifarch x86_64
%endif
%endif
%ifarch %{ix86} x86_64
%{?systemd_requires}
%endif
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libxml2-devel
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  rdma-core-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
The Portable Hardware Locality (hwloc) software package provides
a portable abstraction (across OS, versions, architectures, ...)
of the hierarchical topology of modern architectures, including
NUMA memory nodes,  shared caches, processor sockets, processor cores
and processing units (logical processors or "threads"). It also gathers
various system attributes such as cache and memory information. It primarily
aims at helping applications with gathering information about modern
computing hardware so as to exploit it accordingly and efficiently.

hwloc may display the topology in multiple convenient formats.
It also offers a powerful programming interface (C API) to gather information
about the hardware, bind processes, and much more.

%package devel
Summary:   Headers and shared development libraries for hwloc
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%ifnarch %{arm}
Requires:  rdma-core-devel%{?_isa}
%endif
%description devel
Headers and shared object symbolic links for the hwloc.

%package libs
Summary:   Run time libraries for the hwloc
%description libs
Run time libraries for the hwloc

%package gui
Summary:   The gui-based hwloc program(s)
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%description gui
GUI-based tool for displaying system topology information.

%package plugins
Summary:   Plugins for hwloc
Requires:  %{name}-plugins%{?_isa} = %{version}-%{release}
%description plugins
 This package contains plugins for hwloc. This includes
  - PCI support
  - GL support
  - libxml support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-plugins --disable-silent-rules --runstatedir=/run
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
cp -p AUTHORS COPYING NEWS README VERSION %{buildroot}%{_pkgdocdir}
cp -pr doc/examples %{buildroot}%{_pkgdocdir}
mv  %{buildroot}%{_pkgdocdir}/examples/Makefile  %{buildroot}%{_pkgdocdir}/examples/Makefile_%{_arch}
desktop-file-validate %{buildroot}/%{_datadir}/applications/lstopo.desktop
rm %{buildroot}%{_mandir}/man1/lstopo.1
ln %{buildroot}%{_mandir}/man1/lstopo-no-graphics.1 %{buildroot}%{_mandir}/man1/lstopo.1
%ifarch %{ix86} x86_64
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_datadir}/%{name}/hwloc-dump-hwdata.service %{buildroot}%{_unitdir}/
%else
rm %{buildroot}%{_datadir}/%{name}/hwloc-dump-hwdata.service
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

LD_LIBRARY_PATH=$PWD/hwloc/.libs make check
%ifarch %{ix86} x86_64
%post

%systemd_post hwloc-dump-hwdata.service
%preun

%systemd_preun hwloc-dump-hwdata.service
%postun

%systemd_postun_with_restart hwloc-dump-hwdata.service
%endif
%files -f %{oreon_filedir}/main.list
%files -n hwloc-devel -f %{oreon_filedir}/hwloc-devel.list
%files -n hwloc-libs -f %{oreon_filedir}/hwloc-libs.list
%files -n hwloc-gui -f %{oreon_filedir}/hwloc-gui.list
%files -n hwloc-plugins -f %{oreon_filedir}/hwloc-plugins.list

%changelog

%autochangelog
