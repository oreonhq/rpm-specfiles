%global source0_hash cc9df4a26a0e84d0b326ccbf8fb1502c39a09c81ade0599ab51d5b92356ad933
%global gh_commit    815bbbc963cf35e5413df195aa29df58243ecd24
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   git
%global php_home     %{_datadir}/php/SebastianBergmann
%global pear_name    Git
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:1}%{!?_without_tests:0}
Name:           php-phpunit-git
Version:        2.1.4
Release:        21%{?dist}
Summary:        Simple wrapper for Git
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://%{gh_project}hub.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz
BuildArch:      noarch
Requires:       git
Requires:       php(language) >= 5.3.3
Requires:       php-date
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(sebastian/git) = %{version}
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Obsoletes:      php-phpunit-Git < 1.2.0-3
Provides:       php-phpunit-Git = %{version}-%{release}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
Simple PHP wrapper for Git.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab \
  --template fedora \
  --output src/autoload.php \
  src
%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{pear_name}
%oreon_autofiles main

%post

if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
