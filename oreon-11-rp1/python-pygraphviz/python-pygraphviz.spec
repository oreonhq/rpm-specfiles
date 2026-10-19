%global source0_hash e3a0a0da443af50277f98de0a73932a8f3fc3dc39685911e94b58111e153a8cc
Name:           python-pygraphviz
Version:        2.0.2
Release:        1%{?dist}
Summary:        Python interface to Graphviz
License:        BSD-3-Clause
URL:            https://pygraphviz.github.io
Source0:        https://files.pythonhosted.org/packages/source/p/pygraphviz/pygraphviz-%{version}.tar.gz
Patch0:         graphviz-13.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78
BuildRequires:  python3dist(swig) > 4.1.0
Requires:       python3-pygraphviz = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygraphviz
Summary:        Python interface to Graphviz
%description -n python3-pygraphviz

%prep
%global oreon_srcdir pygraphviz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygraphviz usr/lib/python3*/site-packages/pygraphviz* usr/lib64/python3*/site-packages/pygraphviz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygraphviz* usr/lib64/python3*/site-packages/pygraphviz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygraphviz -f %{oreon_filedir}/python3-pygraphviz.list

%changelog

%autochangelog
