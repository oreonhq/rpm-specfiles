%global source0_hash bd4551d38dad85e0f61ecdf45c63d7800c6cd15dfaad0305b7f2411c75a2844a
%bcond_without       tests
%global pear_name    Cache_Lite
%global gh_commit    fc7c6703cfbddc55c80c5ae3926dcc80c1d993f9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     pear
%global gh_project   Cache_Lite
Summary:        Fast and Safe little cache system for PHP
Name:           php-pear-Cache-Lite
Version:        2.0.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language)  >= 7.4
Requires:       php-autoloader(pear/pear-core-minimal) >= 1.10
Requires:       php-date
Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/cache_lite) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-autoloader(pear/pear-core-minimal)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
# /oreon:deps
%description
This package is a little cache system optimized for file containers. It is
fast and safe (because it uses file locking and/or anti-corruption tests).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate classmap autoloader
phpab --template fedora --output Cache/Lite/autoload.php Cache
cat << 'EOF' | tee -a Cache/Lite/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{pear_phpdir}/PEAR/autoload.php',
]);
EOF
%install
mkdir -p     %{buildroot}%{pear_phpdir}/
cp -pr Cache %{buildroot}%{pear_phpdir}/Cache
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
ln -s %{buildroot}%{pear_phpdir}/Cache/Lite/autoload.php vendor/autoload.php
: Upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
%endif
%post

if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
