%global source0_hash 20e998aae86d1629e787a924c044bb912d21ac8f5d1c1b707f2af06eb4c6016d

%global with_tests 0

Name:           mosquitto
Version:        2.1.2
Release:        1%{?dist}
Summary:        Open Source MQTT v5/v3.1.x Broker

License:        EPL-2.0
URL:            https://mosquitto.org/
Source0:        https://mosquitto.org/files/source/%{name}-%{version}.tar.gz
Source1:        mosquitto-sysusers.conf
Patch:          mosquitto-fix-service.patch

BuildRequires:  asciidoc
BuildRequires:  c-ares-devel
BuildRequires:  cjson-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libargon2-devel
BuildRequires:  libedit-devel
BuildRequires:  libuuid-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  libxslt
BuildRequires:  openssl-devel
%if 0%{?fedora}
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
%if 0%{?with_tests}
BuildRequires:  CUnit-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  python3-psutil
BuildRequires:  uthash-devel
%endif
#BuildRequires:  uthash-devel
Provides: bundled(uthash)

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Mosquitto is an open source message broker that implements the MQ Telemetry
Transport protocol version v5 and 3.1.x. MQTT provides a lightweight method
of carrying out messaging using a publish/subscribe model. This makes it
suitable for "machine to machine" messaging such as with low power sensors 
or mobile devices such as phones, embedded computers or micro-controllers 
like the Arduino.

%package devel
Requires:     %{name}%{?_isa} = %{version}-%{release}
Summary:      Development files for %{name}

%description devel
Development headers and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Don't strip binaries on install: rpmbuild will take care of it
sed -i "s|(INSTALL) -s|(INSTALL)|g" lib/Makefile src/Makefile client/Makefile
# Search for the correct websockets library name
sed -i "s/websockets_shared/websockets/" src/CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
       -DWITH_WEBSOCKETS=ON \
       -DWITH_SYSTEMD=ON \
       -DWITH_SRV=ON \
       -DWITH_TLS=ON \
%if 0%{?with_tests}
       -DWITH_TESTS=ON \
%else
       -DWITH_TESTS=OFF \
%endif
       %nil

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 service/systemd/%{name}.service.notify %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_var}/log/%{name}
mkdir -p %{buildroot}%{_rundir}/%{name}

%if 0%{?with_tests}
%check
make test
%endif

%files
%license LICENSE.txt 
%doc ChangeLog.txt CONTRIBUTING.md README.md
%dir %attr(750,mosquitto,mosquitto) %{_sysconfdir}/%{name}
%dir %attr(750,mosquitto,mosquitto) %{_localstatedir}/log/%{name}
%dir %attr(750,mosquitto,mosquitto) %{_rundir}/%{name}
%ghost %config(noreplace) %attr(640,mosquitto,mosquitto) %{_sysconfdir}/%{name}/%{name}.conf
%config %attr(640,mosquitto,mosquitto) %{_sysconfdir}/%{name}/*.example
%{_bindir}/%{name}*
%if 0%{?rhel}
%{_sbindir}/%{name}
%endif
%{_libdir}/libmosquitto*.so.1
%{_libdir}/libmosquitto*.so.%{version}
%{_libdir}/mosquitto_*.so
%{_sysusersdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_mandir}/man*/%{name}*
%{_mandir}/man7/mqtt.7.*

%files devel
%{_includedir}/mosquitto/
%{_includedir}/mosquitto*.h
%{_includedir}/mqtt*.h
%{_libdir}/libmosquitto*.so
%{_libdir}/pkgconfig/libmosquitto*.pc
%{_mandir}/man3/libmosquitto.3.*

%changelog
%autochangelog
