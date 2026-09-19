%global source0_hash 8bf59ea0b2774478d757c7f0b256d1cb19b62aace29791565f260cbc29febcd0

%global pypi_name varint

Name:          python-%{pypi_name}
Version:       1.0.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic varint implementation in python
License:       MIT
URL:           https://github.com/fmoo/%{name}
# No license file in PyPi tarball.
# Upstream bug - https://github.com/fmoo/python-varint/issues/7
Source:        %{url}/archive/%{version}/varint-%{version}.tar.gz
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
%autochangelog
