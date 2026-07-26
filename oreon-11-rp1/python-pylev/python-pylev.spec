%global source0_hash 063910098161199b81e453025653ec53556c1be7165a9b7c50be2f4d57eae1c3

%global pypi_name pylev

%{?python_enable_dependency_generator}

%global common_description %{expand:
A pure Python Levenshtein implementation that’s not freaking GPL’d.

Based off the Wikipedia code samples at
https://en.wikipedia.org/wiki/Levenshtein_distance.}

Name:           python-%{pypi_name}
Summary:        Liberally licensed, pure Python Levenshtein implementation
Version:        1.3.0
Release:        28%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            http://github.com/toastdriven/pylev
Source0:        %{pypi_source}

# Include LICENSE file from upstream repository
Source1:        https://raw.githubusercontent.com/toastdriven/pylev/master/LICENSE

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE

%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
