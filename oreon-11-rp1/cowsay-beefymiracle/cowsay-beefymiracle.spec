%global source0_hash 211dd37622d1629c6c6b82522bdc20c22f62a179888d72353c4e0fe193c4a454
%global cowpathdir %{_sysconfdir}/cowsay/cowpath.d
%global pkgcowsdir %{_datadir}/%{name}/cows
Name:           cowsay-beefymiracle
Version:        1.0
Release:        1%{?dist}
Summary:        Cowsay file for the Beefy Miracle
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://rrix.fedorapeople.org/beefsay
Source0:        http://rrix.fedorapeople.org/beefsay/beefymiracle.cow
Requires:       cowsay >= 3.7.0-6
BuildArch:      noarch
# oreon:deps
BuildRequires:  cowsay
# /oreon:deps
%description
Provides a cowsay file for His Holiness the Beefy Miracle. It can be invoked
using cowsay -f beefymiracle, or aliased appropriately.

%prep

mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

cd %{name}-%{version}
echo "%{pkgcowsdir}" > %{name}.path
sed -e 's,/bin/env perl,/usr/bin/perl,g' %{SOURCE0} > beefymiracle.cow
%install
cd %{name}-%{version}
rm -rf %{buildroot}
install -d -m 0755              %{buildroot}%{cowpathdir}
install -p -m 0644 %{name}.path %{buildroot}%{cowpathdir}
install -d -m 0755                  %{buildroot}%{pkgcowsdir}
install -p -m 0644 beefymiracle.cow %{buildroot}%{pkgcowsdir}
%oreon_autofiles main

%check

export COWPATH=%{buildroot}%{pkgcowsdir}
echo "Installation (probably) successful" | cowsay -f beefymiracle
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
