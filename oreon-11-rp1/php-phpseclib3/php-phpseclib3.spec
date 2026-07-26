%global source0_hash 3d8e150769e19de8c1bc15b0a40bcba3c76060320e9c0ee2113ab8ae57535f5b

%global composer_vendor         phpseclib
%global composer_project        phpseclib

%global github_owner            phpseclib
%global github_name             phpseclib
%bcond_without                  tests

Version:    3.0.50
Release:    1%{?dist}
%global vmajor %(v="%{version}"; v=(${v//./ }); echo "${v[0]}")

Name:       php-%{composer_project}%{vmajor}
Summary:    PHP Secure Communications Library
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_name}

Source0:    %{name}-%{version}.zip
# Generate a full archive from git tag, with tests
Source2:    makesrc.sh

BuildArch:      noarch

%global php_min_version 5.6.1
%define depends_on() %{expand:
Requires: %{*}

%if %{with tests}
BuildRequires: %{*}
%endif
}

%depends_on php-bcmath  >= %{php_min_version}
%depends_on php-gmp     >= %{php_min_version}
%depends_on php-mcrypt  >= %{php_min_version}
%depends_on php-openssl >= %{php_min_version}
%depends_on php-sodium  >= %{php_min_version}
%depends_on php-xml     >= %{php_min_version}
%depends_on php-composer(paragonie/constant_time_encoding)

BuildRequires:  php-fedora-autoloader-devel

%if %{with tests}
%global phpunit_bin %{_bindir}/phpunit9
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-cli >= %{php_min_version}
BuildRequires:  %{phpunit_bin}
%endif

# Autoloader
Requires:   php-composer(fedora/autoloader)
Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
MIT-licensed pure-PHP implementations of an arbitrary-precision integer 
arithmetic library, fully PKCS#1 (v2.1) compliant RSA, DES, 3DES, RC4, 
Rijndael, AES, Blowfish, Twofish, SSH-1, SSH-2, SFTP, and X.509

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
phpab \
	--template fedora \
	--output autoload.php \
	--basedir phpseclib/ \
	./composer.json
echo "require_once '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php';" >> autoload.php
cat autoload.php

%install
mkdir -p %{buildroot}%{_datadir}/php
cp -a %{composer_project} %{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}

cp autoload.php %{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}/autoload.php

%if %{with tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require "%{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('phpseclib3\\Tests\\', dirname(__DIR__) . "/tests");
date_default_timezone_set('UTC');
EOF

# avoid already defined class
sed -e 's/CreateKeyTest/RSACreateKeyTest/' -i tests/Unit/Crypt/RSA/CreateKeyTest.php
sed -e 's/CreateKeyTest/DSACreateKeyTest/' -i tests/Unit/Crypt/DSA/CreateKeyTest.php

# Not supported curves ? (need investigations)
rm tests/Unit/Crypt/EC/CurveTest.php

php tests/make_compatible_with_phpunit7.php
php tests/make_compatible_with_phpunit9.php

# from travis/run-phpunit.sh
# testAuthorityInfoAccess fails without internet access
# testCurveExistance as we remove some files
php -d memory_limit=1G %{phpunit_bin} \
	--filter '^((?!(testAuthorityInfoAccess|testCurveExistance|testLoginToInvalidServer)).)*$' \
	--verbose --configuration tests/phpunit.xml
%endif

%files
%doc AUTHORS CHANGELOG.md composer.json README.md
%license LICENSE
%{_datadir}/php/%{composer_project}%{vmajor}

%changelog
%autochangelog
