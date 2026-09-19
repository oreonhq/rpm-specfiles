%global source0_hash 29133b82e93a8a97b67d8893ef0f0ac904ba73320404e7751a6ac81dddad2966

Name:           php-pdb
Version:        1.3.4
Release:        39%{?dist}
Summary:        PHP classes for manipulating Palm OS databases

License:        LGPL-2.1-or-later
URL:            http://php-pdb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/php-pdb/php-pdb-1_3_4.tar.gz

# Fix incorrect FSF addresses. Submitted upstream:
#   https://github.com/fidian/php-pdb/pull/5
Patch0:         php-pdb-licence.patch

BuildArch:      noarch

Requires:       php >= 4.0.1

%description
PHP-PDB is a set of PHP classes that manipulate Palm OS databases. It lets you
read, write, alter, and easily use data that is meant to be sent to or
retrieved from a handheld.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn php-pdb
%patch -P0 -p1

%build
# nothing to do

%install

# install php-pdb library
install -m 0755 -d %{buildroot}%{_datadir}/php/php-pdb
install -p -m 644 -t %{buildroot}%{_datadir}/php/php-pdb php-pdb.inc

# install modules
install -m 0755 -d %{buildroot}%{_datadir}/php/php-pdb/modules
install -p -m 644 -t %{buildroot}%{_datadir}/php/php-pdb/modules modules/*.inc

%files
%{_datadir}/php/php-pdb
%doc pdb-test.php
%license doc/{COPYING,LEGAL}

%changelog
%autochangelog
