%global source0_hash 0fafc3201c046e72913abb8a7a2b75cb17c3e15ebdd3ed546adf8fe9a9d4f54e
Name:           python-pipdeptree
Version:        4.2.5
Release:        1%{?dist}
Summary:        Command line utility to show dependency tree of packages.
License:        MIT
URL:            https://github.com/tox-dev/pipdeptree
Source0:        https://files.pythonhosted.org/packages/source/p/pipdeptree/pipdeptree-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson) >= 1.12
BuildRequires:  python3dist(meson-python) >= 0.21
BuildRequires:  python3dist(ninja) >= 1.13.2
Requires:       python3-pipdeptree = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pipdeptree
Summary:        Command line utility to show dependency tree of packages.
# oreon:reqs
Requires:       python3dist(nab) >= 0.0.17
Requires:       python3dist(nab-index) >= 0.0.17
Requires:       python3dist(nab-project) >= 0.0.17
# /oreon:reqs
%description -n python3-pipdeptree

%prep
%global oreon_srcdir pipdeptree-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pipdeptree usr/lib/python3*/site-packages/pipdeptree* usr/lib64/python3*/site-packages/pipdeptree* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pipdeptree* usr/lib64/python3*/site-packages/pipdeptree* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pipdeptree -f %{oreon_filedir}/python3-pipdeptree.list

%changelog

%autochangelog
