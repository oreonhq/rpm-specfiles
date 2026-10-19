%global source0_hash 14ef735dc103632ecabc2791a88b3ef3966da47e1e785d2545fbb6b9dfba4a44
%global github_owner     php-fig
%global github_name      http-message
%global github_version   2.0
%global github_commit    cb6ce4845ce34a8ad9e68117c10ee90a29919eba
%global composer_vendor  psr
%global composer_project http-message
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Common interface for HTTP messages (PSR-7)
Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz
BuildArch:     noarch
Requires:      php(language) >= 7.2
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
This package holds all interfaces/classes/traits related to PSR-7 [1].

Note that this is not a HTTP message implementation of its own. It is merely an
interface that describes a HTTP message. See the specification for more details.

Autoloader: %{phpdir}/Psr/Http/Message/autoload.php

[1] http://www.php-fig.org/psr/psr-7/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build

: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
%install
mkdir -p %{buildroot}%{phpdir}/Psr/Http/Message
cp -rp src/* %{buildroot}%{phpdir}/Psr/Http/Message/
%oreon_autofiles main

%check

: Test autoloader
php -r '
require "%{buildroot}%{phpdir}/Psr/Http/Message/autoload.php";
exit (interface_exists("Psr\\Http\\Message\\UriInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
