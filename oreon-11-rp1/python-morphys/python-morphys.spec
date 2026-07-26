%global source0_hash 58b423108a8ab0e54d8ca031753e2b3b70f40692a32c91c60924804199028bb2

%global git_commit 0642a71126c32cd26b3a443a5cac27e4e1f7240f
%global pypi_name morphys
%global common_description %{expand:
Smart conversions between unicode and bytes types for common cases in python.}

Name:          python-%{pypi_name}
Version:       1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Smart conversions between unicode and bytes types
License:       MPL-2.0
URL:           https://github.com/mkalinski/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{url}/archive/%{git_commit}/morphys-1.0.tar.gz
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{git_commit}
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
%python3 ./tests.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
