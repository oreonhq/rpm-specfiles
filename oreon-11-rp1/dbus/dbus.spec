%global source1_hash 108723e6bb2b0655abcb8ec7b06d27918bd7ac215f835ba086b45f9780cb529b
%global source0_hash 0ba2a1a4b16afe7bceb2c07e9ce99a8c2c3508e5dec290dbb643384bd6beb7e2
%global source2_key_fpr DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90
%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global gettext_package         dbus-1
%global libselinux_version      2.0.86
%global fedora_release_version  30-0.2
%global generic_release_version 30-0.1
%bcond_without tests
%bcond_with check
%bcond_without cmake
Name:    dbus
Epoch:   1
Version: 1.16.2
Release:        1%{?dist}
Summary:        D-BUS message bus
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:     https://www.freedesktop.org/wiki/Software/dbus/
Source0:        https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz.asc
Source2: gpgkey-DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90.gpg
Source3: 00-start-message-bus.sh
Source4: dbus.socket
Source5: dbus-daemon.service
Source6: dbus.user.socket
Source7: dbus-daemon.user.service
Source8: dbus-systemd-sysusers.conf
Patch0: 0001-tools-Use-Python3-for-GetAllMatchRules.patch
%if %{with cmake}
%endif
%if %{with tests}
%endif
%if %{with check}
%endif
Requires: (dbus-broker >= 16-4 if systemd)
# oreon:deps
BuildRequires:  /usr/bin/Xvfb
BuildRequires:  /usr/bin/ducktype
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  /usr/bin/yelp-build
BuildRequires:  audit-libs-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libX11-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject
BuildRequires:  systemd
BuildRequires:  xmlto
# /oreon:deps
%description
D-BUS is a system for sending messages between applications. It is
used both for the system-wide message bus service, and as a
per-user-login-session messaging facility.

%package common
Summary:        D-BUS message bus configuration
BuildArch:      noarch
Conflicts:      fedora-release < %{fedora_release_version}
Conflicts:      generic-release < %{generic_release_version}
%description common
The %{name}-common package provides the configuration and setup files for D-Bus
implementations to provide a System and User Message Bus.

%package daemon
Summary:        D-BUS message bus
Conflicts:      fedora-release < %{fedora_release_version}
Conflicts:      generic-release < %{generic_release_version}
Requires:       libselinux%{?_isa} >= %{libselinux_version}
Requires:       dbus-common = %{epoch}:%{version}-%{release}
Requires:       dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       dbus-tools = %{epoch}:%{version}-%{release}
%{?sysusers_requires_compat}
%description daemon
D-BUS is a system for sending messages between applications. It is
used both for the system-wide message bus service, and as a
per-user-login-session messaging facility.

%package tools
Summary:        D-BUS Tools and Utilities
Requires:       dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description tools
Tools and utilities to interact with a running D-Bus Message Bus, provided by
the reference implementation.

%package libs
Summary: Libraries for accessing D-BUS
%description libs
This package contains lowlevel libraries for accessing D-BUS.

%package doc
Summary: Developer documentation for D-BUS
Requires: %{name}-daemon = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
This package contains developer documentation for D-Bus along with
other supporting documentation such as the introspect dtd file.

%package devel
Summary: Development files for D-BUS
Requires: dbus-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: xml-common
%description devel
This package contains libraries and header files needed for
developing software that uses D-BUS.

%package tests
Summary: Tests for the %{name}-daemon package
Requires: %{name}-daemon%{?_isa} = %{epoch}:%{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name}-daemon package.

%package x11
Summary: X11-requiring add-ons for D-BUS
Requires: %{name}-daemon = %{epoch}:%{version}-%{release}
%description x11
D-BUS contains some tools that require Xlib to be installed, those are
in this separate package so server systems need not install X.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

CONFIG_OPTIONS=(
  -Dlibaudit=enabled
  -Dselinux=enabled
  -Dsystem_socket=/run/dbus/system_bus_socket
  -Ddbus_user=dbus
  -Duser_session=true
  -Dinstalled_tests=true
  --libexecdir=%{_libexecdir}/dbus-1
)
%global _vpath_builddir build
%meson \
  "${CONFIG_OPTIONS[@]}" \
  -Ddoxygen_docs=enabled \
  -Dducktype_docs=enabled \
  -Dxml_docs=enabled \
  -Dasserts=false \
  -Dqt_help=disabled \
  -Dapparmor=disabled \
  -Dkqueue=disabled \
  -Dlaunchd=disabled
