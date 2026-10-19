%global source0_hash a31bdedf4d950deee6d94c81173361190f5628895769c6a0ddeae77606e1f3ab
%global gh_commit    fe695ec993e0a55c3abdda10a9364eb31c6f1bf0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     bovigo
%global gh_project   vfsStream
%global pk_owner     mikey179
%global pk_project   vfsstream
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
Name:           php-%{pk_owner}-%{pk_project}
Version:        1.6.12
Release:        1%{?dist}
Summary:        PHP stream wrapper for a virtual file system
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-date
Requires:       php-dom
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
Requires:       php-xml
Requires:       php-zip
Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
Provides:       php-composer(%{pk_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(yoast/phpunit-polyfills) >= 2.0 with php-composer(yoast/phpunit-polyfills) < 3)
BuildRequires:  /usr/bin/phpab
BuildRequires:  php(language)
BuildRequires:  phpunit9
# /oreon:deps
%description
vfsStream is a PHP stream wrapper for a virtual file system that may be
helpful in unit tests to mock the real file system.

It can be used with any unit test framework, like PHPUnit or SimpleTest.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate autoloader
%{_bindir}/phpab \
    --output src/main/php/org/bovigo/vfs/autoload.php \
             src/main/php/org/bovigo/vfs
%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr src/main/php/org %{buildroot}%{_datadir}/php/org
%oreon_autofiles main
%if %{with_tests}
%check

rm src/test/php/org/bovigo/vfs/vfsStreamWrapperLargeFileTestCase.php
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/org/bovigo/vfs/autoload.php';
require_once '%{_datadir}/php/Yoast/PHPUnitPolyfills2/autoload.php';
EOF
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    VER=$($cmd -r 'echo PHP_VERSION_ID;')
    $cmd %{_bindir}/phpunit9 \
      --filter '^((?!(unregisterThirdPartyVfsScheme|unregisterWhenNotInRegisteredState)).)*$' \
      --verbose --no-coverage || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
