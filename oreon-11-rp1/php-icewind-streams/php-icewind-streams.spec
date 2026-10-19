%global source0_hash 2866d333dd4eabb5055409cfaa9806c9bc27651ef82921ff971040692697b559
%global gh_commit    cb2bd3ed41b516efb97e06e8da35a12ef58ba48b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   Streams
%global pk_vendor    icewind
%global pk_name      streams
%global ns_vendor    Icewind
%global ns_name      Streams
Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.7.8
Release:        1%{?dist}
Summary:        A set of generic stream wrappers
License:        MIT AND AGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
Requires:       php(language) >= 7.1
Requires:       php-hash
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(theseer/autoload)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
# /oreon:deps
%description
Generic stream wrappers for php.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}
%oreon_autofiles main

%check

cd tests
: Generate a simple autoloader for test suite
%{_bindir}/phpab --output bootstrap.php .
echo "require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php';" >> bootstrap.php
: Run the test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
