%global source0_hash ef63cb46038cac0edd6e25327d7382a6b490f436ecb1d680166f8a28a30ab2a3
%global srcname poezio_omemo
Name:           poezio-omemo
Version:        0.7.0
Release:        1%{?dist}
Summary:        OMEMO plugin for the Poezio XMPP client
License:        GPL-3.0-only
URL:            https://codeberg.org/poezio/poezio-omemo
Source0:        https://codeberg.org/poezio/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This plugin provides OMEMO support for Poezio client.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}
# Remove shebang in 2 non-executable files
find ./%{srcname}/ -type f '(' -name __init__.py -o -name version.py ')' -ls -exec sed -i 's@#!/usr/bin/env python3@@' '{}' \;

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
