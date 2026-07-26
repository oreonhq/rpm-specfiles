%global source0_hash c9a7d7e24bae42d4ead1b096599e3a803cbf1091b0b782d12bcc297d9359f007

Name:           pidgin-birthday-reminder
Version:        1.13
Release:        15%{?dist}
Summary:        Birthday Reminder plugin for Pidgin

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/kgraefe/pidgin-birthday-reminder
Source0:        https://github.com/kgraefe/pidgin-birthday-reminder/releases/download/v%{version}/pidgin-birthday-reminder-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pidgin-devel
BuildRequires:  /usr/bin/appstream-util
Requires:       pidgin

%description
Pidgin Birthday Reminder reminds you of your buddies birthdays. Birthdays can
be set by hand or be automatically filled-in for ICQ, MSN and XMPP protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la

%find_lang %{name}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/pidgin-birthday-reminder.metainfo.xml

%files -f %{name}.lang
%license COPYING
%{_libdir}/pidgin/*.so
%{_datadir}/appdata/pidgin-birthday-reminder.metainfo.xml
%{_datadir}/pixmaps/pidgin/birthday_reminder/
# Pidgin package doesn't own sounds/pidgin/ dir
%dir %{_datadir}/sounds/pidgin/
%{_datadir}/sounds/pidgin/birthday_reminder/

%changelog
%autochangelog
