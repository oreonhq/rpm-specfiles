%global source0_hash 98e8f7039990771af0cabc1a6ed09f53d3d9d391903817cf6d3d3ca4cfb0b58b
%global with_tests 0
Name:           gtts
Version:        2.5.4
Release:        1%{?dist}
Summary:        Create an mp3 file from spoken text via the Google TTS API
License:        MIT
URL:            https://github.com/pndurette/gTTS
Source0:        https://github.com/pndurette/gTTS/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
%if 0%{?with_tests}
%endif
Requires:       python3-gtts
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-gtts = %{version}-%{release}
# /oreon:deps
%package -n       python3-gtts+tests
Summary:        Metapackage for python3-gtts tests extras
Requires:       python3-gtts = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.1.3
Requires:       python3dist(pytest) < 8.4.0
Provides:       python3dist(gtts[tests]) = %{version}-%{release}

%description -n python3-gtts+tests
Metapackage for python3-gtts tests extras.

%package -n       python3-gtts+docs
Summary:        Metapackage for python3-gtts docs extras
Requires:       python3-gtts = %{version}-%{release}
Provides:       python3dist(gtts[docs]) = %{version}-%{release}

%description -n python3-gtts+docs
Metapackage for python3-gtts docs extras.

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
# oreon:reqs
Requires:       python3dist(click) < 8.2
Requires:       python3dist(click) >= 7.1
Requires:       python3dist(requests) < 3
Requires:       python3dist(requests) >= 2.27
# /oreon:reqs
%description -n python3-gtts
gTTS (Google Text to Speech): Python3 interface for Google's Text to Speech API. 
Create an mp3 file with the python3 gTTS module. It allows unlimited lengths to 
be spoken by tokenizing long sentences where the speech would naturally pause.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gTTS-%{version}

# Remove click upper version bound
sed -i 's/click >=7.1, <8.2/click >=7.1/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gtts usr/lib/python3*/site-packages/gtts* usr/lib64/python3*/site-packages/gtts* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gtts* usr/lib64/python3*/site-packages/gtts* usr/bin/*

%check

%files
%files -n python3-gtts -f %{oreon_filedir}/python3-gtts.list

%changelog

%autochangelog
