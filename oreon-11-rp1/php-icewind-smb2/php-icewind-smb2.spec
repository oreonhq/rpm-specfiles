%global source0_hash 6b4d9571c3a05e96071f9df8da2ea633aafb9efc1abee29a908028be06f248cc
%global gh_commit    464459aa5d4ab6bd59f13b4455c8fc3558bb6e07
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   SMB
%global pk_vendor    icewind
%global pk_name      smb
%global ns_vendor    Icewind
%global ns_name      SMB
%global major        2
%global with_tests   0%{?_with_tests:1}
Name:           php-%{pk_vendor}-%{pk_name}%{major}
Version:        3.7.0
Release:        1%{?dist}
Summary:        php wrapper for smbclient and libsmbclient-php
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
%if %{with_tests}
Source2:        %{name}-config.json
%endif
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 5.4
Requires:       php-composer(%{pk_vendor}/streams) >= 0.2
Requires:       %{_bindir}/smbclient
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-posix
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}
# oreon:deps

# /oreon:deps
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

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}
%oreon_autofiles main
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
