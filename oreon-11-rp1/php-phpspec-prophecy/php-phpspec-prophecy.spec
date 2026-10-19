%global source0_hash 24abbfe5276a0a4136cb5a51955e63871248f7cea3ae45d4a4bfa26e5af7f418
%global gh_commit    0da07c10d5fe64cd0c748f0523b47599400f2ed1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   prophecy
%bcond_without       tests
%bcond_with          phpspec
Name:           php-phpspec-prophecy
Version:        1.26.1
Release:        1%{?dist}
Summary:        Highly opinionated mocking framework for PHP
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%if %{with phpspec}
%endif
%endif
Requires:       php(language) >= 8.2
Requires:       (php-composer(phpdocumentor/reflection-docblock) >= 5.2   with php-composer(phpdocumentor/reflection-docblock) < 7)
Requires:       (php-composer(sebastian/comparator)              >= 3.0   with php-composer(sebastian/comparator)              < 9)
Requires:       (php-composer(sebastian/recursion-context)       >= 3.0   with php-composer(sebastian/recursion-context)       < 9)
Requires:       (php-composer(doctrine/instantiator)             >= 1.2   with php-composer(doctrine/instantiator)             < 3)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(phpspec/prophecy) = %{version}
# oreon:deps
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.2 with php-composer(doctrine/instantiator) < 3)
BuildRequires:  (php-composer(phpdocumentor/reflection-docblock) >= 5.2 with php-composer(phpdocumentor/reflection-docblock) < 7)
BuildRequires:  (php-composer(sebastian/comparator) >= 3.0 with php-composer(sebastian/comparator) < 9)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 3.0 with php-composer(sebastian/recursion-context) < 9)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit11
BuildRequires:  phpunit12
BuildRequires:  phpunit13
# /oreon:deps
%description
Prophecy is a highly opinionated yet very powerful and flexible PHP object
mocking framework.

Though initially it was created to fulfil phpspec2 needs, it is flexible enough
to be used inside any testing framework out there with minimal effort.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/Prophecy/autoload.php src
cat << 'EOF' | tee -a src/Prophecy/autoload.php
if (PHP_VERSION_ID > 80400) {
	$inst = [
        '%{_datadir}/php/Doctrine/Instantiator2/autoload.php',
        '%{_datadir}/php/Doctrine/Instantiator/autoload.php',
    ];
} else {
	$inst = '%{_datadir}/php/Doctrine/Instantiator/autoload.php';
}
\Fedora\Autoloader\Dependencies::required([
    $inst,
    [
        '%{_datadir}/php/phpDocumentor/Reflection/DocBlock6/autoload.php',
        '%{_datadir}/php/phpDocumentor/Reflection/DocBlock5/autoload.php',
    ],
]);
if (!class_exists('SebastianBergmann\\Comparator\\Comparator')) { // v2 from phpunit, v1 from phpspec
	$inst = [
        '%{_datadir}/php/SebastianBergmann/Comparator6/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Comparator5/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Comparator4/autoload.php',
        '%{_datadir}/php/SebastianBergmann/Comparator3/autoload.php',
	];
	if (PHP_VERSION_ID > 80300) {
		array_unshift($inst, '%{_datadir}/php/SebastianBergmann/Comparator7/autoload.php');
	}
	if (PHP_VERSION_ID > 80400) {
		array_unshift($inst, '%{_datadir}/php/SebastianBergmann/Comparator8/autoload.php');
	}
    \Fedora\Autoloader\Dependencies::required([$inst]);
}
if (!class_exists('SebastianBergmann\\RecursionContext\\Context')) { // v2 from phpunit, v1 from phpspec
    $inst = [
            '%{_datadir}/php/SebastianBergmann/RecursionContext6/autoload.php',
            '%{_datadir}/php/SebastianBergmann/RecursionContext5/autoload.php',
            '%{_datadir}/php/SebastianBergmann/RecursionContext4/autoload.php',
            '%{_datadir}/php/SebastianBergmann/RecursionContext3/autoload.php',
    ];
	if (PHP_VERSION_ID > 80300) {
		array_unshift($inst, '%{_datadir}/php/SebastianBergmann/RecursionContext7/autoload.php');
	}
	if (PHP_VERSION_ID > 80400) {
		array_unshift($inst, '%{_datadir}/php/SebastianBergmann/RecursionContext8/autoload.php');
	}
    \Fedora\Autoloader\Dependencies::required([$inst]);
}
// from https://github.com/symfony/deprecation-contracts
if (!function_exists('trigger_deprecation')) {
    function trigger_deprecation(string $package, string $version, string $message, mixed ...$args): void
    {
        @trigger_error(($package || $version ? "Since $package $version: " : '').($args ? vsprintf($message, $args) : $message), \E_USER_DEPRECATED);
    }
}
EOF
%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php
%oreon_autofiles main

%check

%if %{with tests}
: Dev autoloader
mkdir vendor
phpab --output vendor/autoload.php fixtures tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{_datadir}/php/Prophecy/autoload.php';
EOF
: check autoloader
php %{buildroot}%{_datadir}/php/Prophecy/autoload.php
%if %{with phpspec}
: check phpspec
phpspec --version
%endif
ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=vendor/autoload.php \
       %{_bindir}/phpunit11 \
         || ret=1
  fi
done
if [ -x %{_bindir}/phpunit12 ]; then
for cmd in php php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=vendor/autoload.php \
       %{_bindir}/phpunit12 \
         || ret=1
  fi
done
fi
if [ -x %{_bindir}/phpunit13 ]; then
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=vendor/autoload.php \
       %{_bindir}/phpunit13 \
         || ret=1
  fi
done
fi
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
