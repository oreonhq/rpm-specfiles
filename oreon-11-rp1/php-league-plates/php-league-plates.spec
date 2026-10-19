%global source0_hash 2999e06cff21f20e3472c60ad6662152a2ce03ff4c7147e2676a720e2bb2ca1a
%global gh_commit    12ee65166adbc6fb5916fb80b0c0758e49a2d996
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   plates
%global pk_vendor    league
%global pk_name      plates
%global ns_vendor    League
%global ns_project   Plates
Name:           php-%{pk_vendor}-%{pk_name}
Version:        3.6.0
Release:        1%{?dist}
Summary:        Native PHP template system
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
Requires:       php(language) >= 8.0
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(mikey179/vfsStream)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit10
# /oreon:deps
%description
Plates is a native PHP template system that's fast, easy to use and easy
to extend. It's inspired by the excellent Twig template engine and strives
to bring modern template language functionality to native PHP templates.
Plates is designed for developers who prefer to use native PHP templates
over compiled template languages, such as Twig or Smarty.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate classmap autoloader
phpab --template fedora --output src/autoload.php src
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
// Dependency
require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';
EOF
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 || ret=1
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
