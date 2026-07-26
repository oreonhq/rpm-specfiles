%global source0_hash 0f4620dcbbf963f27c86bdf31cfcae9413492e0600c3c8d85835cb746b209c9d

Name:         lxqt-session
Summary:      Main session for LXQt desktop suite
Version:      2.3.0
Release:      3%{?dist}
License:      LGPL-2.1-only
URL:          https://lxqt-project.org/
Source0:      https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream

# Proposed upstream
# https://github.com/lxqt/lxqt-session/pull/571
Patch0101:    0101-Add-miriway-entry-for-Wayland-window-managers.patch
Patch0102:    0102-set-default-compositor.patch
Patch0103:    0103-set-locale1-envar-for-miriway.patch

# Downstream only
Patch1001:    1001-Drop-Hyprland-entry-for-Wayland-window-managers.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  qtxdg-tools
BuildRequires:  perl

#Needs Updated
#Requires:      lxqt-themes-fedora

# use pcmanfm-qt for default desktop
Recommends:   pcmanfm-qt

# We want the Wayland session installed
Requires:     lxqt-wayland-session

# Retain this for now
Recommends:   lxqt-x11-session

# For package split of x11 session
Conflicts:    %{name} < 2.1.1-5
Obsoletes:    %{name} < 2.1.1-5

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

%autosetup -S git_am

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
%if 0%{?fedora}
sed -i 's/theme=frost/theme=fedora-lxqt/g;s/icon_theme=oxygen/icon_theme=breeze/g' %{buildroot}%{_sysconfdir}/lxqt/lxqt.conf
sed -i 's/cursor_theme=whiteglass/cursor_theme=breeze_cursors/g;/General/a window_manager=openbox' %{buildroot}%{_sysconfdir}/lxqt/session.conf
%endif

%find_lang lxqt-session --with-qt
%find_lang lxqt-config-session --with-qt
%find_lang lxqt-leave --with-qt

%files
%dir %{_sysconfdir}/lxqt
%{_bindir}/lxqt-session
%{_bindir}/lxqt-config-session
%{_bindir}/lxqt-leave
%{_datadir}/applications/*.desktop
%config(noreplace) %{_sysconfdir}/lxqt/session.conf
%config(noreplace) %{_sysconfdir}/lxqt/lxqt.conf
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/windowmanagers.conf
%{_mandir}/man1/lxqt-config-session*
%{_mandir}/man1/lxqt-leave*
%{_mandir}/man1/lxqt-session*
%{_datadir}/lxqt/waylandwindowmanagers.conf

%files -n lxqt-x11-session
%config(noreplace) %{_sysconfdir}/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_bindir}/startlxqt
%{_datadir}/xsessions/lxqt.desktop
%{_mandir}/man1/startlxqt.1*

%files l10n -f lxqt-session.lang -f lxqt-leave.lang -f lxqt-config-session.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/%{name}
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/lxqt-session
%{_datadir}/lxqt/translations/lxqt-config-session/lxqt-config-session_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-session/lxqt-config-session_arn.qm
%{_datadir}/lxqt/translations/lxqt-leave/lxqt-leave_ast.qm
%{_datadir}/lxqt/translations/lxqt-leave/lxqt-leave_arn.qm
%{_datadir}/lxqt/translations/lxqt-session/lxqt-session_ast.qm
%{_datadir}/lxqt/translations/lxqt-session/lxqt-session_arn.qm

%changelog
%autochangelog
