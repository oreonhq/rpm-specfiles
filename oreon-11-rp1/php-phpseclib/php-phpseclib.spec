%global source0_hash aa7869104990ab51bb758421810730944abdce89f0f0e37845cfe6e33fa33e9b

%global composer_vendor         phpseclib
%global composer_project        phpseclib

%global github_owner            phpseclib
%global github_name             phpseclib
%global github_commit           2552c4001631d1cc844332faea6a08a49c964b28
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%bcond_without                  tests

Name:       php-%{composer_vendor}
Version:    2.0.52
Release:    1%{?dist}
Summary:    PHP Secure Communications Library
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_name}

Source0:    %{name}-%{version}-%{github_short}.tgz
Source1:    %{name}-autoload.php
# Generate a full archive from git snapshot, with tests
Source2:    makesrc.sh

BuildArch:      noarch

%if %{with tests}
BuildRequires:  php-composer(fedora/autoloader)
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
%else
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global phpunit %{_bindir}/phpunit6
%else
%global phpunit %{_bindir}/phpunit
%endif
%endif
BuildRequires:  %{phpunit}
BuildRequires:  %{_bindir}/phpab
# Optional at runtime, to avoid too muck skipped tests
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
BuildRequires:  php-mcrypt
%endif

Requires:   php(language) >= 5.3.3
Requires:   php-bcmath
Requires:   php-date
Requires:   php-gmp
Requires:   php-hash
Requires:   php-mcrypt
Requires:   php-openssl
Requires:   php-pcre
Requires:   php-session
Requires:   php-standard
Requires:   php-xml
# Autoloader
Requires:   php-composer(fedora/autoloader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
MIT-licensed pure-PHP implementations of an arbitrary-precision integer 
arithmetic library, fully PKCS#1 (v2.1) compliant RSA, DES, 3DES, RC4, 
Rijndael, AES, Blowfish, Twofish, SSH-1, SSH-2, SFTP, and X.509

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}
cp %{SOURCE1} %{composer_vendor}/autoload.php

%build

%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr %{composer_vendor} %{buildroot}%{_datadir}/php

%if %{with tests}
%check
%{_bindir}/phpab --output tests/bootstrap.php tests
cat << 'EOF' | tee -a tests/bootstrap.php
if (class_exists("PHPUnit_Framework_TestCase") && !class_exists("PHPUnit\\Framework\\TestCase")) {
     class_alias("PHPUnit_Framework_TestCase", "PHPUnit\\Framework\\TestCase");
}
if (class_exists("PHPUnit_Framework_Error_Notice") && !class_exists("PHPUnit\Framework\Error\Notice")) {
     class_alias("PHPUnit_Framework_Error_Notice", "PHPUnit\Framework\Error\Notice");
}
require "%{buildroot}%{_datadir}/php/%{composer_vendor}/autoload.php";
date_default_timezone_set('UTC');
EOF

# from travis/run-phpunit.sh
if %{phpunit} --atleast-version 8
then
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/n setUpBeforeClass()/n setUpBeforeClass(): void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/n setUp()/n setUp(): void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/n tearDown()/n tearDown(): void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/\(n assertIsArray([^)]*)\)/\1: void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/\(n assertIsString([^)]*)\)/\1: void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/\(n assertStringContainsString([^)]*)\)/\1: void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/\(n assertStringNotContainsString([^)]*)\)/\1: void/g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/^class Unit_Crypt_\(AES\|Hash\|RSA\)_/class /g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/^class Unit_File_\(X509\)_/class /g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/^class Unit_Math_\(BigInteger\)_/class /g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/^class Unit_\(Crypt\|File\|Math\|Net\)_/class /g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/^class Functional_Net_/class /g'
    find tests -type f -name "*.php" -print0 | xargs -0 sed -i 's/extends Unit_Crypt_Hash_\(SHA512Test\|SHA256Test\)/extends \1/g'
fi

# avoid already defined class
sed -e '/require /d' -i tests/Unit/Crypt/Hash/SHA*_96Test.php

# testAuthorityInfoAccess fails without internet access
ret=0
for cmd in "php %{phpunit}" php80 php81 php82 php83 php84 php85; do
  if which $cmd; then
    set $cmd
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit9} \
       --filter '^((?!(testAuthorityInfoAccess|testVectors|testKeySizes|testOpenSSHEncrypted)).)*$' \
       --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%{_datadir}/php/%{composer_vendor}
%doc AUTHORS CHANGELOG.md composer.json README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE

%changelog
%autochangelog
