%global source0_hash c4129895808e5441f053115fd4724a5534a605cde75b189e961baa4736dda2b7
Name:		php-oojs-oojs-ui
Version:	0.53.2
Release:        1%{?dist}
Summary:        Object-Oriented JavaScript – User Interface
License:	MIT
URL:		http://www.mediawiki.org/wiki/OOjs_UI
Source0:        https://github.com/wikimedia/oojs-ui/archive/refs/tags/v%{version}.tar.gz#/oojs-ui-%{version}.tar.gz
BuildArch:	noarch
Requires:	php(language) >= 7.4.3
Provides:	php-composer(oojs/oojs-ui) = %{version}
# oreon:deps
BuildRequires:  php-theseer-autoload
# /oreon:deps
%description
OOjs UI (Object-Oriented JavaScript – User Interface) is a library that allows
developers to rapidly create front-end web applications that operate
consistently across a multitude of browsers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir oojs-ui-%{version}
%oreon_prep
%build

phpab --output php/autoload.php php
%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/OOUI
cp -rp php/* %{buildroot}%{_datadir}/php/OOUI
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
