%global source0_hash ae0064d4ae00cfa7fb5363592914fb3573dcf8bf1f608794b499c53e4f698b57

# remirepo/fedora spec file for php-phpdocumentor-reflection-common2
#
# Copyright (c) 2017-2025 Remi Collet, Shawn Iwinski
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      ReflectionCommon
%global github_version   2.2.0
%global github_commit    1d01c49d4ed62f25aa84a747ad35d5a16924662b

%global composer_vendor  phpdocumentor
%global composer_project reflection-common

%global major            2

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       16%{?github_release}%{?dist}
Summary:       Common reflection classes used by phpdocumentor

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# GitHub export does not include tests.
# Run makesrc.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       makesrc.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
%endif
## Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.0)
# only pcre and spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Common reflection classes used by phpdocumentor to reflect the code structure.

Autoloader: %{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-common.php src

%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor
cp -rp src %{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}

%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php
mkdir vendor
touch vendor/autoload.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php81 php82 php83 php84; do
    if which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=$BOOTSTRAP \
            %{_bindir}/phpunit9 --no-coverage || RETURN_CODE=1
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
%doc composer.json
%dir %{phpdir}/phpDocumentor
%dir %{phpdir}/phpDocumentor/Reflection%{major}
     %{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Element.php
     %{phpdir}/phpDocumentor/Reflection%{major}/File.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Fqsen.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Location.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Project.php
     %{phpdir}/phpDocumentor/Reflection%{major}/ProjectFactory.php

%changelog
%autochangelog
