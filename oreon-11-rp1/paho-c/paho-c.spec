%global source0_hash 8b960f51edc7e03507637d987882bc486d8f4be6e79431bf99e2763344fd14c5
Name:           paho-c
Version:        1.3.16
Release:        1%{?dist}
Summary:        MQTT C Client
License:        BSD-3-Clause AND EPL-2.0
URL:            https://eclipse.dev/paho/clients/c/
Source0:        https://github.com/eclipse/paho.mqtt.c/archive/v%{version}/paho.mqtt.c-%{version}.tar.gz
Source1:        unused.abignore
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
# /oreon:deps
%description
The Paho MQTT C Client is a fully fledged MQTT client written in C.

%package        devel
Summary:        MQTT C Client development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files and samples for the the Paho MQTT C Client.

%package        doc
Summary:        MQTT C Client development kit documentation
BuildArch:      noarch
%description    doc
Development documentation files for the the Paho MQTT C Client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir paho.mqtt.c-%{version}
%oreon_prep
%build

%cmake \
    -GNinja \
    -DPAHO_WITH_SSL=ON \
    -DPAHO_BUILD_DOCUMENTATION=ON \
    -DPAHO_BUILD_SAMPLES=ON \
    -DPAHO_ENABLE_CPACK=OFF
%cmake_build
%install
%cmake_install
install -pDm755 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/abi/paho-c.abignore
mkdir -p %{buildroot}%{_mandir}/man3
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man/man3/* %{buildroot}%{_mandir}/man3/
mv -fv %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man/man3/* %{buildroot}%{_mandir}/man3/
rm -rvf %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTAsync/man %{buildroot}%{_docdir}/Eclipse\ Paho\ C/doc/MQTTClient/man
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n paho-c-devel -f %{oreon_filedir}/paho-c-devel.list
%files -n paho-c-doc -f %{oreon_filedir}/paho-c-doc.list

%changelog

%autochangelog
