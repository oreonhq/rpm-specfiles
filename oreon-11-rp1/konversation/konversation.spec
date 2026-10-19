%global stable_kf6 stable
%global source0_hash b859bcf527fec1d4fbb29a0ba4d1e18430cef58871994617881895e7867fb6f7
ExcludeArch: %{ix86}
Name:           konversation
Version: 25.12.3
Release:        1%{?dist}
Summary:        A user friendly IRC client
License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:            http://konversation.kde.org/
%if 0%{?snap}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%else
%endif
Source1:        konversationrc
Requires: qca-qt6-ossl%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(qca2-qt6)
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konversation.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.konversation.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
