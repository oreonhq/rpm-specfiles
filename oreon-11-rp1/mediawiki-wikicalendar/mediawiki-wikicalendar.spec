%global source0_hash fd7847eddffa29651a6e131c91780ee28cc2b820696dcf99d479ec99ef2a578d

Name:           mediawiki-wikicalendar
Version:        1.16
Release:        30%{?dist}
Summary:        Simple calendar extension for mediawiki

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://code.google.com/p/wikicalendar/
Source0:        http://wikicalendar.googlecode.com/files/wikicalendar-%{version}.tar.gz
BuildArch:      noarch

Requires:       mediawiki

%description
The extension adds an <calendar> tag to the mediawiki syntax which can show
calendars in different formats.

The idea was to keep the calendar as simple as possible and leave all
the editing and page creation to mediawiki. It doesn't require any new
database tables or files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n wikicalendar-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/calendar
install -cpm 644 calendar/*.php $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/calendar/

%files
%{_datadir}/mediawiki/extensions/calendar
%doc ChangeLog README LICENSE

%changelog
%autochangelog
