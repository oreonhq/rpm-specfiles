%global source0_hash 23698ce31aae71e6f4c5a2a463709a0333ac4b94fc2933edc61f433aaf427ae9
%global docs 1
Name: dlt-daemon
Version: 2.18.11
Release:        1%{?dist}
Summary:        DLT - Diagnostic Log and Trace
Group: System Environment/Base
License: MPL-2.0
URL: https://github.com/COVESA/dlt-daemon
Source0:        https://github.com/COVESA/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: dlt-daemon-config.patch
Patch1: dlt-daemon-cmake.patch
%if 0%{?docs}
%endif
Requires(pre): shadow-utils
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pandoc
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
mkdir -p $RPM_BUILD_ROOT/var/lib/dlt-daemon
%ldconfig_scriptlets -n dlt-libs
%oreon_autofiles dlt-libs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dlt-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dlt-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dlt-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dlt-libs-devel -f %{oreon_filedir}/dlt-libs-devel.list
%files -n dlt-libs -f %{oreon_filedir}/dlt-libs.list
%files -n dlt-tools -f %{oreon_filedir}/dlt-tools.list
%files -n dlt-examples -f %{oreon_filedir}/dlt-examples.list

%changelog

%autochangelog