%meson_build
%if %{with check}
%global _vpath_builddir build-check
%meson "${CONFIG_OPTIONS[@]}" -Dasserts=true -Dverbose_mode=true
%meson_build
%endif
%install
%global _vpath_builddir build
%meson_install
rm -f %{buildroot}/%{_pkgdocdir}/examples/GetAllMatchRules.py
%if ! %{with cmake}
rm -rf %{buildroot}%{_libdir}/cmake
%endif
rm -f %{buildroot}%{_unitdir}/dbus.{socket,service}
rm -f %{buildroot}%{_unitdir}/sockets.target.wants/dbus.socket
rm -f %{buildroot}%{_unitdir}/multi-user.target.wants/dbus.service
rm -f %{buildroot}%{_userunitdir}/dbus.{socket,service}
rm -f %{buildroot}%{_userunitdir}/sockets.target.wants/dbus.socket
rm -f %{buildroot}%{_sysusersdir}/dbus.conf
install -Dp -m755 %{SOURCE3} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/00-start-message-bus.sh
install -Dp -m644 %{SOURCE4} %{buildroot}%{_unitdir}/dbus.socket
install -Dp -m644 %{SOURCE5} %{buildroot}%{_unitdir}/dbus-daemon.service
install -Dp -m644 %{SOURCE6} %{buildroot}%{_userunitdir}/dbus.socket
install -Dp -m644 %{SOURCE7} %{buildroot}%{_userunitdir}/dbus-daemon.service
install -Dp -m644 %{SOURCE8} %{buildroot}%{_sysusersdir}/dbus.conf
install --directory %{buildroot}%{_sysconfdir}/dbus-1/session.d
install --directory %{buildroot}%{_sysconfdir}/dbus-1/system.d
install --directory %{buildroot}%{_datadir}/dbus-1/interfaces
install --directory %{buildroot}/var/lib/dbus
install --directory %{buildroot}/run/dbus
install -pm 644 -t %{buildroot}%{_pkgdocdir} \
    doc/introspect.dtd doc/introspect.xsl doc/system-activation.txt
install --directory %{buildroot}%{_datadir}/gtk-doc/html
ln -s %{_pkgdocdir} %{buildroot}%{_datadir}/gtk-doc/html/dbus
cat > dbus-run-installed-tests <<EOF
set -e
timeout="timeout 300s"
ret=0
i=0
tmpdir=\$(mktemp --directory --tmpdir dbus-run-installed-tests.XXXXXX)
for t in %{_libexecdir}/dbus-1/installed-tests/dbus/test-*; do
    i=\$(( \$i + 1 ))
    echo "# \$i - \$t ..."
    echo "x" > "\$tmpdir/result"
    ( set +e; \$timeout \$t; echo "\$?" > "\$tmpdir/result" ) 2>&1 | sed 's/^/# /'
    e="\$(cat "\$tmpdir/result")"
    case "\$e" in
        (0)
            echo "ok \$i - \$t"
            ;;
        (77)
            echo "ok \$i # SKIP \$t"
            ;;
        (*)
            echo "not ok \$i - \$t (\$e)"
            ret=1
            ;;
    esac
done
rm -rf tmpdir
echo "1..\$i"
exit \$ret
EOF
install -pm 755 -t %{buildroot}%{_libexecdir}/dbus-1 dbus-run-installed-tests
%oreon_autofiles dbus-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-daemon usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dbus-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-x11 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

pushd build-check
export DISPLAY=42
{ Xvfb :${DISPLAY} -nolisten tcp -auth /dev/null >/dev/null 2>&1 &
  trap "kill -15 $! || true" 0 HUP INT QUIT TRAP TERM; };
%meson_test
popd
%endif
%pre daemon

%sysusers_create_compat %{SOURCE8}
%post common

%systemd_post dbus.socket
%systemd_user_post dbus.socket
%post daemon

%systemd_post dbus-daemon.service
%systemd_user_post dbus-daemon.service
%preun common

%systemd_preun dbus.socket
%systemd_user_preun dbus.socket
%preun daemon

%systemd_preun dbus-daemon.service
%systemd_user_preun dbus-daemon.service
%postun common

%systemd_postun dbus.socket
%systemd_user_postun dbus.socket
%postun daemon

%systemd_postun dbus-daemon.service
%systemd_user_postun dbus-daemon.service
%triggerpostun common -- dbus-common < 1:1.12.10-4

if [ -x /usr/bin/systemctl ]; then
    systemctl --no-reload preset dbus.socket &>/dev/null || :
    systemctl --no-reload --global preset dbus.socket &>/dev/null || :
fi
%triggerpostun daemon -- dbus-daemon < 1:1.12.10-7

if [ -x /usr/bin/systemctl ]; then
    systemctl --no-reload preset dbus-daemon.service &>/dev/null || :
    systemctl --no-reload --global preset dbus-daemon.service &>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n dbus-common -f %{oreon_filedir}/dbus-common.list
%files -n dbus-daemon -f %{oreon_filedir}/dbus-daemon.list
%files -n dbus-tools -f %{oreon_filedir}/dbus-tools.list
%files -n dbus-libs -f %{oreon_filedir}/dbus-libs.list
%files -n dbus-doc -f %{oreon_filedir}/dbus-doc.list
%files -n dbus-devel -f %{oreon_filedir}/dbus-devel.list
%files -n dbus-tests -f %{oreon_filedir}/dbus-tests.list
%files -n dbus-x11 -f %{oreon_filedir}/dbus-x11.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.2-1
- Prepare for Oreon 11 (RP1)
