%global source0_hash 7dc7d8f23d11e539427e7b8e3afa70353e159c16f703bad6dd082cc6cdfeeaa8
Name:           python-application-properties
Version:        0.9.3
Release:        1%{?dist}
Summary:        A simple, easy to use, unified manner of accessing program properties.
License:        MIT
URL:            https://application_properties.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/a/application_properties/application_properties-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-application-properties = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-application-properties
Summary:        A simple, easy to use, unified manner of accessing program properties.
%description -n python3-application-properties

%prep
%global oreon_srcdir application_properties-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-application-properties usr/lib/python3*/site-packages/application_properties* usr/lib64/python3*/site-packages/application_properties* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/application_properties* usr/lib64/python3*/site-packages/application_properties* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-application-properties -f %{oreon_filedir}/python3-application-properties.list

%changelog

%autochangelog
