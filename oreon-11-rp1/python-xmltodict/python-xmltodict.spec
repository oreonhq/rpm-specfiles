%global source0_hash 6d94c9f834dd9e44514162799d344d815a3a4faec913717a9ecbfa5be1bb8e61
Name:           python-xmltodict
Version:        1.0.4
Release:        1%{?dist}
Summary:        Makes working with XML feel like you are working with JSON
License:        MIT
URL:            https://github.com/martinblech/xmltodict
Source0:        https://files.pythonhosted.org/packages/source/x/xmltodict/xmltodict-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-xmltodict = %{version}-%{release}
# /oreon:deps
%package -n       python3-xmltodict+test
Summary:        Metapackage for python3-xmltodict test extras
Requires:       python3-xmltodict = %{version}-%{release}
Provides:       python3dist(xmltodict[test]) = %{version}-%{release}

%description -n python3-xmltodict+test
Metapackage for python3-xmltodict test extras.

%description

%package -n     python3-xmltodict
Summary:        Makes working with XML feel like you are working with JSON
%description -n python3-xmltodict

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xmltodict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xmltodict usr/lib/python3*/site-packages/xmltodict* usr/lib64/python3*/site-packages/xmltodict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xmltodict* usr/lib64/python3*/site-packages/xmltodict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xmltodict -f %{oreon_filedir}/python3-xmltodict.list

%changelog

%autochangelog

