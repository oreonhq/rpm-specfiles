%global source0_hash df8775122b5df1bae157af38beb1da6919aeb4d01bdea27388716bbb33f45ac0
%bcond_without   tests
%global github_owner     twigphp
%global github_name      Twig
%global github_version   1.44.7
%global github_commit    0887422319889e442458e48e2f3d9add1a172ad5
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global composer_vendor  twig
%global composer_project twig
%global php_min_ver 7.2.5
%{!?phpdir:      %global phpdir      %{_datadir}/php}
%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}
Name:          php-%{composer_project}
Version:       %{github_version}
Release:        6%{?dist}
Summary:        The flexible, fast, and secure template engine for PHP
License:       BSD
URL:           http://twig.sensiolabs.org
Source0:        %{name}-%{version}-%{github_short}.tgz
Source1:       makesrc.sh
BuildArch: noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Obsoletes:     php-twig-Twig < %{version}-%{release}
Provides:      php-twig-Twig = %{version}-%{release}
Provides:      php-pear(pear.twig-project.org/Twig) = %{version}
Obsoletes:     php-channel-twig < 1.4
# oreon:deps
BuildRequires:  (php-composer(psr/container) >= 1.0 with php-composer(psr/container) < 2)
BuildRequires:  (php-composer(symfony/debug) >= 3.4 with php-composer(symfony/debug) < 4)
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-devel
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-hash
BuildRequires:  php-iconv
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-spl
# /oreon:deps
%description
%{summary}.

* Fast: Twig compiles templates down to plain optimized PHP code. The
  overhead compared to regular PHP code was reduced to the very minimum.

* Secure: Twig has a sandbox mode to evaluate untrusted template code. This
  allows Twig to be used as a template language for applications where users
  may modify the template design.

* Flexible: Twig is powered by a flexible lexer and parser. This allows the
  developer to define its own custom tags and filters, and create its own
  DSL.

Autoloader: %{phpdir}/Twig/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Move the PSR-4 compat library
mv src lib/Twig/psr4

: Create lib autoloader
phpab --template fedora --output lib/Twig/autoload.php lib

%build

: nothing
%install
: PSR-0 and PSR-4 Libraries
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/
%oreon_autofiles main

%check

: Library version check
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Twig/autoload.php";
    exit(version_compare("%{version}", Twig_Environment::VERSION, "=") ? 0 : 1);'
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Twig/autoload.php";
    exit(version_compare("%{version}", Twig\Environment::VERSION, "=") ? 0 : 1);'
%if %{with tests}
: Generate autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{phpdir}/Twig/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Twig\\Tests\\', dirname(__DIR__) . '/tests');
\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Symfony3/Component/Debug/autoload.php',
    '%{phpdir}/Psr/Container/autoload.php',
));
EOF
: Disable listener from symfony/phpunit-bridge # ^4.4.9|^5.0.9
sed -e '/listener/d' phpunit.xml.dist > phpunit.xml
: Test suite without extension
ret=0
for SCL in "php %{phpunit}" php74 php80 php81 php82; do
    if which $SCL; then
        set $SCL
        $1 ${2:-%{_bindir}/phpunit9} $SKIP \
          --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
