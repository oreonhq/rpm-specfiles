%global source0_hash 98e8f7039990771af0cabc1a6ed09f53d3d9d391903817cf6d3d3ca4cfb0b58b

# Needs access to Google Services so doesn't run in koji
%global with_tests 0

Name:           gtts
Version:        2.5.4
Release:        7%{?dist}
Summary:        Create an mp3 file from spoken text via the Google TTS API

License:        MIT
URL:            https://github.com/pndurette/gTTS
Source0:        https://github.com/pndurette/gTTS/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-gtts-token
BuildRequires:  python3-requests
%if 0%{?with_tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-testfixtures
%endif

Requires:       python3-gtts

%description
gTTS (Google Text to Speech): A cli interface for Google's Text to Speech API. 
Create an mp3 file with the gtts-cli command line utility. It allows 
unlimited lengths to be spoken by tokenizing long sentences where the speech 
would naturally pause.

%package -n python3-gtts
Summary:  Library for Python 3 to communicate with the Google gtts
%{?python_provide:%python_provide python3-gtts}

Requires: python3-beautifulsoup4
Requires: python3-click
Requires: python3-gtts-token
Requires: python3-requests

%description -n python3-gtts
gTTS (Google Text to Speech): Python3 interface for Google's Text to Speech API. 
Create an mp3 file with the python3 gTTS module. It allows unlimited lengths to 
be spoken by tokenizing long sentences where the speech would naturally pause.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gTTS-%{version}

# Remove click upper version bound
sed -i 's/click >=7.1, <8.2/click >=7.1/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gtts

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files
%{_bindir}/gtts-cli*

%files -n python3-gtts
%license LICENSE
%{python3_sitelib}/*

%changelog
%autochangelog
