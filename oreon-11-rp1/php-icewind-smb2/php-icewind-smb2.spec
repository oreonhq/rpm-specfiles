%global source0_hash 6b4d9571c3a05e96071f9df8da2ea633aafb9efc1abee29a908028be06f248cc

# remirepo/fedora spec file for php-icewind-smb2
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    464459aa5d4ab6bd59f13b4455c8fc3558bb6e07
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   SMB
# Packagist information
%global pk_vendor    icewind
%global pk_name      smb
# Namespace information
%global ns_vendor    Icewind
%global ns_name      SMB
# API version, for parallel installation
%global major        2
# Test suite requires a Samba server and configuration file
#   yum install samba
#   systemctl start smb
#   systemctl start nmb
#   useradd testsmb
#   install -o testsmb -m 755 -d /home/testsmb/test
#   smbpasswd -a testsmb
#   create php-icewind-smb-config.json using config.json from sources
%global with_tests   0%{?_with_tests:1}

Name:           php-%{pk_vendor}-%{pk_name}%{major}
Version:        2.0.7
Release:        16%{?dist}
Summary:        php wrapper for smbclient and libsmbclient-php

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
%if %{with_tests}
# Can't be provided, contains credential
Source2:        %{name}-config.json
%endif

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-composer(%{pk_vendor}/streams) >= 0.2
BuildRequires:  php-date
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-posix
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^4.8"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8
BuildRequires:  php-composer(theseer/autoload)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.4"
#        "icewind/streams": ">=0.2.0"
Requires:       php(language) >= 5.4
Requires:       php-composer(%{pk_vendor}/streams) >= 0.2
# From phpcompatinfo report for version 2.0.2
Requires:       %{_bindir}/smbclient
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-posix
# Autoloader
Requires:       php-composer(fedora/autoloader)
%if 0%{?fedora} > 21
Recommends:     php-smbclient
%endif

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
PHP wrapper for smbclient and libsmbclient-php

* Reuses a single smbclient instance for multiple requests
* Doesn't leak the password to the process list
* Simple 1-on-1 mapping of SMB commands
* A stream-based api to remove the need for temporary files
* Support for using libsmbclient directly trough libsmbclient-php

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for icewind/smb and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Icewind\\SMB\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Icewind/Streams/autoload.php',
]);
EOF

%build
# Empty build section, most likely nothing required.

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}

%if %{with_tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Icewind\\SMB\\Test\\', dirname(__DIR__) . '/tests');
EOF

cd tests
: Client configuration
cp %{SOURCE2} config.json

: Run the test suite
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc composer.json
%doc *.md example.php
%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}

%changelog
%autochangelog
