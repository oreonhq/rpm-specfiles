%global source0_hash 7388a57e0df5b84b1e48622bd9eaed87d133f8042ea0f1348a1f7600bb1d61a9

#
# Fedora spec file for php-Monolog
#
# Copyright (c) 2012-2022 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Seldaek
%global github_name      monolog
%global github_version   1.27.1
%global github_commit    904713c5929655dc9b97288b69cfeedad610c9a1

%global composer_vendor  monolog
%global composer_project monolog

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psrlog_min_ver 1.0.1
%global psrlog_max_ver 2.0
# "sentry/sentry": "^0.13"
%global sentry_min_ver 0.13
%global sentry_max_ver 1.0
# "aws/aws-sdk-php": "^2.4.9 || ^3.0"
#     NOTE: Min version not 2.4.9 because autoloader required
%global aws_min_ver 2.8.13
%global aws_max_ver 4.0
# "swiftmailer/swiftmailer": "~5.3"
%global swift_min_ver 5.3
%global swift_max_ver 6

# Build using "--with tests" to disable tests
%bcond_with tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-Monolog
Version:   %{github_version}
Release:   10%{?dist}
Summary:   Sends your logs to files, sockets, inboxes, databases and various web services

License:   MIT
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Fix tests for sentry/sentry >= 0.16.0 (and < 1.0)
#
# Patch adapted for Monolog version 1.21.0 from
#     https://github.com/Seldaek/monolog/pull/880
Patch0:    %{name}-tests-sentry-gte-0-16-0.patch

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/log) >= %{psrlog_min_ver}
BuildRequires: php-composer(psr/log) <  %{psrlog_max_ver}
## optional
BuildRequires: php-composer(swiftmailer/swiftmailer) >= %{swift_min_ver}
BuildRequires: php-composer(swiftmailer/swiftmailer) <  %{swift_max_ver}
BuildRequires: php-composer(sentry/sentry) >= %{sentry_min_ver}
BuildRequires: php-composer(sentry/sentry) <  %{sentry_max_ver}
BuildRequires: php-composer(aws/aws-sdk-php) >= %{aws_min_ver}
BuildRequires: php-composer(aws/aws-sdk-php) <  %{aws_max_ver}
## phpcompatinfo (computed from version 1.22.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-xml
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/log) >= %{psrlog_min_ver}
Requires:      php-composer(psr/log) <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 1.22.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-json
Requires:      php-mbstring
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
Requires:      php-xml
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/log-implementation) = 1.0.0

# Removed sub-packages
Obsoletes:     %{name}-amqp   < %{version}-%{release}
Provides:      %{name}-amqp   = %{version}-%{release}
Obsoletes:     %{name}-dynamo < %{version}-%{release}
Provides:      %{name}-dynamo = %{version}-%{release}
Obsoletes:     %{name}-mongo  < %{version}-%{release}
Provides:      %{name}-mongo  = %{version}-%{release}
Obsoletes:     %{name}-raven  < %{version}-%{release}
Provides:      %{name}-raven  = %{version}-%{release}

# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-composer(aws/aws-sdk-php)
Suggests:      php-composer(sentry/sentry)
Suggests:      php-composer(swiftmailer/swiftmailer)
Suggests:      php-pecl(amqp)
Suggests:      php-pecl(mongo)
%endif

%description
Monolog sends your logs to files, sockets, inboxes, databases and various web
services. Special handlers allow you to build advanced logging strategies.

This library implements the PSR-3 [1] interface that you can type-hint against
in your own libraries to keep a maximum of interoperability. You can also use it
in your applications to make sure you can always use another compatible logger
at a later time.

[1] http://www.php-fig.org/psr/psr-3/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Fix tests for sentry/sentry >= 0.16.0
%patch -P0 -p1

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Monolog/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Monolog\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
));

\Fedora\Autoloader\Dependencies::optional(array(
    array(
        '%{phpdir}/Aws3/autoload.php',
        '%{phpdir}/Aws/autoload.php',
    ),
    '%{phpdir}/Raven/autoload.php',
    '%{phpdir}/Swift/swift_required.php',
));
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}
cp -pr src/Monolog %{buildroot}%{phpdir}/

%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Monolog/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Monolog\\', __DIR__ . '/tests/Monolog');
BOOTSTRAP

: Remove MongoDBHandlerTest because it requires a running MongoDB server
rm -f tests/Monolog/Handler/MongoDBHandlerTest.php

: Remove GitProcessorTest because it requires a git repo
rm -f tests/Monolog/Processor/GitProcessorTest.php

: Mocking issues
rm -f tests/Monolog/Handler/SocketHandlerTest.php

: Trying to access array offset on value of type null in Raven lib
rm -f tests/Monolog/Handler/RavenHandlerTest.php

: Skip tests known to fail
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
sed 's/function testThrowsOnInvalidEncoding/function SKIP_testThrowsOnInvalidEncoding/' \
    -i tests/Monolog/Formatter/NormalizerFormatterTest.php
%endif

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55 php56 php70 php71} php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc doc
%doc composer.json
%{phpdir}/Monolog

%changelog
%autochangelog
