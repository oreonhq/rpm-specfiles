%global source0_hash e0c8731e00568bd6999bd25dff5071514517d7869b94b5e3c9ea2f4fda59e31b
%global gh_commit    2d6702ff215bf922936ccc1ad31007edc76451b9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   mime-type-detection
%global pk_vendor    league
%global pk_name      mime-type-detection
%global ns_vendor    League
%global ns_project   MimeTypeDetection
Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.17.0
Release:        1%{?dist}
Summary:        Mime-type detection for Flysystem
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%global phpunit %{_bindir}/phpunit10
Requires:       php(language) >= 7.4
Requires:       php-fileinfo
Requires:       php-json
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-fileinfo
BuildRequires:  php-json
BuildRequires:  phpunit10
# /oreon:deps
%description
This package supplies a generic mime-type detection interface with a finfo
based implementation.

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
EOF
sed -e 's/PHPStan\\Testing\\TestCase/PHPUnit\\Framework\\TestCase/' -i src/OverridingExtensionToMimeTypeMapTest.php
: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit10} \
      --filter '^((?!(the_generated_map_should_be_up_to_date)).)*$' \
      --no-coverage \
      || ret=1
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
