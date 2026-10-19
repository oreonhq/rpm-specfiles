%global source0_hash 4cbef8da2eb1ba28c863844bc3f8fe98c0b90ede17b086cc4bb01875a1dfcb4c
Name:          php-smarty-gettext
Summary:        Gettext support for Smarty
Version:       1.7.0
Release:        1%{?dist}
License:       LGPL-2.1-or-later
URL:           https://github.com/smarty-gettext/smarty-gettext
Source0:        https://github.com/smarty-gettext/smarty-gettext/archive/%{version}/smarty-gettext-%{version}.tar.gz
Source1:       make_smarty_gettext_tarball.sh
BuildArch:     noarch
Requires:      php(language) >= 5.3
Requires:      php-Smarty
Requires:      php-gettext
Provides:      php-composer(smarty-gettext/smarty-gettext) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
smarty-gettext provides gettext (i18n) support for Smarty, the popular PHP
templating engine, to implement an NLS (Native Language Support) API which can
be used to internationalize and translate your PHP applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n smarty-gettext-%{version}

%build

%install
phpab --template fedora --output smarty-gettext-autoload.php . tests
install -d -m 0755 %{buildroot}%{_datadir}/php/Smarty/plugins/
install -p -m 0644 \
  block.t.php \
  function.locale.php \
  smarty-gettext-autoload.php \
  %{buildroot}%{_datadir}/php/Smarty/plugins/
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
