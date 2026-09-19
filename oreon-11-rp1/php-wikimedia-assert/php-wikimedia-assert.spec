%global source0_hash 9289425064c826d15b9da683517e77cfbf017927c1d3805db23297b27146ad6a

Name:		php-wikimedia-assert
Version:	0.5.1
Release:	9%{?dist}
Summary:	An alternative to PHP's assert

License:	MIT
URL:		https://github.com/wikimedia/Assert
Source0:	https://github.com/wikimedia/Assert/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-spl

Provides:	php-composer(wikimedia/assert) = %{version}

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

%files
%license COPYING
%doc README.md RELEASE-NOTES.md
%{_datadir}/php/Wikimedia

%changelog
%autochangelog
