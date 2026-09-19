%global source0_hash 32f0f6671fedb0dd4571217e13a504c738cf1920a9d0b59ab34907428fa62414

# Created by pyp2rpm-3.3.10
%global pypi_name trampoline
%global pypi_version 0.1.2

%global forgeurl https://gitlab.com/ferreum/trampoline

# No tags, go by inspection of git repo
# commit 1d98f39c3015594e2ac8ed48dccc2f393b4dd82b
# Author: Daniel K <code.danielk@gmail.com>
# Date:   Sat Aug 18 03:00:11 2018 +0200
#
#    version 0.1.2
#
%global commit 1d98f39c3015594e2ac8ed48dccc2f393b4dd82b
%global date 20180818

%forgemeta

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Simple and tiny yield-based trampoline implementation

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

%description
 trampoline - unlimited recursion Simple and tiny yield-based trampoline
implementation for python. --This trampoline allows recursive functions to
recurse virtually (or literally) infinitely. Most existing recursive functions
can be converted with simple modifications.The implementation is tiny: the gist
of the module consists of a single function with around 30 lines of simple
python...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 trampoline - unlimited recursion Simple and tiny yield-based trampoline
implementation for python. --This trampoline allows recursive functions to
recurse virtually (or literally) infinitely. Most existing recursive functions
can be converted with simple modifications.The implementation is tiny: the gist
of the module consists of a single function with around 30 lines of simple
python...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import
%pytest

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
