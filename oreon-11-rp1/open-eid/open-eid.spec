%global source0_hash none
Name:           open-eid
Version:        17.12
Release:        1%{?dist}
Summary:        Meta-package for Estonian Electronic Identity Software
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.ria.ee
BuildArch:      noarch
Requires:       qdigidoc
Requires:       web-eid
Provides:       estonianidcard = %{version}-%{release}
Obsoletes:      estonianidcard <= 3.12.0-2
# oreon:deps

# /oreon:deps
%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running ID-card utilities.

%prep

%setup -c -T

%build

%install

%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
