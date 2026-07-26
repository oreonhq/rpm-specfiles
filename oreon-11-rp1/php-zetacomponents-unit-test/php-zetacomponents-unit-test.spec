%global source0_hash 12a410e1c1b0b17a33ecae49246e0139d35db11b4767a1fb5514d39c58c95a10

# remirepo/fedora spec file for php-zetacomponents-unit-test
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    179fd95f1ed1292a5fb639a89f482dfce2038758
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   UnitTest
%global cname        unit-test
%global ezcdir       %{_datadir}/php/ezc

Name:           php-%{gh_owner}-%{cname}
Version:        1.2.6
Release:        4%{?dist}
Summary:        Zeta UnitTest Component

License:        Apache-2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel

# From phpcompatinfo report for 1.0.2
Requires:       php(language) > 5.3
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       phpunit9
# Also use Exception for Base, skipped to avoid circular dep.
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}

%description
UnitTest is an internal component which extends PhpUnit to facilitate test
running and reports of the components themselves.

For this reason, there is no tutorial for this component. If you really want
to use it for some reason it's sane to expect some community support on IRC or
the mailing list.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate a simple autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoloader.php \
   src

%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: The library
cp -pr src \
       %{buildroot}%{ezcdir}/%{gh_project}
: For ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload

%files
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%doc docs design
%dir %{ezcdir}
%dir %{ezcdir}/autoload
     %{ezcdir}/autoload/*_autoload.php
     %{ezcdir}/%{gh_project}

%changelog
%autochangelog
