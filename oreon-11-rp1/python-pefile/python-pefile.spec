%global source0_hash 3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632
Name:           python-pefile
Version:        2024.8.26
Release:        1%{?dist}
Summary:        Python module for working with Portable Executable files
License:        MIT
URL:            https://github.com/erocarrera/pefile
%global srcname pefile
%global common_desc pefile is a multi-platform Python module to read and work with Portable\
Executable (aka PE) files. Most of the information in the PE Header is \
accessible, as well as all the sections, section's information and data.\
pefile requires some basic understanding of the layout of a PE file. Armed \
with it it's possible to explore nearly every single feature of the file.\
Some of the tasks that pefile makes possible are:\
* Modifying and writing back to the PE image\
* Header Inspection\
* Sections analysis\
* Retrieving data\
* Warnings for suspicious and malformed values\
* Packer detection with PEiD’s signatures\
* PEiD signature generation\
Source0:        https://github.com/erocarrera/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{common_desc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Python module for working with Portable Executable files
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
%{common_desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import pefile peutils ordlookup
%files -f %{oreon_filedir}/main.list
%files -n python3-pefile -f %{oreon_filedir}/python3-pefile.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.8.26-1
- Prepare for Oreon 11 (RP1)
