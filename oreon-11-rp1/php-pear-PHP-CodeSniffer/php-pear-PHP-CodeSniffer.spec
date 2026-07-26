%global source0_hash 6ff98b5b007410e7bace4c6771f4dd6a06effc0557cbad7742ae1505ed809bed

# spec file for php-pear-PHP-CodeSniffer
#
# Copyright (c) 2013-2025 Remi Collet
# Copyright (c) 2009-2013 Christof Damian
# Copyright (c) 2006-2009 Konstantin Ryabitsev
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    0525c73950de35ded110cffafb9892946d7771b5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2025-11-10
%global gh_owner     PHPCSStandards
%global gh_project   PHP_CodeSniffer
# keep in old PEAR tree
%global pear_phpdir  %{_datadir}/pear

%global upstream_version 4.0.1
#global upstream_prever  rc1

Name:           php-pear-PHP-CodeSniffer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
Summary:        PHP coding standards enforcement tool

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite
Source0:        %{name}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tgz
Source1:        makesrc.sh

# RPM installation path
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
# 8.1 because of phpunit10
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlwriter
BuildRequires:  php-simplexml
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-intl
%if %{with tests}
BuildRequires:  php-bcmath
# to run test suite, from composer.json "require-dev"
#        "phpunit/phpunit": "^8.0 || ^9.3.4 || ^10.5.32 || ^11.3.3"
%global phpunit %{_bindir}/phpunit10
BuildRequires:  phpunit10 >= 10.5.32
%endif

# from composer.json "require": {
#        "php": ">=7.2.0",
#        "ext-tokenizer": "*",
#        "ext-xmlwriter": "*",
#        "ext-simplexml": "*"
Requires:       php(language) >= 7.2
Requires:       php-tokenizer
Requires:       php-xmlwriter
Requires:       php-simplexml
# From phpcompatinfo report for version 3.8.0
Requires:       php-dom
Requires:       php-iconv
Requires:       php-intl

Provides:       php-pear(%{gh_project}) = %{version}
Provides:       php-composer(squizlabs/php_codesniffer) = %{version}
Provides:       phpcs = %{version}
Obsoletes:      phpcs < %{version}

%description
PHP_CodeSniffer provides functionality to verify that code conforms to
certain standards, such as PEAR, or user-defined.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

%build
# Empty build section, 

%install
: Install the library
mkdir -p                %{buildroot}%{pear_phpdir}/PHP/CodeSniffer
cp -pr src              %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/src/
cp -pr autoload.php     %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -pr requirements.php %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -p  phpcs.xml.dist   %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/
cp -p  phpcs.xsd        %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/

: Cleanup
find %{buildroot}%{pear_phpdir}/PHP/CodeSniffer -depth -type d -name Tests -exec rm -r {} \; -print

: Install the commands
install -Dpm 755 bin/phpcs  %{buildroot}%{_bindir}/phpcs
install -Dpm 755 bin/phpcbf %{buildroot}%{_bindir}/phpcbf

%if %{with tests}
%check
# Fix current date
YEAR=$(date +%Y)
PREV=$(expr $YEAR - 1)
sed -e "/@copyright/s/${PREV}/${YEAR}/" \
    -i src/Standards/Squiz/Tests/Commenting/FileCommentUnitTest.1.*.fixed

# Version 4.0.0beta1: Tests: 3871, Assertions: 23018, PHPUnit Deprecations: 777, Skipped: 16.
# testBrokenRulesetMultiError failing reported as https://github.com/PHPCSStandards/PHP_CodeSniffer/issues/767
ret=0
for cmdarg in \
    "php   %{phpunit}" \
    "php81 %{_bindir}/phpunit10" \
    "php82 %{_bindir}/phpunit11" \
    "php83 %{_bindir}/phpunit11" \
    "php84 %{_bindir}/phpunit11" \
    "php85 %{_bindir}/phpunit11"
  do if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=-1 $2 \
       --filter '^((?!(testBrokenRulesetMultiError)).)*$' \
       --no-coverage || ret=1
  fi
done
exit $ret
%endif

%files
%license licence.txt
%doc *.md
%{pear_phpdir}/PHP
%{_bindir}/phpcbf
%{_bindir}/phpcs

%changelog
%autochangelog
