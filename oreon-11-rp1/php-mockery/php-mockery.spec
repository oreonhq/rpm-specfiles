%global source0_hash none

#
# Fedora spec file for php-deepend-Mockery
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%bcond_without       tests

%global gh_commit    1f4efdd7d3beafe9807b08156dfcb176d18f1699
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     mockery
%global gh_project   mockery
%global ns_project   Mockery
%global major        1

Name:           php-mockery
Version:        1.6.12
Release:        5%{?dist}
Summary:        Mockery is a simple but flexible PHP mock object framework

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Use our autoloader
Patch0:         %{gh_project}-tests.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.3
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5 || ^9.6.17",
#        "symplify/easy-coding-standard": "^12.1.4"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.6.17
BuildRequires: (php-composer(hamcrest/hamcrest-php) >= 2.0.1 with php-composer(hamcrest/hamcrest-php) < 3)
BuildRequires:  php-pdo
# Autoloader
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.3",
#        "lib-pcre": ">=7.0",
#        "hamcrest/hamcrest-php": "~2.0"
Requires:       php(language) >= 7.3
Requires:      (php-composer(hamcrest/hamcrest-php) >= 2.0.1 with php-composer(hamcrest/hamcrest-php) < 3)
# From phpcompatinfo report for version 1.4.2
Requires:       php-pcre
Requires:       php-spl
Requires:       php-reflection
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(mockery/mockery) = %{version}

%description
Mockery is a simple but flexible PHP mock object framework for use in unit 
testing. It is inspired by Ruby's flexmock and Java's Mockito, borrowing 
elements from both of their APIs.

Autoloader: %{_datadir}/php/%{ns_project}%{major}/autoload.php

%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv library/*.php library/%{ns_project}/
phpab --template fedora --output library/%{ns_project}/autoload.php library

cat << 'EOF' | tee -a library/%{ns_project}/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '/usr/share/php/Hamcrest2/autoload.php',
    __DIR__ . '/helpers.php',
]);
EOF

%patch -P0 -p0 -b .rpm

rm -f docs/.gitignore

%build
# Empty build section, most likely nothing required.

%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp library/%{ns_project} %{buildroot}/%{_datadir}/php/%{ns_project}%{major}

%check
%if %{with tests}
: Use installed tree and our autoloader
export COMPOSER_VENDOR_DIR=%{buildroot}%{_datadir}/php/%{ns_project}%{major}

phpab --output tests/classmap.php --exclude */SemiReservedWordsAsMethods.php tests/Mockery tests/Fixture

: Run upstream test suite
ret=0

# need investigation
rm tests/Mockery/MockeryCanMockClassesWithSemiReservedWordsTest.php

for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md docs
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}

%changelog
%autochangelog
