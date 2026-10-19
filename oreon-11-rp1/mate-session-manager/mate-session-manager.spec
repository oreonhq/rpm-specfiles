%global source0_hash d32ce4595ba1da65290777203f2bc82bd973b214a3a04080a1ef5c68990a2d7b
%global branch 1.28
Name:          mate-session-manager
Summary:        MATE Desktop session manager
License:       GPL-2.0-or-later
Version:       %{branch}.0
Release:        1%{?dist}
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        mate-session-manager_0001-Use-g_info-for-screensaver-left-the-bus-message.patch
Patch2:        mate-session-manager_0004-util-Only-accept-common-space-characters.patch
Patch3:        mate-session-manager_0005-util-Disable-capturing-of-subpatterns.patch
Patch4:        mate-session-manager_0006-manager-Loosen-environment-variable-restrictions.patch
Requires: system-logos
Requires: mate-control-center
Requires: mate-polkit
Requires: polkit-desktop-policy
Requires: mate-desktop-libs
Requires: dbus-x11
# oreon:deps
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mesa-libGLES-devel
BuildRequires:  systemd-devel
BuildRequires:  xmlto
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
This package contains a session that can be started from a display
manager such as MDM. It will load all necessary applications for a
full-featured user session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                    \
    --disable-static          \
    --enable-ipv6             \
    --with-default-wm=marco   \
    --with-systemd            \
    --enable-docbook-docs     \
    --disable-schemas-compile
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-session-properties.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
