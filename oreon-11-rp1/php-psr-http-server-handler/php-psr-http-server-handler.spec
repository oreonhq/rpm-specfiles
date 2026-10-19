%global source0_hash 237d4340f756dcea0d4ba6ddaed44550cc2c04e414c11642433eee75b5565c57
%global gh_commit    84c4fb66179be4caaf8e97bd239203245302e7d4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-server-handler
%global pk_vendor    psr
%global pk_project   %{gh_project}
%global ns_vendor    Psr
%global ns_project   Http
%global ns_sub       Server
Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Common interface for HTTP server-side request handler
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz
BuildArch:      noarch
Requires:       php(language) >= 7.0
Requires:      (php-composer(%{pk_vendor}/http-message) >= 1.0  with php-composer(%{pk_vendor}/http-message) < 3)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 3)
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
This repository holds the RequestHandlerInterface related to PSR-15
(HTTP Server Request Handlers).

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-15/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

%build

: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Http/Message2/autoload.php',
        '%{_datadir}/php/Psr/Http/Message/autoload.php',
    ],
]);
EOF
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}
%oreon_autofiles main

%check

: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\%{ns_sub}\\RequestHandlerInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
