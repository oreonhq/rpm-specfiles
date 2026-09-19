%global source0_hash 22bf4aaece5c186c16904ea80cac647f6974917c3046e7f1bf851e03a02cc8f5

Summary:        Gettext emulation in PHP
Name:           php-php-gettext
Version:        1.0.12
Release:        22%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://launchpad.net/php-gettext
Source0:        https://launchpad.net/php-gettext/trunk/%{version}/+download/php-gettext-%{version}.tar.gz
Patch0:         php-php-gettext-1.0.11-php7.patch
Requires:       php-common
Requires:       php-mbstring
Obsoletes:      php-gettext < 1.0.11-5
BuildArch:      noarch

%description
This library provides PHP functions to read MO files even when gettext is 
not compiled in or when appropriate locale is not present on the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n php-gettext-%{version}
%patch -P0 -p1 -b .php7

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/php/gettext/
install -p -m 644 gettext.php streams.php gettext.inc $RPM_BUILD_ROOT%{_datadir}/php/gettext/

%files
%license COPYING
%doc README AUTHORS
%{_datadir}/php/gettext/

%changelog
%autochangelog
