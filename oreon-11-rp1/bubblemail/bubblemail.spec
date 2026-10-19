%global source0_hash becf86cb6f0b914563813f512cbee6b32527b943c34cbba20e3e39bab55ddbc0
Name:           bubblemail
Version:        1.12
Release:        1%{?dist}
Summary:        Extensible mail notification service
License:        GPL-2.0-only
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Patch0:         01.bubblemail-fix_missing_locales.patch
Requires:       folks
Requires:       gnome-keyring
Requires:       hicolor-icon-theme
Requires:       libsecret
Requires:       python3
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-requests
Requires:       python3-gstreamer1
Requires:       python3-pyxdg
Requires:       python3-pysocks
Recommends:     gnome-online-accounts
Recommends:     gnome-shell-extension-bubblemail
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bubblemail = %{version}-%{release}
# /oreon:deps
%description
Bubblemail is a D-Bus service providing a list of the new and unread user's mail
from local mailboxes, pop, imap, and gnome online accounts. It includes a
libnotify frontend to create notifications and can be used by other frontends as
well.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' \
        bubblemail/plugins/spamfilterplugin.py \
        bubblemail/plugins/userscriptplugin.py

%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{python3_sitelib}/etc/ %{buildroot}/etc/
%find_lang %{name}
cat %{name}.lang >> %{pyproject_files}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
%files

%changelog

%autochangelog
