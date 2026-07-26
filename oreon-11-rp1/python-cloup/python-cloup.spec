%global source0_hash c852e0a0541aa433c6ab31a9b8b503f63d9881e91ddaf0384d6927965f2b421c

##
## This package does not build docs due to the fact that the documents
## have heavy dependencies on packages not in Fedora and based around
## python-3.8. An initial look at fixing this was beyond the scope of
## the initial packagers skills (2024-11-05).

%{?!python3_pkgversion:%global python3_pkgversion 3}

%global modname cloup
%global srcname %{modname}
%global pypi_name %{modname}
%global forgeurl https://github.com/janLuke/%{pypi_name}
%global version0 3.0.7
%forgemeta

%global desc CLOUP extends Click with options

Name:           python-%{srcname}
Version:        %{version0}
Release:        %{autorelease}_00
Summary:        %{desc}
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{pypi_source}
# Patches go here

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{desc}

Library to build command line interfaces based on Click. It extends
click with: option groups, constraints (e.g. mutually exclusive
params), command aliases, help themes, "did you mean ...?" suggestions
and more.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:

%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import -t
%tox

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
