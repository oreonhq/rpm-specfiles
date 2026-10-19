%global source0_hash 430eb6633841191642b6978ddaadc8a3547de177a6d88e57882e0e5374e83416
%bcond_with    tests
%global gh_commit    dca41cd15c2ac9d055ad70dbfd011130757d1f82
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   PHP-Parser
%global pk_project   php-parser
%global php_home     %{_datadir}/php
%global ns_project   PhpParser
%global major        5
%global upstream_version 5.7.0
Name:           php-%{gh_owner}-%{pk_project}%{major}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        A PHP parser written in PHP - version 5
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.4
Requires:       php-tokenizer
Requires:       php-json
Requires:       php-ctype
Requires:       php-cli
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-ctype
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  php-tokenizer
BuildRequires:  phpunit9
# /oreon:deps
%description
This is a PHP parser written in PHP.
Its purpose is to simplify static code analysis and manipulation.

This package provides the library version %{major} and the php-parse%{major} command.

Documentation: https://github.com/nikic/PHP-Parser/tree/master/doc

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm

%build

: Generate an simple classmap autoloader
phpab --template fedora \
      --tolerant \
      --output lib/%{ns_project}/autoload.php \
      lib/%{ns_project}
%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr lib/%{ns_project} %{buildroot}%{php_home}/%{ns_project}%{major}
: Command
install -Dpm 0755 bin/php-parse %{buildroot}%{_bindir}/php-parse%{major}
%oreon_autofiles main

%check

%if %{with tests}
: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/php-parse > bin/php-parse-test
php bin/php-parse-test --help
: Test suite autoloader
mkdir vendor
cat << 'AUTOLOAD' | tee vendor/autoload.php
<?php
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', dirname(__DIR__).'/test/PhpParser/');
AUTOLOAD
: Upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84 php85; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d include_path=%{php_home} \
       -d auto_prepend_file=%{buildroot}/%{php_home}/%{ns_project}%{major}/autoload.php \
      ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
