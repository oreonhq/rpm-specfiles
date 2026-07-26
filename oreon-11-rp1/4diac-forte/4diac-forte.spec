%global source0_hash b6edbf0217844f3f11230b6c360a406936aed4fd54c5b007ff680c16b5ef6f9c

# Force out of source build
%undefine __cmake_in_source_build

%global with_sysfs 1
%global with_opcua 0
%global with_paho 1
%global with_modbus 1

# LuaJIT is only available on i686, x86_64, and aarch64
%ifarch i686 x86_64 aarch64
%global with_lua 0
%global with_luajit 1
%else
%global with_lua 1
%global with_luajit 0
%endif

Name:     4diac-forte
Version:  2.0.1
Release:  14%{?dist}
Summary:  IEC 61499 runtime environment
License:  EPL-2.0
URL:      http://eclipse.org/4diac
Source0:  https://git.eclipse.org/c/4diac/org.eclipse.4diac.forte.git/snapshot/org.eclipse.4diac.forte-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: systemd
%{?systemd_requires}

%if 0%{?with_opcua}
BuildRequires: open62541-devel >= 1.0
%endif

%if 0%{?with_lua}
BuildRequires: lua-devel >= 5.1
%endif

%if 0%{?with_luajit}
BuildRequires: luajit-devel >= 2.1.0
%endif

%if 0%{?with_paho}
BuildRequires: paho-c-devel >= 1.3.9
%endif

%if 0%{?with_modbus}
BuildRequires: libmodbus-devel >= 3.1.6
%endif

%description
The 4DIAC runtime environment (4DIAC-RTE, FORTE) is a small portable
implementation of an IEC 61499 runtime environment targeting small
embedded control devices (16/32 Bit), implemented in C++. It supports
online-reconfiguration of its applications and the real-time capable
execution of all function block types provided by the IEC 61499 standard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n org.eclipse.4diac.forte-%{version}

%build
%cmake -DFORTE_ARCHITECTURE=Posix \
       -DFORTE_COM_ETH=ON \
       -DFORTE_COM_FBDK=ON \
       -DFORTE_COM_LOCAL=ON \
%if 0%{?with_paho}
       -DFORTE_COM_PAHOMQTT=ON \
%endif
%if 0%{?with_modbus}
       -DFORTE_COM_MODBUS=ON \
%endif
%if 0%{?with_opcua}
       -DFORTE_COM_OPC_UA=ON -DFORTE_COM_OPC_UA_INCLUDE_DIR=%{_includedir} -DFORTE_COM_OPC_UA_LIB_DIR=%{_libdir} -DFORTE_COM_OPC_UA_LIB=libopen62541.so -DFORTE_COM_OPC_UA_MASTER_BRANCH=ON \
%endif
       -DFORTE_MODULE_CONVERT=ON \
       -DFORTE_MODULE_IEC61131=ON \
%if 0%{?with_sysfs}
       -DFORTE_MODULE_SysFs=ON \
%endif
       -DFORTE_MODULE_UTILS=ON \
       -DFORTE_MODULE_IEC61131=ON \
%if 0%{?with_lua}
       -DFORTE_USE_LUATYPES=Lua \
%endif
%if 0%{?with_luajit}
       -DFORTE_USE_LUATYPES=LuaJIT -DLUAJIT_INCLUDE_DIR=%{_includedir}/luajit-2.1 -DLUAJIT_LIBRARY=%{_libdir}/libluajit-5.1.so \
%endif
       -DFORTE_TESTS=OFF

%cmake_build

%install
mkdir -p %{buildroot}%{_unitdir}
install -p systemd/4diac-forte.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p systemd/4diac-forte-sysconfig %{buildroot}%{_sysconfdir}/sysconfig/4diac-forte

%cmake_install

%post
%systemd_post 4diac-forte.service

%preun
%systemd_preun 4diac-forte.service

%postun
%systemd_postun_with_restart 4diac-forte.service

%files
%license epl-2.0.html
%{_bindir}/forte
%{_unitdir}/4diac-forte.service
%config(noreplace) %{_sysconfdir}/sysconfig/4diac-forte

%changelog
%autochangelog
