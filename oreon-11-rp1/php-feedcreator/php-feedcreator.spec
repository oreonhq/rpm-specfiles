%global source0_hash 0135f0dd415d307c004afc2f2833cef250f7cfe70dff643f09e7eb395c3881c4

Name:           php-feedcreator
Version:        1.7.2
Release:        33%{?dist}
Summary:        Create RSS feeds

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.bitfolge.de/rsscreator-en.html
Source0:        http://www.bitfolge.de/download/feedcreator_172.zip

BuildArch:      noarch
Requires:       php >= 4.0.3 

%description
FeedCreator.class.php provides an easy way to create RSS feeds from within PHP
using ease to use classes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/php/
cp -a feedcreator.class.php $RPM_BUILD_ROOT%{_datadir}/php/

%files
%doc lgpl.txt
%{_datadir}/php/feedcreator.class.php

%changelog
%autochangelog
