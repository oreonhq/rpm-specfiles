%global source0_hash 65861e95ea3bfd3aac67a81f2d721fe859fe959250e2f1142bc7e162b38bfb29
Name:           ampy
Version:        1.0.7
Release:        1%{?dist}
Summary:        Command line tool to interact with a MicroPython board over a serial connection
License:        MIT
URL:            https://github.com/adafruit/ampy
Source0:        https://github.com/adafruit/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       adafruit-%{name} = %{version}-%{release}
%py_provides    python3-adafruit-%{name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ampy = %{version}-%{release}
# /oreon:deps
%description
Adafruit MicroPython tool is a command line tool to interact with a MicroPython
board over a serial connection.

Ampy is meant to be a simple command line tool to manipulate files and run code
on a MicroPython board over its serial connection. With ampy you can send files
from your computer to a MicroPython board's file system, download files from a
board to your computer, and even send a Python script to a board to be
executed.

Note that ampy by design is meant to be simple and does not support advanced
interaction like a shell or terminal to send input to a board. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

# shebangs
sed -i '1d' $(grep -lr '#!/usr/')

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%{python3} -m unittest tests/test_*.py -v
%files

%changelog

%autochangelog
