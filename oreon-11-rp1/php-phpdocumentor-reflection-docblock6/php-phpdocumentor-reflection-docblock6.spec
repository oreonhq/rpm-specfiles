%global source0_hash 9e86a4eb66bd331101f722f49d01c2893fdcbf5cd567ff2e2142c526981604a0
%global gh_commit    7bae67520aa9f5ecc506d646810bd40d9da54582
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global major        6
%bcond_without       tests
Name:           php-phpdocumentor-reflection-docblock%{major}
Version:        6.0.3
Release:        1%{?dist}
Summary:        DocBlock parser
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tar.gz
Source1:       makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.4
Requires:       php-filter
Requires:      (php-composer(phpdocumentor/type-resolver)     >= 2.0   with php-composer(phpdocumentor/type-resolver)     < 3)
Requires:      (php-composer(webmozart/assert)                >= 1.9.1 with php-composer(webmozart/assert)                < 3)
Requires:      (php-composer(phpdocumentor/reflection-common) >= 2.2   with php-composer(phpdocumentor/reflection-common) < 3)
Requires:      (php-composer(phpstan/phpdoc-parser)           >= 2.0   with php-composer(phpstan/phpdoc-parser)           < 3)
Requires:      (php-composer(doctrine/deprecations)           >= 1.1   with php-composer(doctrine/deprecations)           < 2)
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}
# oreon:deps
BuildRequires:  (php-composer(doctrine/deprecations) >= 1.1 with php-composer(doctrine/deprecations) < 2)
BuildRequires:  (php-composer(mockery/mockery) >= 1.6 with php-composer(mockery/mockery) < 2)
BuildRequires:  (php-composer(phpdocumentor/reflection-common) >= 2.2 with php-composer(phpdocumentor/reflection-common) < 3)
BuildRequires:  (php-composer(phpdocumentor/type-resolver) >= 2.0 with php-composer(phpdocumentor/type-resolver) < 3)
BuildRequires:  (php-composer(phpstan/phpdoc-parser) >= 2.0 with php-composer(phpstan/phpdoc-parser) < 3)
BuildRequires:  (php-composer(webmozart/assert) >= 1.9.1 with php-composer(webmozart/assert) < 3)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
The ReflectionDocBlock component of phpDocumentor provides a DocBlock
parser that is fully compatible with the PHPDoc standard.

With this component, a library can provide support for annotations via
DocBlocks or otherwise retrieve information that is embedded in a DocBlock.

Autoloader: %{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

sed 's#vendor/mockery/mockery/library/Mockery#%{_datadir}/php/Mockery1#' phpunit.xml.dist \
    > phpunit.xml

# single directory tree
mv src/*php      src/DocBlock/
mv src/Exception src/DocBlock/

%build

phpab \
  --template fedora \
  --output src/DocBlock/autoload.php \
  src/
cat << 'AUTOLOAD' | tee -a src/DocBlock/autoload.php
$deps = [
    '%{_datadir}/php/Webmozart/Assert/autoload.php',
];
if (PHP_VERSION_ID > 80200) {
    array_unshift($deps, '%{_datadir}/php/Webmozart/Assert2/autoload.php');
}
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/phpDocumentor/Reflection/TypeResolver2/autoload.php',
    '%{_datadir}/php/phpDocumentor/Reflection2/autoload-common.php',
    $deps,
    '%{_datadir}/php/PHPStan/PhpDocParser/autoload.php',
    '%{_datadir}/php/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD
%install
mkdir -p            %{buildroot}%{_datadir}/php/phpDocumentor/Reflection
cp -pr src/DocBlock %{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}
%oreon_autofiles main

%check

%if %{with tests}
sed -e '/autoload.php/d' -i docs/examples/*.php
phpab \
  --template fedora \
  --output bootstrap.php \
  tests/unit tests/integration
cat <<BOOTSTRAP | tee -a bootstrap.php
\Fedora\Autoloader\Dependencies::required([
    '%{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock%{major}/autoload.php',
    '%{_datadir}/php/Mockery1/autoload.php',
]);
BOOTSTRAP
RETURN_CODE=0
for PHP_EXEC in "php %{phpunit}" php82 php83 php84 php85; do
    if which $PHP_EXEC; then
        set $PHP_EXEC
        $1 -d auto_prepend_file=$PWD/bootstrap.php \
            ${2:-%{_bindir}/phpunit9} \
                --bootstrap bootstrap.php \
                --filter '^((?!(testDescriptionsCanEscapeAtSignsAndClosingBraces)).)*$' \
                --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
