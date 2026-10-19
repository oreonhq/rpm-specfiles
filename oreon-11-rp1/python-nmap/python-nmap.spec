%global source0_hash f75af6b91dd8e3b0c31f869db32163f62ada686945e5b7c25f84bc0f7fad3b64
%global srcname nmap
Name:           python-%{srcname}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Python library which helps in using nmap port scanner
License:        GPL-3.0-or-later
URL:            https://xael.org/pages/python-nmap-en.html
Source0:        https://xael.org/pages/%{name}-%{version}.tar.gz
Patch0:         setup.py.patch
BuildArch:      noarch
Requires:       nmap
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nmap = %{version}-%{release}
# /oreon:deps
%description
python-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%package -n python3-%{srcname}
Summary:        Python library which helps in using nmap port scanner
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
python3-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p0

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/nmap* usr/lib64/python3*/site-packages/nmap* usr/bin/*

%check

%pyproject_check_import -e nmap.test_nmap
%files
%files -n python3-nmap -f %{oreon_filedir}/python3-nmap.list

%changelog

%autochangelog
