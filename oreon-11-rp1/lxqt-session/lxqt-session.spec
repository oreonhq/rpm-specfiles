%global source0_hash c9f712925dd1246693d6892334f325596d685d4341822cf8071bad17233ae922
Name:         lxqt-session
Summary:        Main session for LXQt desktop suite
Version:      2.4.0
Release:        1%{?dist}
License:      LGPL-2.1-only
URL:          https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0101:    0101-Add-miriway-entry-for-Wayland-window-managers.patch
Patch0102:    0102-set-default-compositor.patch
Patch0103:    0103-set-locale1-envar-for-miriway.patch
Patch1001:    1001-Drop-Hyprland-entry-for-Wayland-window-managers.patch
Recommends:   pcmanfm-qt
Requires:     lxqt-wayland-session
Recommends:   lxqt-x11-session
Conflicts:    %{name} < 2.1.1-5
Obsoletes:    %{name} < 2.1.1-5
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  qtxdg-tools
# /oreon:deps
%description
%{summary}.

%package -n lxqt-x11-session
BuildArch:    noarch
Summary:      Files for LXQt X11 session
Requires:     openbox-theme-mistral-thin
Requires:     %{name} = %{version}-%{release}
Requires:     dbus-x11
Recommends:   xscreensaver
Conflicts:    %{name} < 2.1.1-5
Obsoletes:    %{name} < 2.1.1-5
%description -n lxqt-x11-session
This package provides the LXQt X11 session files.

%package l10n
BuildArch:    noarch
Summary:      Translations for lxqt-session
Requires:     lxqt-session
%description l10n
This package provides translations for the lxqt-session package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
for name in config-session hibernate lockscreen logout reboot shutdown suspend; do
  desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-${name}.desktop
done
mkdir %{buildroot}%{_sysconfdir}/lxqt/
cp %{buildroot}%{_datadir}/lxqt/lxqt.conf %{buildroot}%{_datadir}/lxqt/session.conf %{buildroot}%{_sysconfdir}/lxqt/
%find_lang lxqt-session --with-qt
%find_lang lxqt-config-session --with-qt
%find_lang lxqt-leave --with-qt
%oreon_autofiles lxqt-x11-session usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-x11-session -f %{oreon_filedir}/lxqt-x11-session.list
%files -n lxqt-session-l10n -f %{oreon_filedir}/lxqt-session-l10n.list

%changelog

%autochangelog
