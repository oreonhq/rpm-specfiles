%global source0_hash b859bcf527fec1d4fbb29a0ba4d1e18430cef58871994617881895e7867fb6f7

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           konversation
Version: 25.12.3
Release: 1%{?dist}
Summary:        A user friendly IRC client

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:            http://konversation.kde.org/
%if 0%{?snap}
# use releaseme script
Source0:        %{name}-%{version}-%{snap}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/konversation-%{version}.tar.xz
%endif

Source1:        konversationrc

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: pkgconfig(qca2-qt6)

# python3
BuildRequires: python3-devel

Requires: qca-qt6-ossl%{?_isa}

%description
A simple and easy to use IRC client with support for
strikeout; multi-channel joins; away / unaway messages;
ignore list functionality; support for foreign
language characters; auto-connect to server; optional timestamps
to chat windows; configurable background colors and much more

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Add Comment key to .desktop file
grep '^Comment=' %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop || \
desktop-file-edit \
  --set-comment="A user friendly IRC client" \
  data/org.kde.%{name}.desktop

%py3_shebang_fix \
  data/scripts/* \
  data/scripting_support/python/konversation/*.py

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

install -p -m644 -D %{SOURCE1} %{buildroot}%{_kf6_sysconfdir}/xdg/konversationrc

%find_lang konversation --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konversation.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.konversation.desktop

%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kf6_datadir}/icons/hicolor &> /dev/null ||:

%posttrans
gtk-update-icon-cache %{_kf6_datadir}/icons/hicolor &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kf6_datadir}/icons/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kf6_datadir}/icons/hicolor &> /dev/null ||:
  update-desktop-database -q &> /dev/null ||:
fi
%endif

%files  -f konversation.lang
%doc ChangeLog README
%config(noreplace) %{_kf6_sysconfdir}/xdg/konversationrc
%{_kf6_bindir}/konversation
%{_kf6_datadir}/applications/org.kde.konversation.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.konversation.service
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/knotifications6/konversation.notifyrc
%{_kf6_datadir}/knsrcfiles/konversation_nicklist_theme.knsrc
%{_kf6_datadir}/konversation/
%{_kf6_datadir}/qlogging-categories6/konversation.categories
%{_kf6_metainfodir}/org.kde.konversation.appdata.xml

%changelog
%autochangelog
