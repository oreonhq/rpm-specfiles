%global source0_hash 929c31de184dd3d413b6433d9fe4b378fdfda18dfbb8e8ba03bd1829f68a99ed
Name:		php-wikimedia-assert
Version:	0.5.1
Release:        9%{?dist}
Summary:        An alternative to PHP's assert
License:	MIT
URL:		https://github.com/wikimedia/Assert
Source0:        https://github.com/wikimedia/Assert/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	php(language) >= 5.3.0
Requires:	php-spl
Provides:	php-composer(wikimedia/assert) = %{version}
# oreon:deps
BuildRequires:  php-theseer-autoload
# /oreon:deps
%description
This package provides an alternative to PHP's assert() that allows for a
simple and reliable way to check preconditions and postconditions in PHP
code. It was proposed as a MediaWiki RFC, but is completely generic and
can be used by any PHP program or library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Assert-%{version}

%build

phpab --output src/autoload.php src
%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/Wikimedia/Assert
cp -rp src/* %{buildroot}%{_datadir}/php/Wikimedia/Assert
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
