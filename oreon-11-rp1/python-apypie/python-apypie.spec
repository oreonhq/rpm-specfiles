%global source0_hash 52fae9d499f0f079113d3cc9af3cc3494c6aa9d42791dc243fbfad4799ede8ea
Name:           python-apypie
Version:        0.8.0
Release:        1%{?dist}
Summary:        Apipie bindings for Python
License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        https://files.pythonhosted.org/packages/source/a/apypie/apypie-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-apypie = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-apypie
Summary:        Apipie bindings for Python
%description -n python3-apypie

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir apypie-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apypie usr/lib/python3*/site-packages/apypie* usr/lib64/python3*/site-packages/apypie* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apypie* usr/lib64/python3*/site-packages/apypie* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apypie -f %{oreon_filedir}/python3-apypie.list

%changelog

%autochangelog
