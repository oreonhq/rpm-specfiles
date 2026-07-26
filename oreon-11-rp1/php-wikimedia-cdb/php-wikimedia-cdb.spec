%global source0_hash 1f5f9d084a99cfbb1c3bc6e30e81e536164e5a1bccfc27fae47a43b6dfb87007

Name:		php-wikimedia-cdb
Version:	3.0.0
Release:	6%{?dist}
Summary:	CDB functions for PHP

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.mediawiki.org/wiki/CDB
Source0:	https://github.com/wikimedia/cdb/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-dba
BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 7.4.0

Provides:	php-composer(wikimedia/cdb) = %{version}

%description
CDB, short for "constant database", refers to a very fast and highly reliable
database system which uses a simple file with key value pairs. This library
wraps the CDB functionality exposed in PHP via the dba_* functions. In cases
where dba_* functions are not present or are not compiled with CDB support,
a pure-PHP implementation is provided for falling back.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cdb-%{version}

%build
phpab --output src/autoload.php src

%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/Cdb
cp -rp src/* %{buildroot}%{_datadir}/php/Cdb

%files
%license COPYING
%doc README.md
%{_datadir}/php/Cdb

%changelog
%autochangelog
