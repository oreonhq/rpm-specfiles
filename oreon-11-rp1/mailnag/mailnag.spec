%global source0_hash 27cff6844f3601cf903505fcd50c2443a7b39720429737583f1b2392bc69a3e9
Name:           mailnag
Version:        2.2.0
Release:        24%{?dist}
Summary:        Mail notification daemon
License:        GPL-2.0-only
URL:            https://github.com/pulb/%{name}
Source0:        https://github.com/pulb/%{name}/archive/v%{version}.tar.gz
Patch0:         mailnag-pingtest_w_fedora.patch
Patch1:         mailnag-deprecated_ssl_wrap.patch
Requires:       python3
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-gstreamer1
Requires:       python3-pyxdg
Requires:       gnome-keyring
Requires:       python3-zombie-imp
BuildArch:      noarch
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
# /oreon:deps
%description
Mailnag checks POP3 and IMAP servers for new mail and when it finds one
creates a proper GNOME 3 notification that mentions sender and subject.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mailnag-%{version}
%patch -P0 -b .patch0 -p1
%patch -P1 -b .patch1 -p1

%build

%py3_build
%install
rm -rf %{buildroot}
%py3_install
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/mailnag.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/mailnag-config.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
