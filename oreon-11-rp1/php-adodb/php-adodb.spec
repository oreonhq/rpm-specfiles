%global source0_hash 5fffc7d0020996a9b9a1fe5824cd3bbb38e1f2add27aa235fda2d1b9effe3cee

%{!?_httpd_contentdir: %{expand: %%global _httpd_contentdir /var/www}}

Name:           php-adodb
Summary:        Database abstraction layer for PHP
Version:        5.22.11
Release:        2%{?dist}

License:        BSD-3-Clause or LGPL-2.0-or-later
URL:            http://adodb.org
BuildArch:      noarch
# for macros
BuildRequires:  httpd-devel

Source0:        http://downloads.sourceforge.net/adodb/adodb-%{version}.tar.gz

Requires:       php-common

%description
ADOdb is an object oriented library written in PHP that abstracts database 
operations for portability. It is modelled on Microsoft's ADO, but has many
improvements that make it unique (eg. pivot tables, Active Record support, 
generating HTML for paging recordsets with next and previous links, cached 
recordsets, HTML menu generation, etc).
ADOdb hides the differences between the different databases so you can easily
switch DBs without changing code.

# !! TODO !! MAKE A SUBPACKAGE FOR THE PEAR::AUTH DRIVER

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n adodb5

%build
# fix dir perms
find . -type d | xargs chmod 755
# fix file perms
find . -type f | xargs chmod 644

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_httpd_contentdir}/icons
install -d $RPM_BUILD_ROOT%{_datadir}/php/adodb
cp -pr * $RPM_BUILD_ROOT%{_datadir}/php/adodb/

# cleanup
rm -rf $RPM_BUILD_ROOT%{_datadir}/php/adodb/docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/php/adodb/tests
rm -f $RPM_BUILD_ROOT%{_datadir}/adodb/*.txt

%files
%license LICENSE.md
%doc README.md docs/*
%{_datadir}/php/adodb

%changelog
%autochangelog
