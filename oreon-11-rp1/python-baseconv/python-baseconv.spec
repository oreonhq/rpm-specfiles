%global source0_hash 0539f8bd0464013b05ad62e0a1673f0ac9086c76b43ebf9f833053527cd9931b

%global pypi_name baseconv

Name:          python-%{pypi_name}
Version:       1.2.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic baseconv implementation in python
License:       PSF-2.0
URL:           https://github.com/semente/%{name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{name}}
BuildSystem:   pyproject
BuildOption(prep):    -n %{name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
