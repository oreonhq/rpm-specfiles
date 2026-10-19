%global source0_hash 7cda9cfc2e2849a22486d14dcbf5aa5354c480735112fb5a5b7b26fb760dac4c
%global gh_commit    e7be26966b7398204a234f8673fdad5ac6277802
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     myclabs
%global gh_project   php-enum
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    MyCLabs
%global ns_project   Enum
%global php_home     %{_datadir}/php
%bcond_without       tests
Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.8.5
Release:        1%{?dist}
Summary:        PHP Enum implementation
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.3
Requires:       php-json
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-json
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
PHP Enum implementation inspired from SplEnum.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

mv stubs/Stringable.php src/

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
require_once __DIR__ . '/Stringable.php';
EOF

%build

%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee tests/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\Tests\\%{ns_project}\\', __DIR__ . '/../tests');
require __DIR__ . '/bootstrap.php';
EOF
ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap tests/autoload.php || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
