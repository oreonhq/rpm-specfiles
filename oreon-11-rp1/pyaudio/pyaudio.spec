%global source0_hash 26bccc81e4243d1c0ff5487e6b481de6329fcd65c79365c267cef38f363a2b56

%global srcname pyaudio
%global sum Python bindings for PortAudio

Name:		%{srcname}
Version:	0.2.13
Release:	11%{?dist}
License:	MIT
Url:		http://people.csail.mit.edu/hubert/pyaudio/
Source0:	https://files.pythonhosted.org/packages/91/a0/f439da954d78a987298cb8d1ca1b141c53b1d1d1c7a50e17198ed061b9ac/PyAudio-0.2.13.tar.gz
Summary:	%{sum}

BuildRequires:	gcc
BuildRequires:	portaudio-devel
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyaudio

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CHANGELOG

%changelog
%autochangelog
