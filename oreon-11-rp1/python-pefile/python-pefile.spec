# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-pefile
Version:        2024.8.26
Release:        %autorelease
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


# Source tarball contains 60+ MB of potentially malicious EXE files as tests
#Source0:        https://github.com/erocarrera/%%{srcname}/archive/v%%{version}.tar.gz#/%%{srcname}-%%{version}.tar.gz

# Release tarball contains only the functionality
Source0:        https://github.com/erocarrera/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

# For the patch
# BuildRequires: git-core

%description
%{common_desc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{common_desc}


%prep
%oreon_verify_sources
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%build
%py3_build

%install
%py3_install

%check
%py3_check_import pefile peutils ordlookup
# regression tests in this package are based on binary blob of exe files - commercial and malware
# at this point (2019-09-20) not suitable to be in Fedora.
# More info on:
# https://github.com/erocarrera/pefile/issues/171
# https://github.com/erocarrera/pefile/issues/82#issuecomment-192018385
# %%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
# TODO ... README missing in the 2024.8.26 release, should check with next version
#%%doc README*
%{python3_sitelib}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.8.26-1
- Prepare for Oreon 11 (RP1)
