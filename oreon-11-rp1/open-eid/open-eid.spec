%global source0_hash none

Name:           open-eid
Version:        17.12
Release:        23%{?dist}
Summary:        Meta-package for Estonian Electronic Identity Software

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.ria.ee
BuildArch:      noarch

Requires:       qdigidoc
Requires:       web-eid
Provides:       estonianidcard = %{version}-%{release}
Obsoletes:      estonianidcard <= 3.12.0-2

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running ID-card utilities.

%prep
%setup -c -T

%build

%install

%files

%changelog
%autochangelog
