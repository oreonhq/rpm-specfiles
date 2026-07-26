%global source0_hash cd451d420ff8b2a59d406e9d4c2d8bbd45ba7de7292a2c93ad3f5263c58dc3b8

# remirepo/fedora spec file for php-phpunit-php-token-stream4
#
# Copyright (c) 2010-2023 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    a853a0e183b9db7eed023d7933a858fa1c8d25a3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-token-stream
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        4
%global php_home     %{_datadir}/php
# Fake NS for directory layout
%global ns_vendor    SebastianBergmann
%global ns_project   PhpTokenStream
%if %{bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.4
Release:        16%{?dist}
Summary:        Wrapper around PHP tokenizer extension

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-tokenizer
BuildRequires:  php-pcre
BuildRequires:  php-spl
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# from composer.json
#        "php": "^7.3 || ^8.0",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 7.3
Requires:       php-tokenizer
# from phpcompatinfo report for version 4.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Wrapper around PHP tokenizer extension.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee -a src/NewTokens.php
<?php declare(strict_types=1);

// From PHP 8.1
class PHP_Token_AMPERSAND_FOLLOWED_BY_VAR_OR_VARARG extends PHP_Token
{
}
EOF

%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
