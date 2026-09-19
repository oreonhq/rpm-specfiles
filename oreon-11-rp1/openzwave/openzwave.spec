%global source0_hash none

Name:     openzwave
Version:  1.6.1914
Release:  12%{?dist}
Summary:  Sample Executables for OpenZWave
URL:      http://www.openzwave.net
License:  LGPL-3.0-or-later
Source0:  http://old.openzwave.com/downloads/openzwave-%{version}.tar.gz
#Source0:  https://github.com/OpenZWave/open-zwave/archive/%{commit0}.tar.gz#/%{name}-%{short0}.tar.gz

# New SwitchMultilevel command class support is broken so disable it
#Patch1:   openzwave-1.6-SwitchMultilevel.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: hidapi-devel
BuildRequires: systemd-devel
BuildRequires: tinyxml-devel

%description
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without
requiring any in depth knowledge of the Z-Wave protocol.

%package -n libopenzwave
Summary: Library to access Z-Wave interfaces

%description -n libopenzwave
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without
requiring any in depth knowledge of the Z-Wave protocol.

%package -n libopenzwave-devel
Summary: Open-ZWave header files
Requires: libopenzwave%{?_isa} = %{version}-%{release}

%description -n libopenzwave-devel
Header files needed when you want to compile your own
applications using openzwave

%package -n libopenzwave-devel-doc
Summary: Open-ZWave API documentation files
Requires: libopenzwave-devel%{?_isa} = %{version}-%{release}

%description -n libopenzwave-devel-doc
API documentation files needed when you want to compile your own
applications using openzwave

%prep
%setup -q -n %{name}-%{version}
#patch1 -p1 -b.switchmultilevel
# don't use projects compiler flags
sed -i 's/^RELEASE_CFLAGS.*/RELEASE_CFLAGS :=/' cpp/build/Makefile
sed -i 's/^RELEASE_CFLAGS.*/RELEASE_CFLAGS :=/' cpp/examples/MinOZW/Makefile

%build
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
CFLAGS="-fPIC -DNDEBUG -Wformat %{optflags} '-DSYSCONFDIR=\"%{_sysconfdir}/openzwave/\"' -DOPENZWAVE_ENABLE_EXCEPTIONS" \
LDFLAGS="%{__global_ldflags}" \
VERSION_MAJ=$major_ver \
VERSION_MIN=$minor_ver \
VERSION_REV=$revision \
PREFIX=/usr \
sysconfdir=%{_sysconfdir}/openzwave/ \
includedir=%{_includedir} \
docdir=%{_defaultdocdir}/openzwave-%{version} \
instlibdir=%{_libdir} \
USE_HID=1 \
USE_BI_TXML=0 \
make %{?_smp_mflags} SHELL='sh -x'

%install
rm -rf %{buildroot}/*
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_defaultdocdir}/openzwave-%{version}/
mkdir -p %{buildroot}/%{_sysconfdir}/
mkdir -p %{buildroot}/%{_includedir}/openzwave/
DESTDIR=%{buildroot} \
VERSION_MAJ=$major_ver \
VERSION_MIN=$minor_ver \
VERSION_REV=$revision \
PREFIX=/usr \
sysconfdir=%{_sysconfdir}/openzwave/ \
includedir=%{_includedir}/openzwave/ \
docdir=%{_defaultdocdir}/openzwave-%{version} \
instlibdir=%{_libdir} \
USE_HID=1 \
USE_BI_TXML=0 \
make install
rm %{buildroot}%{_defaultdocdir}/openzwave-%{version}/Doxyfile.in
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/html/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/default.htm
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/general/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/images+css/
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/api/
# Upstream does not use it anymore
# https://github.com/OpenZWave/open-zwave/commit/d62a9fd09b14303bf27323758f4a7bf9dcf14455
rm -f %{buildroot}%{_defaultdocdir}/openzwave-%{version}/ChangeLog.old

%files
%{_bindir}/MinOZW

%files -n libopenzwave
%license licenses/*.txt
%doc docs/default.htm docs/general/ docs/images+css/
%{_libdir}/libopenzwave.so.*
%dir %{_sysconfdir}/openzwave/
%config(noreplace) %{_sysconfdir}/openzwave/*

%files -n libopenzwave-devel
%{_bindir}/ozw_config
%{_includedir}/openzwave/
%{_libdir}/libopenzwave.so
%{_libdir}/pkgconfig/libopenzwave.pc

%files -n libopenzwave-devel-doc
%doc docs/api/

%ldconfig_scriptlets -n libopenzwave

%changelog
%autochangelog
