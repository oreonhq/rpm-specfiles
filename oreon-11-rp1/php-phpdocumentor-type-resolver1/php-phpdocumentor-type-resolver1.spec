%global source0_hash 4151c3146dd35e4e5d6c916e421ac75ac6187e80b140fbe61a5e76161b228e74
%global github_owner     phpDocumentor
%global github_name      TypeResolver
%global github_version   1.12.0
%global github_commit    92a98ada2b93d9b201a613cb5a33584dde25f195
%global composer_vendor  phpdocumentor
%global composer_project type-resolver
%global major            1
%global ns_major         2
%global php_min_ver 7.3
%global reflection_common_min_ver 2.0
%global reflection_common_max_ver 3
%global phpdoc_parser_min_ver 1.18
%global phpdoc_parser_max_ver 3
%global deprecations_min_ver 1.0
%global deprecations_max_ver 2
%bcond_without tests
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:        2%{?dist}
Summary:        A PSR-5 based resolver of Class names, Types and Structural Element Names
Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       makesrc.sh
BuildArch:     noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= %{php_min_ver}
Requires:      (php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver} with php-composer(phpdocumentor/reflection-common) < %{reflection_common_max_ver})
Requires:      (php-composer(phpstan/phpdoc-parser)           >= %{phpdoc_parser_min_ver}     with php-composer(phpstan/phpdoc-parser)           < %{phpdoc_parser_max_ver})
Requires:      (php-composer(doctrine/deprecations)           >= %{deprecations_min_ver}      with php-composer(doctrine/deprecations)           < %{deprecations_max_ver})
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(doctrine/deprecations) >= 1.0 with php-composer(doctrine/deprecations) < 2)
BuildRequires:  (php-composer(phpdocumentor/reflection-common) >= 2.0 with php-composer(phpdocumentor/reflection-common) < 3)
BuildRequires:  (php-composer(phpstan/phpdoc-parser) >= 1.18 with php-composer(phpstan/phpdoc-parser) < 3)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  phpunit9
# /oreon:deps
%description
The specification on types in DocBlocks (PSR-5) describes various keywords
and special constructs but also how to statically resolve the partial name
of a Class into a Fully Qualified Class Name (FQCN).

PSR-5 also introduces an additional way to describe deeper elements than
Classes, Interfaces and Traits called the Fully Qualified Structural Element
Name (FQSEN). Using this it is possible to refer to methods, properties and
class constants but also functions and global constants.

This package provides two Resolvers that are capable of:
1. Returning a series of Value Object for given expression while resolving any
  partial class names, and
2. Returning an FQSEN object after resolving any partial Structural Element
  Names into Fully Qualified Structural Element names.

Autoloader: %{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Update examples autoload require
sed "s#.*require.*vendor.*/autoload.php.*#require_once '%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php';#" \
    -i examples/*

%build

: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-type-resolver.php src
cat <<'AUTOLOAD' | tee -a src/autoload-type-resolver.php
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-common.php',
    '%{phpdir}/PHPStan/PhpDocParser/autoload.php',
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD
%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}
cp -rp src/* %{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}/
%oreon_autofiles main

%check

%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php';
\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\Reflection\\', __DIR__.'/tests/unit');
BOOTSTRAP
: Upstream tests
RETURN_CODE=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84 php85; do
    if which $cmdarg; then
        set $cmdarg
        $1 -d auto_prepend_file=$PWD/bootstrap.php \
            ${2:-%{_bindir}/phpunit9} --verbose --no-coverage --bootstrap bootstrap.php \
            --testsuite=unit \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
