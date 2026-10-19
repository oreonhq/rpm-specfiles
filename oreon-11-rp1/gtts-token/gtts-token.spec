%global source0_hash 7c89d51f50d2068e5f3d84085dd04586ab98f480f9c97ecc927285a11d2e41be
%{?python_enable_dependency_generator}
%global pypi_name gTTS-token
%global with_tests 0
Name:           gtts-token
Version:        1.1.4
Release:        1%{?dist}
Summary:        Calculates a token to run the Google Translate text to speech
License:        MIT
URL:            https://github.com/boudewijn26/gTTS-token
Source0:        https://github.com/Boudewijn26/gTTS-token/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gtts-token = %{version}-%{release}
# /oreon:deps
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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gtts-token usr/lib/python3*/site-packages/gtts_token* usr/lib64/python3*/site-packages/gtts_token* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gtts_token* usr/lib64/python3*/site-packages/gtts_token* usr/bin/*

%check

%files
%files -n python3-gtts-token -f %{oreon_filedir}/python3-gtts-token.list

%changelog

%autochangelog
