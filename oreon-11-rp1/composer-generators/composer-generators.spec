%global source0_hash none
Name:           composer-generators
Version:        0.1.2
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://git.remirepo.net/cgit/rpms/composer-generators.git/
Summary:        Tools for composer enabled applications packager
Source0:        composer.prov
Source1:        composer.attr
Source10:       LICENSE
Source11:       NEWS
BuildArch:      noarch
Requires:       php-cli
# oreon:deps
BuildRequires:  php-cli
# /oreon:deps
%description
This package provides RPM generators which are used for
getting provides from composer enabled applications.

* find main project name and provide it
* find bundled libraries and provide them

%prep

%setup -c -T
cp -a %{sources} .

%install
install -Dpm 755 composer.prov %{buildroot}%{_rpmconfigdir}/composer.prov
install -Dpm 644 composer.attr %{buildroot}%{_fileattrsdir}/composer.attr
%oreon_autofiles main

%check

: Syntax check only
%{_bindir}/php -l %{buildroot}%{_rpmconfigdir}/composer.prov
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
