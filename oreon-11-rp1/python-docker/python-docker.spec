%global source0_hash ad8c70e6e3f8926cb8a92619b832b4ea5299e2831c14284663184e200546fa6c

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
# Disable python2 build by default
%bcond_with python2
%else
%bcond_with python3
%bcond_without python2
%endif

%global srcname docker

Name:           python-%{srcname}
Version:        7.1.0
Release:        10%{?dist}
Summary:        A Python library for the Docker Engine API
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        A Python library for the Docker Engine API
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python%{?fedora:2}-setuptools
Obsoletes:      python-docker-py < 1:2

%description -n python2-%{srcname}
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.
%endif # with python2

%if %{with python3}
%package -n python3-%{srcname}
Summary:        A Python library for the Docker Engine API
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
Obsoletes:      python3-docker-py < 1:2

%description -n python3-%{srcname}
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.
%endif # with_python3

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info ssh}

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -fr docker.egg-info

%build
%if %{with python2}
%py2_build
%endif # with python2

%if %{with python3}
%pyproject_wheel
%endif # with_python3

%install
%if %{with python2}
%py2_install
%endif # with python2

%if %{with python3}
%pyproject_install
%pyproject_save_files docker
%endif # with_python3

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%endif # with python2

%if %{with python3}
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%endif # with_python3

%changelog
%autochangelog
