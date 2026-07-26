%global source0_hash 99c012c93c42c97a4fa3b89f1dbddcf56afb3d33a29465df7ca71fccb2f81b12

Name:		php-wikimedia-utfnormal
Version:	4.0.0
Release:	6%{?dist}
Summary:	Unicode normalization functions

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.mediawiki.org/wiki/Utfnormal
Source0:	https://github.com/wikimedia/utfnormal/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 7.4.3

Provides:	php-composer(wikimedia/utfnormal) = %{version}

%description
utfnormal is a library that contains unicode normalization functions. It was
split out of MediaWiki core during the 1.25 development cycle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n utfnormal-%{version}

%build
phpab --output src/autoload.php src

%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/UtfNormal
cp -rp src/* %{buildroot}%{_datadir}/php/UtfNormal

%files
%license COPYING
%doc README.md
%{_datadir}/php/UtfNormal

%changelog
%autochangelog
