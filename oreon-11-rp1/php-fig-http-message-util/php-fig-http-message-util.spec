%global source0_hash bda66b01e233240ebad21b2726b792f75eee46fd37449d4e8fb0be873aed994f
%global gh_commit    9d94dc0154230ac39e5bf89398b324a86f63f765
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-message-util
%global pk_owner     fig
%global pk_project   %{gh_project}
Name:           php-%{pk_owner}-%{pk_project}
Version:        1.1.5
Release:        1%{?dist}
Summary:        PSR Http Message Util
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
Requires:       php(language) > 5.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Recommends:     php-composer(psr/http-message)
%endif
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
BuildRequires:  php-cli
BuildRequires:  php-composer(fedora/autoloader)
# /oreon:deps
%description
This library holds utility classes and constants to facilitate common
operations of PSR-7; the primary purpose is to provide constants for
referring to request methods, response status codes and messages, and
potentially common headers.

Autoloader: %{_datadir}/php/Fig/Http/Message/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

cat << 'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{pk_owner}/%{pk_project} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Fig\\Http\\Message\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional(array(
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
));
AUTOLOAD
%install
mkdir -p   %{buildroot}%{_datadir}/php/Fig/Http
cp -pr src %{buildroot}%{_datadir}/php/Fig/Http/Message
%oreon_autofiles main

%check

php -r '
require "%{buildroot}%{_datadir}/php/Fig/Http/Message/autoload.php";
$ok = interface_exists("Fig\\Http\\Message\\StatusCodeInterface");
echo "Autoload " . ($ok ? "Ok\n" : "fails\n");
exit ($ok ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
