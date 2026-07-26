%global source0_hash 504724b69755667512e7830320ff28a1dab3fd36715598ba2d2749ad052632de

%if (0%{?rhel} == 10)
%global docs 0
%else
%global docs 1
%endif

Name: dlt-daemon
Version: 2.18.10
Release: 8%{?dist}
Summary: DLT - Diagnostic Log and Trace
Group: System Environment/Base
License: MPL-2.0
URL: https://github.com/COVESA/dlt-daemon
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: dlt-daemon-config.patch
Patch1: dlt-daemon-cmake.patch

BuildRequires: cmake
%if 0%{?docs}
BuildRequires: pandoc
%endif

BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: gcc-c++
%if ((0%{?fedora} >= 38) || (0%{?rhel} >= 10))
BuildRequires: zlib-ng-compat-devel
%else
BuildRequires: zlib-devel
%endif

Requires(pre): shadow-utils

%description
This component provides a standardised log and trace interface, based on the
standardised protocol specified in the AUTOSAR standard 4.0 DLT.
This component can be used by GENIVI components and other applications as
logging facility providing
- the DLT shared library
- the DLT daemon, including startup scripts
- the DLT daemon adaptors
- the DLT client console utilities
- the DLT test applications

%package -n dlt-libs-devel
Summary:        DLT - Diagnostic Log and Trace: Development files
Requires:       dlt-libs = %{version}-%{release}
%description -n dlt-libs-devel
%{summary}.

%package -n dlt-libs
Summary:        DLT - Diagnostic Log and Trace: Libraries
%description -n dlt-libs
%{summary}.

%package -n dlt-tools
Summary:        DLT - Diagnostic Log and Trace: Tools
Recommends:     %{name} = %{version}-%{release}
%description -n dlt-tools
%{summary}.

%package -n dlt-examples
Summary:        DLT - Diagnostic Log and Trace: Examples
Requires:       %{name} = %{version}-%{release}
%description -n dlt-examples
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Create a sysusers.d config file
cat >dlt-daemon.sysusers.conf <<EOF
u dlt-daemon - 'User for dlt-daemon' /var/lib/dlt-daemon -
EOF

%build
mkdir -p build
cd build
%cmake .. -Wno-dev \
        -DDLT_USER=dlt-daemon \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DWITH_DLT_USE_IPv6=OFF \
        -DDLT_IPC=UNIX_SOCKET \
%if 0%{?docs}
        -DWITH_MAN=ON \
%endif
        -DWITH_SYSTEMD=ON \
        -DWITH_SYSTEMD_WATCHDOG=ON \
        -DWITH_SYSTEMD_JOURNAL=ON \
        -DWITH_DLT_ADAPTOR=ON \
        -DWITH_DLT_SYSTEM=ON \
        -DDLT_USER_IPC_PATH=/run/dlt
%cmake_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0644 -D dlt-daemon.sysusers.conf %{buildroot}%{_sysusersdir}/dlt-daemon.conf
cd build
%cmake_install

# Home directory for the 'dlt-daemon' user
mkdir -p $RPM_BUILD_ROOT/var/lib/dlt-daemon

%ldconfig_scriptlets -n dlt-libs

%files
%license LICENSE
%doc AUTHORS README.md ReleaseNotes.md
%attr(755,dlt-daemon,dlt-daemon) %dir /var/lib/dlt-daemon
%config(noreplace) %{_sysconfdir}/dlt.conf
%config(noreplace) %{_sysconfdir}/dlt_gateway.conf
%{_unitdir}/dlt.service
%attr(0755,root,root)
%{_bindir}/dlt-daemon
%if 0%{?docs}
%{_mandir}/man1/dlt-daemon.1*
%{_mandir}/man5/dlt.conf.5*
%{_mandir}/man5/dlt_gateway.conf.5*
%endif
%{_sysusersdir}/dlt-daemon.conf

%files -n dlt-examples
# The binaries do not have man pages but do have markdown documents.
%doc doc/dlt-qnx-system.md doc/dlt_build_options.md doc/dlt_cdh.md doc/dlt_demo_setup.md doc/dlt_design_specification.md doc/dlt_example_user.md doc/dlt_extended_network_trace.md doc/dlt_filetransfer.md doc/dlt_for_developers.md doc/dlt_glossary.md doc/dlt_kpi.md doc/dlt_multinode.md doc/dlt_offline_logstorage.md
%{_bindir}/dlt-example-filetransfer
%{_bindir}/dlt-example-user
%{_bindir}/dlt-example-user-common-api
%{_bindir}/dlt-example-user-func
%{_bindir}/dlt-test-client
%{_bindir}/dlt-test-filetransfer
%{_bindir}/dlt-test-fork-handler
%{_bindir}/dlt-test-init-free
%{_bindir}/dlt-test-multi-process
%{_bindir}/dlt-test-multi-process-client
%{_bindir}/dlt-test-non-verbose
%{_bindir}/dlt-test-preregister-context
%{_bindir}/dlt-test-stress
%{_bindir}/dlt-test-stress-client
%{_bindir}/dlt-test-stress-user
%{_bindir}/dlt-test-user
%{_datadir}/dlt-filetransfer/dlt-test-filetransfer-file
%{_datadir}/dlt-filetransfer/dlt-test-filetransfer-image.png
%{_unitdir}/dlt-example-user.service

%files -n dlt-tools
%{_bindir}/dlt-adaptor-stdin
%{_bindir}/dlt-adaptor-udp
%{_bindir}/dlt-control
%{_bindir}/dlt-convert
%{_bindir}/dlt-logstorage-ctrl
%{_bindir}/dlt-passive-node-ctrl
%{_bindir}/dlt-receive
%{_bindir}/dlt-sortbytimestamp
%{_bindir}/dlt-system
%config(noreplace) %{_sysconfdir}/dlt-system.conf
%{_unitdir}/dlt-receive.service
%{_unitdir}/dlt-system.service
%{_unitdir}/dlt-adaptor-udp.service
%if 0%{?docs}
%{_mandir}/man1/dlt-adaptor-stdin.1*
%{_mandir}/man1/dlt-adaptor-udp.1*
%{_mandir}/man1/dlt-control.1*
%{_mandir}/man1/dlt-convert.1*
%{_mandir}/man1/dlt-logstorage-ctrl.1*
%{_mandir}/man1/dlt-passive-node-ctrl.1*
%{_mandir}/man1/dlt-receive.1*
%{_mandir}/man1/dlt-sortbytimestamp.1*
%{_mandir}/man1/dlt-system.1*
%{_mandir}/man5/dlt-system.conf.5*
%endif

%files -n dlt-libs
%{_libdir}/libdlt.so.*

%files -n dlt-libs-devel
%{_includedir}/dlt/*.h
%{_libdir}/pkgconfig/automotive-dlt.pc
%{_libdir}/libdlt.so
%{_libdir}/cmake/automotive-dlt/*.cmake

%changelog
%autochangelog
