%global source0_hash f895de2683627e969e4849dbfbbb2b500787481ca5ba0de6d6dfdae5f1549abf
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]
Name:           sddm
Version:        0.21.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        QML based desktop and login manager
URL:            https://github.com/sddm/sddm
Source0:        https://github.com/sddm/sddm/archive/refs/tags/v0.21.0.tar.gz#/sddm-0.21.0.tar.gz
Patch0:         https://github.com/sddm/sddm/commit/228778c2b4b7e26db1e1d69fe484ed75c5791c3a.patch
Patch1:         sddm-PR1876.patch
Patch2:         sddm-0.21.0-fix-restart-greeter-when-helper-is-in-a-wrong-state.patch
Patch11:        0001-Delay-for-logind-and-fallback-to-seat0.patch
Patch101:       sddm-0.20.0-fedora_config.patch
Patch103:       sddm-0.18.0-environment_file.patch
Patch104:       sddm-rpmostree-tmpfiles-hack.patch
Patch105:       sddm-0.21.0-qt6greeter.patch
Source10:       sddm.pam
Source11:       sddm-autologin.pam
Source12:       sddm-greeter.pam
Source13: sddm.conf
Source14: README.scripts
Source15: sddm.sysconfig
Source16:  sddm-x11.conf
Source17:        sddm-systemd-sysusers.conf
Provides: service(graphical-login) = sddm
Obsoletes: kde-settings-sddm < 20-5
Requires: systemd
%if %{with x11}
Requires: xorg-x11-xinit
%endif
%{?systemd_requires}
Requires(pre): shadow-utils
Requires: sddm-greeter-displayserver
Suggests: sddm-wayland-generic
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
SDDM is a modern graphical display manager aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%package wayland-generic
Summary: Generic Wayland SDDM greeter configuration
Provides: sddm-greeter-displayserver
Conflicts: sddm-greeter-displayserver
Requires: weston
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description wayland-generic
This package contains configuration and dependencies for SDDM
to use Weston for the greeter display server.

This is the generic default Wayland configuration provided
by SDDM.

%if %{with x11}
%package x11
Summary: X11 SDDM greeter configuration
Provides: sddm-greeter-displayserver
Conflicts: sddm-greeter-displayserver
Provides: deprecated()
Requires: xorg-x11-server-Xorg
Requires: %{name} = %{version}-%{release}
Recommends: qt6-qtvirtualkeyboard
BuildArch: noarch
%description x11
This package contains configuration and dependencies for SDDM
to use X11 for the greeter display server.
%endif

%package themes
Summary: SDDM Themes
Obsoletes: sddm < 0.2.0-0.12
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description themes
A collection of sddm themes, including: elarun, maldives, maya

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 %{?commitdate:-n %{name}-%{commit}}

%build

%cmake \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DBUILD_MAN_PAGES:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DENABLE_JOURNALD:BOOL=ON \
  -DSESSION_COMMAND:PATH=/etc/X11/xinit/Xsession \
  -DWAYLAND_SESSION_COMMAND:PATH=/etc/sddm/wayland-session
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
install -Dpm 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/sddm
install -Dpm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/sddm-autologin
install -Dpm 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/pam.d/sddm-greeter
install -Dpm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/sddm.conf
install -Dpm 644 %{SOURCE14} %{buildroot}%{_datadir}/sddm/scripts/README.scripts
install -Dpm 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/sysconfig/sddm
%if %{with x11}
install -Dpm 644 %{SOURCE16} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/x11.conf
%endif
mkdir -p %{buildroot}/run/sddm
mkdir -p %{buildroot}%{_localstatedir}/lib/sddm
mkdir -p %{buildroot}%{_sysconfdir}/sddm/
cp -a %{buildroot}%{_datadir}/sddm/scripts/* \
      %{buildroot}%{_sysconfdir}/sddm/
rm -fv %{buildroot}%{_sysconfdir}/sddm/Xsession
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE17}
%post

%systemd_post sddm.service
(grep \
   -e '^Current=fedora$' \
   -e '^\[XDisplay\]$' \
   -e '^\[WaylandDisplay\]$' \
   %{_sysconfdir}/sddm.conf > /dev/null && \
 sed -i.rpmsave \
   -e 's|^Current=fedora$|#Current=01-breeze-fedora|' \
   -e 's|^\[XDisplay\]$|\[X11\]|' \
   -e 's|^\[WaylandDisplay\]$|\[Wayland\]|' \
   %{_sysconfdir}/sddm.conf
) ||:
%preun

%systemd_preun sddm.service
%postun

%systemd_postun sddm.service
%files -f %{oreon_filedir}/main.list
%files -n sddm-wayland-generic -f %{oreon_filedir}/sddm-wayland-generic.list
%files -n sddm-x11 -f %{oreon_filedir}/sddm-x11.list
%files -n sddm-themes -f %{oreon_filedir}/sddm-themes.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.21.0-13
- Prepare for Oreon 11 (RP1)
