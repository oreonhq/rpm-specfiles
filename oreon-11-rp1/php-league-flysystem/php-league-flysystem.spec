%global source0_hash 21c638106a85daaee4b9562d8547ef8a6b98e0319fcc1ca8c17997ab5e7cb822
%global gh_commit    3239285c825c152bcc315fe0e87d6b55f5972ed1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   flysystem
%global pk_vendor    league
%global pk_name      flysystem
%global ns_vendor    League
%global ns_project   Flysystem
Name:           php-%{pk_vendor}-%{pk_name}
Version:        3.36.0
Release:        1%{?dist}
Summary:        Filesystem abstraction: Many filesystems, one API
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
Requires:       php(language) >= 7.2.5
Requires:       php-fileinfo
Requires:      (php-composer(league/mime-type-detection) >= 1.3   with php-composer(league/mime-type-detection) < 2)
Requires:       php-date
Requires:       php-ftp
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(league/mime-type-detection) >= 1.3 with php-composer(league/mime-type-detection) < 2)
BuildRequires:  php(language)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-fileinfo
BuildRequires:  php-ftp
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit8
# /oreon:deps
%description
Flysystem is a filesystem abstraction which allows you to easily swap out
a local filesystem for a remote one.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/MimeTypeDetection/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
%oreon_autofiles main

%check

: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
// Test suite
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Stub\\', dirname(__DIR__).'/stub');
EOF
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
   : Run upstream test suite
   $cmd %{_bindir}/phpunit8 \
     --exclude-group integration \
     --filter '^((?!(testPathinfoHandlesUtf8|testStreamSizeForUrl)).)*$' \
     --no-coverage --verbose || ret=1
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
