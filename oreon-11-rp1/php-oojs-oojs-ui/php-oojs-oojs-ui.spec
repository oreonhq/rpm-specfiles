%global source0_hash cd3a08ecd0c7cf856f9e6dac83fe178672c897e66c65d730d184a14e7f77851a

Name:		php-oojs-oojs-ui
Version:	0.51.2
Release:	3%{?dist}
Summary:	Object-Oriented JavaScript – User Interface

License:	MIT
URL:		http://www.mediawiki.org/wiki/OOjs_UI
# Wikimedia changed server software and now doesn't support downloads
# https://phabricator.wikimedia.org/T111887
Source0:	https://github.com/wikimedia/oojs-ui/archive/refs/tags/v%{version}.tar.gz#/oojs-ui-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 7.4.3

Provides:	php-composer(oojs/oojs-ui) = %{version}

%description
OOjs UI (Object-Oriented JavaScript – User Interface) is a library that allows
developers to rapidly create front-end web applications that operate
consistently across a multitude of browsers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n oojs-ui-%{version}

%build
phpab --output php/autoload.php php

%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/OOUI
cp -rp php/* %{buildroot}%{_datadir}/php/OOUI

%files
%license LICENSE-MIT
%doc AUTHORS.txt History.md README.md
%{_datadir}/php/OOUI

%changelog
%autochangelog
