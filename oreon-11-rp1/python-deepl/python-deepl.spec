%global source0_hash 3016bf86f1f53eb6e5fedb458746c6bf6579a840b57c54a2ed701b0344bc79e1
Name:           python-deepl
Version:        1.32.0
Release:        1%{?dist}
Summary:        Python library for the DeepL API.
License:        MIT
URL:            https://github.com/DeepLcom/deepl-python
Source0:        https://files.pythonhosted.org/packages/source/d/deepl/deepl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-deepl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-deepl
Summary:        Python library for the DeepL API.
%description -n python3-deepl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir deepl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-deepl usr/lib/python3*/site-packages/deepl* usr/lib64/python3*/site-packages/deepl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/deepl* usr/lib64/python3*/site-packages/deepl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-deepl -f %{oreon_filedir}/python3-deepl.list

%changelog

%autochangelog
