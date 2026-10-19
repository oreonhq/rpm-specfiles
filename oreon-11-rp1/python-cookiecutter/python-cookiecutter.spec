%global source0_hash ca7bb7bc8c6ff441fbf53921b5537668000e38d56e28d763a1b73975c66c6138
Name:           python-cookiecutter
Version:        2.7.1
Release:        1%{?dist}
Summary:        A command-line utility that creates projects from project templates, e.g. creating a Python package project from a Python package project template.
License:        ...
URL:            https://github.com/cookiecutter/cookiecutter
Source0:        https://files.pythonhosted.org/packages/source/c/cookiecutter/cookiecutter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cookiecutter = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cookiecutter
Summary:        A command-line utility that creates projects from project templates, e.g. creating a Python package project from a Python package project template.
# oreon:reqs
Requires:       python3dist(binaryornot) >= 0.4.4
Requires:       python3dist(click) < 9.0.0
Requires:       python3dist(click) >= 7.0
Requires:       python3dist(jinja2) < 4.0.0
Requires:       python3dist(jinja2) >= 2.7
Requires:       python3dist(python-slugify) >= 4.0.0
Requires:       python3dist(pyyaml) >= 5.3.1
Requires:       python3dist(requests) >= 2.23.0
# /oreon:reqs
%description -n python3-cookiecutter

%prep
%global oreon_srcdir cookiecutter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cookiecutter usr/lib/python3*/site-packages/cookiecutter* usr/lib64/python3*/site-packages/cookiecutter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cookiecutter* usr/lib64/python3*/site-packages/cookiecutter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cookiecutter -f %{oreon_filedir}/python3-cookiecutter.list

%changelog

%autochangelog
