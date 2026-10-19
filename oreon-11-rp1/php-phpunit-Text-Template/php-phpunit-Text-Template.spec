%global source0_hash ee08be115a91084849e11a11a04837bbcc010194bc97488308b9a652ec639cea
%global gh_commit    31f8b717e51d9a2afca6c9f046f5d69fc27c8686
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-text-template
%global php_home     %{_datadir}/php
%global pear_name    Text_Template
%global pear_channel pear.phpunit.de
Name:           php-phpunit-Text-Template
Version:        1.2.1
Release:        1%{?dist}
Summary:        Simple template engine
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
Requires:       php(language) >= 5.3.3
Requires:       php-spl
Provides:       php-composer(phpunit/php-text-template) = %{version}
# oreon:deps
BuildRequires:  //bin/phpab
BuildRequires:  php(language)
# /oreon:deps
%description
Simple template engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Restore previous PSR-0 layout
mkdir -p Text/Template
mv src/Template.php Text/
rmdir src

%build

: Generate autoloader
%{_bindir}/phpab \
  --output  Text/Template/Autoload.php \
  --basedir Text/Template \
  Text
%install
mkdir -p    %{buildroot}%{php_home}
cp -pr Text %{buildroot}%{php_home}
%oreon_autofiles main

%post

if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
