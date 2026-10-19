%global source0_hash 2298cf81afd0e3db3a783536fcf4d8279f3bf2e56d1ad89cc35dc1b85abfdc71
%global gh_commit    c129708154852656aabb13d8606cd5b12dbbabac
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     apereo
%global gh_project   phpCAS
Name:           php-pear-CAS
Version:        1.6.2
Release:        1%{?dist}
Summary:        Central Authentication Service client library in php
License:        Apache-2.0
URL:            https://wiki.jasig.org/display/CASC/phpCAS
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
Requires:       php(language) >= 7.1
Requires:       php-curl
Requires:       php-dom
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires:      (php-composer(psr/log) >= 1.0.0 with php-composer(psr/log) < 4)
%else
Requires:       php-PsrLog
%endif
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-session
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-pear(__uri/CAS) = %{version}
Provides:       php-composer(jasig/phpcas) = %{version}
Provides:       php-composer(apereo/phpcas) = %{version}
Provides:       phpCAS = %{version}-%{release}
# oreon:deps
BuildRequires:  (php-composer(psr/log) >= 1.0.0 with php-composer(psr/log) < 4)
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This package is a PEAR library for using a Central Authentication Service.

Autoloader: %{pear_phpdir}/CAS/Autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab \
    --template fedora \
    --output source/CAS/Autoload.php  \
             source
cat << 'EOF' | tee -a source/CAS/Autoload.php
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__) . '/CAS.php',
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF
%install
mkdir -p %{buildroot}%{pear_phpdir}
cp -pr source/* %{buildroot}%{pear_phpdir}/
%oreon_autofiles main

%check

: Ensure our autoloader works
php -r '
require "%{buildroot}%{pear_phpdir}/CAS/Autoload.php";
if (!class_exists("phpCAS")) {
  echo "Class not found\n";
  exit(1);
}
if (phpCAS::getVersion() != "%{version}") {
  echo "Bad version (found=" . phpCAS::getVersion()  . ", expected=%{version})\n";
  exit(1);
}
echo "Ok\n";
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
