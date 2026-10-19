%global source0_hash be562ed2963cdbd1cccc1541e3a9f4ec08a8c31ab727d07e9cb058bd787be685
%bcond asan 0
%bcond breakpad 0
%bcond x11 %[%{undefined rhel}]
%global commit dacfa9de829ac7cb173825f593236bf2c21f637e
%global commitdate 20260209
%global shortcommit %{sub %{commit} 1 7}
%global tarversion %{?commit:%{commit}}%{!?commit:v%{version}}
%global tarext tar.gz
%global tarbasename %{name}-%{?commit:%{shortcommit}}%{!?commit:%{version}}
Name:               quickshell
Version:            0.2.1%{?commit:^git%{commitdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Flexible QtQuick based desktop shell toolkit
License:            LGPL-3.0-or-later and BSD-3-Clause and HPND-sell-variant
URL:                https://quickshell.org/
Source0:        https://git.outfoxxed.me/%{name}/%{name}/archive/%{commit}.%{tarext}#/%{name}-dacfa9d.%{tarext}
Requires:           (qt6-qtwayland%{?_isa} if qt6-qtbase%{?_isa} < 6.10)
Requires:           qt6-qtsvg%{?_isa}
%if %{with asan}
%endif
%if %{with breakpad}
%endif
Provides:           desktop-notification-daemon = %{version}-%{release}
Provides:           PolicyKit-authentication-agent = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  spirv-tools
# /oreon:deps
%description
Quickshell is a toolkit for building status bars, widgets,
lockscreens, and other desktop components using QtQuick.

It can be used alongside a Wayland compositor to build
a complete desktop environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
%cmake  -GNinja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DDISTRIBUTOR="%{vendor}" \
        -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml \
        -DASAN=%{?with_asan:ON}%{!?with_asan:OFF} \
        -DCRASH_REPORTER=%{?with_breakpad:ON}%{!?with_breakpad:OFF} \
        -DX11=%{?with_x11:ON}%{!?with_x11:OFF} \
        %{?commit:-DGIT_REVISION=%{commit}} \
        %{nil}

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
