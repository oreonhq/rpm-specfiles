%global source0_hash c721cbad5fcab8c9299ccd009ced42974bc969e1c315f7c40a3bf225c42fe46e
Name:		php-wikimedia-ip-set
Version:	4.0.0
Release:        1%{?dist}
Summary:        Library to match IP addresses against CIDR specifications
License:	GPL-2.0-or-later
URL:		http://www.mediawiki.org/wiki/IPSet
Source0:        https://github.com/wikimedia/IPSet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	php(language) >= 7.2.9
Requires:	php-ctype
Requires:	php-spl
Provides:	php-composer(wikimedia/ip-set) = %{version}
# oreon:deps
BuildRequires:  php-theseer-autoload
# /oreon:deps
%description
IPSet is a PHP library to match IPs against CIDR specs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPSet-%{version}

%build

phpab --output src/autoload.php src
%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/IPSet
cp -rp src/* %{buildroot}%{_datadir}/php/IPSet
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
