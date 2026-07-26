%global source0_hash 2d34f6e4d90476473fe4ec5ff0a7a6f2dde3e2f30f2ec950d005cc11842f0843

# remirepo/fedora spec file for php-google-recaptcha
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    56522c261d2e8c58ba416c90f81a4cd9f2ed89b9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     google
%global gh_project   recaptcha
%global with_tests   0%{!?_without_tests:1}
%global psr0         ReCaptcha

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.3.1
Release:        3%{?dist}
Summary:        reCAPTCHA PHP client library

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to retrieve test suite
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 8
BuildRequires:  php-curl
BuildRequires:  php-json
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^10",
#        "friendsofphp/php-cs-fixer": "^3.14",
#        "php-coveralls/php-coveralls": "^2.5"
BuildRequires:  phpunit10
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=8"
Requires:       php(language) >= 8
# From phpcompatinfo report for 1.2.1
Requires:       php-curl
Requires:       php-json
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
reCAPTCHA PHP client library.

reCAPTCHA is a free CAPTCHA service that protect websites from spam and abuse.
This is Google authored code that provides plugins for third-party integration
with reCAPTCHA.

See https://www.google.com/recaptcha/

Autoloader: %{_datadir}/php/%{psr0}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
rm src/autoload.php

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/%{psr0}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{psr0}\\', __DIR__);
AUTOLOAD

%install
: Library
mkdir -p           %{buildroot}%{_datadir}/php
cp -pr src/%{psr0} %{buildroot}%{_datadir}/php/%{psr0}

%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{_datadir}/php/%{psr0}/autoload.php
ret=0

for cmdarg in php php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit10} \
      -d date.timezone=UTC  \
      --bootstrap=$BOOTSTRAP \
      --no-coverage || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/%{psr0}

%changelog
%autochangelog
