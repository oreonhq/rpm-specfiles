%global source0_hash 7c89d51f50d2068e5f3d84085dd04586ab98f480f9c97ecc927285a11d2e41be

%{?python_enable_dependency_generator}
%global pypi_name gTTS-token
# Needs access to Google Services so doesn't run in koji
%global with_tests 0

Name:           gtts-token
Version:        1.1.4
Release:        21%{?dist}
Summary:        Calculates a token to run the Google Translate text to speech
License:        MIT
URL:            https://github.com/boudewijn26/gTTS-token
Source0:        https://github.com/Boudewijn26/gTTS-token/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(requests)
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

%description
gTTS-token (Google Text to Speech token): A python implementation of the token 
validation of Google Translate

%package -n python3-gtts-token
Summary:  Python 3 lib to Calculates a token to run the Google Translate text to speech
%{?python_provide:%python_provide python3-gtts-token}

%description -n python3-gtts-token
gTTS-token (Google Text to Speech token): A python implementation of the token 
validation of Google Translate

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gtts_token

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-gtts-token -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
