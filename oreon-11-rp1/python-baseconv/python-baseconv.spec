%global source0_hash 0539f8bd0464013b05ad62e0a1673f0ac9086c76b43ebf9f833053527cd9931b
%global pypi_name baseconv
Name:          python-%{pypi_name}
Version:       1.2.2
Release:        1%{?dist}
BuildArch:     noarch
Summary:        A basic baseconv implementation in python
License:       PSF-2.0
URL:           https://github.com/semente/%{name}
VCS:           git:%{url}.git
Source0:        https://files.pythonhosted.org/packages/source/p/python-baseconv/python-baseconv-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-baseconv = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:        A basic baseconv implementation in python
%description -n python3-%{pypi_name}
%{summary}.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/baseconv* usr/lib64/python3*/site-packages/baseconv* usr/bin/*

%files
%files -n python3-baseconv -f %{oreon_filedir}/python3-baseconv.list

%changelog

%autochangelog
