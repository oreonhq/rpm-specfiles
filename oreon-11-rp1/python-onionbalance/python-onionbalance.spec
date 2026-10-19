%global source0_hash 4574d496aff03661593cae0157bb5c7e6b9e54f2ef3c15986e9075dee60ce396
Name:           python-onionbalance
Version:        0.2.4
Release:        1%{?dist}
Summary:        Onionbalance provides load-balancing and redundancy for Tor hidden services by distributing requests to multiple backend Tor instances.
License:        GPL
URL:            https://gitlab.torproject.org/tpo/onion-services/onionbalance/
Source0:        https://files.pythonhosted.org/packages/source/o/onionbalance/onionbalance-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-onionbalance-fix-versioneer.patch
Patch1:         drop-dependency-on-future.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-onionbalance = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-onionbalance
Summary:        Onionbalance provides load-balancing and redundancy for Tor hidden services by distributing requests to multiple backend Tor instances.
%description -n python3-onionbalance

%prep
%global oreon_srcdir onionbalance-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-onionbalance usr/lib/python3*/site-packages/onionbalance* usr/lib64/python3*/site-packages/onionbalance* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/onionbalance* usr/lib64/python3*/site-packages/onionbalance* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-onionbalance -f %{oreon_filedir}/python3-onionbalance.list

%changelog

%autochangelog
