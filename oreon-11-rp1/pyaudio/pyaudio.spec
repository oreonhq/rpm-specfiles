%global source0_hash 26bccc81e4243d1c0ff5487e6b481de6329fcd65c79365c267cef38f363a2b56
%global srcname pyaudio
%global sum Python bindings for PortAudio
Name:		%{srcname}
Version:	0.2.14
Release:        1%{?dist}
License:	MIT
Url:		http://people.csail.mit.edu/hubert/pyaudio/
Source0:        https://files.pythonhosted.org/packages/91/a0/f439da954d78a987298cb8d1ca1b141c53b1d1d1c7a50e17198ed061b9ac/PyAudio-0.2.13.tar.gz
Summary:        Python bindings for PortAudio
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) <= 65.1.1
Requires:       python3-pyaudio = %{version}-%{release}
# /oreon:deps
%description
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O
library. With PyAudio, you can easily use Python to play and record audio on
a variety of platforms.

%package -n python3-%{srcname}
Summary:	%{sum}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O
library. With PyAudio, you can easily use Python to play and record audio on
a variety of platforms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PyAudio-%{version}
sed -i 's/setuptools<=65.1.1/setuptools/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyaudio* usr/lib64/python3*/site-packages/pyaudio* usr/bin/*

%files
%files -n python3-pyaudio -f %{oreon_filedir}/python3-pyaudio.list

%changelog

%autochangelog
