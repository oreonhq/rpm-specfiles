%global source0_hash d52a0afa614ad6c088cc9ddff1ae7d29c8c595ac5fdd321170a05f41e634bd1a
%undefine __cmake_in_source_build
%global __cmake_builddir build
%filter_provides_in %{python3_sitearch}/.*\.so$
Summary:        Library and tool to control NAT in UPnP-enabled routers
Name:       miniupnpc
Version:    2.3.3
Release:        1%{?dist}
License:    LicenseRef-Callaway-BSD
URL:        http://miniupnp.free.fr/
Source0:        http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-miniupnpc = %{version}-%{release}
# /oreon:deps
%description
miniupnpc is an implementation of a UPnP client library, enabling applications
to access the services provided by an UPnP "Internet Gateway Device" present on
the network. In UPnP terminology, it is a UPnP Control Point.

This package includes upnpc, a UPnP client application for configuring  port
forwarding in UPnP enabled routers.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and development documentation for
%{name}.

%package -n python3-%{name}
Summary:    Python3 interface to %{name}
%description -n python3-%{name}
This package contains python3 interfaces to %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p2

# Use already built shared object for Python module
# Unversioned link is not enough to avoid a rebuild
sed -i -e 's|build/libminiupnpc.a|build/libminiupnpc.so.%{version}|g' setup.py

%build

%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DNO_GETADDRINFO=FALSE \
    -DUPNPC_BUILD_SAMPLE=TRUE \
    -DUPNPC_BUILD_SHARED=TRUE \
    -DUPNPC_BUILD_STATIC=FALSE \
    -DUPNPC_BUILD_TESTS=TRUE \
    -DUPNPC_NO_INSTALL=FALSE
%cmake_build
%pyproject_wheel
%install
%cmake_install
%pyproject_install
mv %{buildroot}%{_bindir}/upnpc-shared %{buildroot}%{_bindir}/upnpc
mv %{buildroot}%{_bindir}/upnp-listdevices-shared %{buildroot}%{_bindir}/upnp-listdevices
rm -f %{buildroot}%{_bindir}/external-ip.sh
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/miniupnpc* usr/lib64/python3*/site-packages/miniupnpc* usr/bin/*

%check

make CFLAGS="%{optflags} -DMINIUPNPC_SET_SOCKET_TIMEOUT" check
%files
%files -n miniupnpc-devel -f %{oreon_filedir}/miniupnpc-devel.list
%files -n python3-miniupnpc -f %{oreon_filedir}/python3-miniupnpc.list

%changelog

%autochangelog
