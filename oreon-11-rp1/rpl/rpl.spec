%global source0_hash 53e9ac5e82e034b7f58cf384eb435b5ddfbfa88695184c06947596f3bc1ce58d

Name:           rpl
Version:        1.5.7
Release:        34%{?dist}
Summary:        Intelligent recursive search/replace utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/kcoyner/rpl/
Source0:        https://github.com/kcoyner/rpl/archive/v%{version}.tar.gz

# Reported upstream at https://github.com/kcoyner/rpl/issues/5
Patch0:         rpl-python3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
rpl is a UN*X text replacement utility. It will replace strings with
new strings in multiple text files. It can work recursively over
directories and supports limiting the search to specific file
suffixes.

rpl was originally written by Joe Laffey; this is a rewritten version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0

# upstream mistake
sed -i s/1\.5\.6/%{version}/ setup.py

%build
%py3_build

%install
%py3_install
%{__install} -m 0644 -D rpl.1 %{buildroot}%{_mandir}/man1/rpl.1

%files
%doc LICENSE README.md
%{_bindir}/rpl
%{_mandir}/man1/rpl.1.gz
%{python3_sitelib}/*

%changelog
%autochangelog
