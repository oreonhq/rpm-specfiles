%global source0_hash none

%global         pypi_name       pygmtools
%global         forgeurl        https://github.com/Thinklab-SJTU/pygmtools
Version:        0.5.5
%global         tag             %{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        3%{?dist}
Summary:        A library of Python graph matching solvers

License:        MulanPSL-2.0
URL:            https://pygmtools.readthedocs.io/en/latest/
Source:         %{forgesource}

BuildRequires:  python3-devel
# Documentation
#BuildRequires:  python3-sphinx
#BuildRequires:  python3-sphinx-design
#BuildRequires:  python3-sphinx-gallery
# Need to package m2r2
#BuildRequires:  python3-m2r2
BuildArch: noarch

%global _description %{expand:
pygmtools (Python Graph Matching Tools) provides graph matching
solvers in Python.

Graph matching is a fundamental yet challenging problem in pattern
recognition, data mining, and others. Graph matching aims to find
node-to-node correspondence among multiple graphs, by solving an
NP-hard combinatorial optimization problem.

Doing graph matching in Python used to be difficult, and this library
wants to make researchers' lives easier.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation files for %{pypi_name}

%prep
%forgeautosetup -p 1
# Remove for now, but maybe needed when Pytorch is available
rm -f %{pypi_name}/astar/priority_queue.hpp

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
#sphinx-build -b man -D plot_gallery=0 -b man docs man1

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Only check import of main module, as other modules
# have dependencies that may not be available
%pyproject_check_import -t pygmtools

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc docs/guide/*.rst
%doc examples

%changelog
%autochangelog
