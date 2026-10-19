%global source0_hash d50daab1f123259ce57bdfb40dea3f3092d32b7dab65a97c0cc7f2699c7f6f95
%global gh_commit    4d8778e1c7d405cbb471574821c1ff5b68cc8f57
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-http
%global gh_project   message-factory
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    Http
%global ns_project   Message
Name:      %{pk_vendor}-%{pk_project}
Version:   1.1.0
Release:        8%{?dist}
Summary:        Factory interfaces for PSR-7 HTTP Message
License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:   makesrc.sh
BuildArch: noarch
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
Requires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
%else
Requires:  php-psr-http-message
%endif
Requires:   php-composer(fedora/autoloader)
Provides:   php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 3)
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
Factory interfaces for PSR-7 HTTP Message.

Documentation: http://docs.php-http.org/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

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
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
%oreon_autofiles main

%check

: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\RequestFactory") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
