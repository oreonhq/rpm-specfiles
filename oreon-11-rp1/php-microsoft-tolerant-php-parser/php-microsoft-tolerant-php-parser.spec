%global source0_hash 5ae5736a75ec77beacac0d5487ed4ce7ed89507c28a5c19c13e025d28b400137

# remirepo/fedora spec file for php-microsoft-tolerant-php-parser
#
# Copyright (c) 2018-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    3eccfd273323aaf69513e2f1c888393f5947804b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Microsoft
%global gh_project   tolerant-php-parser
# Packagist
%global pk_vendor    microsoft
%global pk_name      %{gh_project}
# PSR-0 namespace
%global ns_vendor    %{gh_owner}
%global ns_project	 PhpParser

%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.1.2
Release:        8%{?dist}
Summary:        Tolerant PHP-to-AST parser

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5.15"
BuildRequires:  phpunit8
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.2"
# php-parser 1.4 for autoloader
Requires:       php(language) >= 7.2
# From phpcompatifo report for 2.1.0
Requires:       php-reflection
Requires:       php-json
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
This is an early-stage PHP parser designed, from the beginning, for IDE usage
scenarios. There is still a ton of work to be done, so at this point, this
repo mostly serves as an experiment and the start of a conversation.

Autoloader %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
%if %{with_tests}
sed -e 's:src/bootstrap.php:%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php:' \
    -i phpunit.xml

# test using BaseTestListener dropped in phpunit7
rm tests/LexicalGrammarTest.php
rm tests/ParserGrammarTest.php

: Run the test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --testsuite invariants \
      || ret=1

    $cmd %{_bindir}/phpunit8 \
      --testsuite grammar \
      --filter '^((?!(testOutputTreeClassificationAndLength)).)*$' \
      || ret=1

    $cmd %{_bindir}/phpunit8 \
      --testsuite api\
      --filter '^((?!(testOutOfOrderTextEdits|testOverlappingTextEdits)).)*$' \
      || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
