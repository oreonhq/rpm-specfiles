%global source0_hash 825e2b5d9144c5491d9c353511169a1595813e6a1ad203faf7525cd2d1d1828e

%global pypi_name pylast

Name:		%{pypi_name}
Version:	7.0.2
Release:	%autorelease
Summary:	Python interface to Last.fm API compatible social networks
License:	Apache-2.0
URL:		https://github.com/pylast/pylast
VCS:		git:%{url}.git
Source0:	%{pypi_source %{pypi_name}}
BuildArch:	noarch
BuildSystem:	pyproject
BuildOption(install):	-l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
