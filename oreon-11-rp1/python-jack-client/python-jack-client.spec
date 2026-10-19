%global source0_hash e8482097e522f0e2ef0efb95c5662932e890340f8ea4ad66fce37c3ac9608426
%global srcname0 JACK-Client
%global srcname1 jackclient-python
%global srcname2 JACK_Client
Name:          python-jack-client
Version:       0.5.5
Release:        1%{?dist}
Summary:        JACK Audio Connection Kit (JACK) Client for Python
BuildArch:     noarch
License:       MIT
URL:           http://jackclient-python.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/j/jack_client/jack_client-%{version}.tar.gz
%{?python_provide:%python_provide %{name}}
Requires:      python3-cffi
Requires:      jack-audio-connection-kit
Suggests:      python3-numpy
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-jack-client = %{version}-%{release}
# /oreon:deps
%description
Python module that provides bindings for the JACK library.
The module is able to create audio input and output ports,
also provides the functionality to manage MIDI ports.

This package installs the library for Python.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname1}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%{?pyproject_test:%pyproject_test}
%{!?pyproject_test:python3 -c 'import sys, importlib; sys.path.insert(0, "%{buildroot}%{python3_sitelib}"); importlib.import_module("jack"); importlib.import_module("_jack")'}
%files

%changelog

%autochangelog
