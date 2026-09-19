%global source0_hash 691c88649243544db717e7edf6a9831df112104e1aefb5f6038a5d071e8cf41d

%global pypi_name simpleaudio

%global pypi_description The simpleaudio module provides asynchronous, cross-platform, \
dependency-free audio playback capability for Python 3.

Name: python-%{pypi_name}
Summary: Simple, asynchronous audio playback module for Python 3
License: MIT

Version: 1.0.4
Release: 21%{?dist}

URL: https://github.com/hamiltron/py-simple-audio
Source0: %pypi_source

BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: python3-devel >= 3.3
BuildRequires: python3-setuptools

%description
%{pypi_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{pypi_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-*.egg-info/

%changelog
%autochangelog
