%global source0_hash f37be348ffd490799fbc3b3531bd51eccc427caaa89f609ddc95a0865293b252

Name:		php-wikimedia-ip-set
Version:	3.1.0
Release:	10%{?dist}
Summary:	Library to match IP addresses against CIDR specifications

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.mediawiki.org/wiki/IPSet
Source0:	https://github.com/wikimedia/IPSet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 7.2.9
Requires:	php-ctype
Requires:	php-spl

Provides:	php-composer(wikimedia/ip-set) = %{version}

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

%files
%license COPYING
%doc README.md
%{_datadir}/php/IPSet

%changelog
%autochangelog
