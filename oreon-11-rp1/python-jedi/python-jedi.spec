%global source0_hash c3f4ccbd276696f4b19c54618d4fb18f9fc24b0aef02acf704b23f487daa1011
Name:           python-jedi
Version:        0.20.0
Release:        1%{?dist}
Summary:        An autocompletion tool for Python that can be used for text editors.
License:        MIT
URL:            https://jedi.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/j/jedi/jedi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jedi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jedi
Summary:        An autocompletion tool for Python that can be used for text editors.
%description -n python3-jedi

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jedi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jedi usr/lib/python3*/site-packages/jedi* usr/lib64/python3*/site-packages/jedi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jedi* usr/lib64/python3*/site-packages/jedi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jedi -f %{oreon_filedir}/python3-jedi.list

%changelog

%autochangelog
