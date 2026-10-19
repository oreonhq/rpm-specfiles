%global source0_hash 260c2774686e651b79f8b8e7fc9d80b3599ea6a66334b47d5f4abb69fc2c0ea1
Name:           python-pure-eval
Version:        0.2.4
Release:        1%{?dist}
Summary:        Safely evaluate AST nodes without side effects
License:        MIT
URL:            http://github.com/alexmojaki/pure_eval
Source0:        https://files.pythonhosted.org/packages/source/p/pure_eval/pure_eval-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 41
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-pure-eval = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pure-eval
Summary:        Safely evaluate AST nodes without side effects
%description -n python3-pure-eval

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pure_eval-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pure-eval usr/lib/python3*/site-packages/pure_eval* usr/lib64/python3*/site-packages/pure_eval* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pure_eval* usr/lib64/python3*/site-packages/pure_eval* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pure-eval -f %{oreon_filedir}/python3-pure-eval.list

%changelog

%autochangelog
