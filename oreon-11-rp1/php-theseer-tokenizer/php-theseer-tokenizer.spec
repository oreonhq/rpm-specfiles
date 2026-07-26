%global source0_hash 84b2c157a9dcb6afd8647a1ab55ca4239d985995bb1bcad4699c37aaef15ad27

# remirepo/fedora spec file for php-theseer-tokenizer
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    b7489ce515e168639d17feec34b8847c326b0b3c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_vendor    theseer
%global gh_project   tokenizer
%global ns_vendor    TheSeer
%global ns_project   Tokenizer

Name:           php-%{gh_vendor}-%{gh_project}
Version:        1.3.1
Release:        2%{?dist}
Summary:        Library for converting tokenized PHP source code into XML

License:        BSD-3-Clause
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-xmlwriter
BuildRequires:  php-dom
BuildRequires:  php-tokenizer
BuildRequires:  php-pcre
BuildRequires:  php-spl
%if %{with tests}
# Tests
BuildRequires:  phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# From composer.json, "require": {
#    "php": "^7.0 || ^8.0",
#    "ext-xmlwriter": "*",
#    "ext-dom": "*",
#    "ext-tokenizer": "*"
Requires:       php(language) >= 7.0
Requires:       php-xmlwriter
Requires:       php-dom
Requires:       php-tokenizer
# From phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_vendor}/%{gh_project}) = %{version}

%description
A small library for converting tokenized PHP source code into XML
and potentially other formats.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate a simple classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%if %{with tests}
%check
ret=0
for cmdarg in php php81 php82 php83 php84 php85; do
  if which $cmdarg; then
      $cmdarg -d auto_prepend_file=%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php \
        %{_bindir}/phpunit9 \
          --no-coverage --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
