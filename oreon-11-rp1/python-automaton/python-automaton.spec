%global source0_hash 3896d03d328b52e341b7dd13c3e3963f0da44ac88a160ac07e761a087ddaa7e3
Name:           python-automaton
Version:        3.5.0
Release:        1%{?dist}
Summary:        Friendly state machines for Python.
License:        Apache-2.0
URL:            https://docs.openstack.org/automaton
Source0:        https://files.pythonhosted.org/packages/source/a/automaton/automaton-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-automaton = %{version}-%{release}
# /oreon:deps
%package -n       python3-automaton+pydot
Summary:        Metapackage for python3-automaton pydot extras
Requires:       python3-automaton = %{version}-%{release}
Requires:       python3dist(pydot) >= 4.0
Provides:       python3dist(automaton[pydot]) = %{version}-%{release}

%description -n python3-automaton+pydot
Metapackage for python3-automaton pydot extras.

%description

%package -n     python3-automaton
Summary:        Friendly state machines for Python.
%description -n python3-automaton

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir automaton-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-automaton usr/lib/python3*/site-packages/automaton* usr/lib64/python3*/site-packages/automaton* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/automaton* usr/lib64/python3*/site-packages/automaton* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-automaton -f %{oreon_filedir}/python3-automaton.list

%changelog

%autochangelog
