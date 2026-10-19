%global source0_hash f8593801fcea340dfbd2a46965206a013acbf356a88f680553de6decaaa9f7eb
%global gh_commit    ea2f4014f163c1be4c601b9b7bd6af81ba8d701c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Seldaek
%global gh_project   phar-utils
Name:           php-seld-phar-utils
Version:        1.2.2
Release:        1%{?dist}
Summary:        PHAR file format utilities
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(seld/phar-utils) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
PHAR file format utilities, for when PHP phars you up.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/Seld/PharUtils/autoload.php';

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab --template fedora --output src/autoload.php src

%build

%install
mkdir -p     %{buildroot}%{_datadir}/php/Seld/PharUtils/
cp -pr src/* %{buildroot}%{_datadir}/php/Seld/PharUtils/
%oreon_autofiles main

%check

: Check if our autoloader works
php -r '
require "%{buildroot}%{_datadir}/php/Seld/PharUtils/autoload.php";
$a = new \Seld\PharUtils\Timestamps("%{SOURCE1}");
echo "Ok\n";
exit(0);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
