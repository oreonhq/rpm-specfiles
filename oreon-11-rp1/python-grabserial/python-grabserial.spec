%global source0_hash ecb474cb90668725a75bb792a0b71d76140acf591909ce08771a2cea0cbf45b9

%global realname grabserial

Name: python-grabserial
Version: 2.0.2
Release: 21%{?dist}
Summary: Reads a serial port and writes data to standard output

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://elinux.org/Grabserial
Source0: https://github.com/tbird20d/grabserial/archive/v%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-setuptools
BuildRequires: python3-devel

%global _description\
Grabserial reads a serial port and writes the data to standard output.The main\
purpose of this tool is to collect messages written to the serial console from\
a target board running Linux, and save the messages on a host machine.

%description %_description

%package -n python3-grabserial
Summary: %summary
Requires: python3-pyserial
%{?python_provide:%python_provide python3-grabserial}

%description -n python3-grabserial %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{realname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files -n python3-grabserial
%doc README.md
%license LICENSE
%{_bindir}/grabserial
%{python3_sitelib}/*.egg-info

%changelog
%autochangelog
