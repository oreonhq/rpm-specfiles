%global source0_hash e31327af911b463da6732e27adc454e749d3d7ffd3b7e6dda676903f8d5d9f4d

# set upstream name variable
%global srcname slixmpp_omemo

Name:           python-slixmpp-omemo
Version:        0.9.1
Release:        9%{?dist}
Summary:        OMEMO plugin for Slixmpp

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://codeberg.org/poezio/slixmpp-omemo
Source0:        https://codeberg.org/poezio/slixmpp-omemo/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-slixmpp
BuildRequires:  python3-omemo
# for tests
#BuildRequires:  python3-pytest

%description
This library provides an interface between python-omemo and
python-slixmpp.

%package     -n python3-slixmpp-omemo
Summary:        OMEMO plugin for Slixmpp

%description -n python3-slixmpp-omemo
This library provides an interface between python-omemo and
python-slixmpp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n slixmpp-omemo
# Remove shebang in 3 non-executable files
find ./%{srcname}/ -type f '(' -name __init__.py -o -name stanza.py -o -name version.py ')' -ls -exec sed -i 's@#!/usr/bin/env python3@@' '{}' \;

%build
%py3_build

%install
%py3_install

%check
# no tests to run with pytest: Disabling.

%files -n python3-slixmpp-omemo
%license LICENSE
%doc CONTRIBUTING.rst ChangeLog README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
