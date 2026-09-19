%global source0_hash f1a4c05349cf252e66a96cef6c821bdb07440f52dae4fde1ad8cdeafb4713f1f

Name:           python-pwntools
Version:        4.15.0
Release:        3%{?dist}
Summary:        A CTF framework and exploit development library
URL:            https://github.com/Gallopsled/pwntools/
VCS:            https://github.com/Gallopsled/pwntools/

# ./LICENSE-pwntools.txt - base project of pwntools is licensed as MIT
# ./pwnlib/data/includes/LICENSE.txt
#    - header files from FreeBSD licensed with BSD 2-clause license
#    - header files from dietlibc licensed with GPLv2 or later
# ./pwnlib/data/useragents/LICENSE.txt - script `download-useragents.py licensed with BSD 2-clause license
License:        MIT AND BSD-2-Clause AND GPL-2.0-or-later

%global srcname pwntools

# Source0:      https://github.com/Gallopsled/%%{srcname}/archive/%%{srcname}-%%{version}.tar.gz
Source0:        https://github.com/Gallopsled/%{srcname}/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# BuildRequires:  python%%{python3_pkgversion}-sphinx

# Build requirements for %%check
BuildRequires:  python%{python3_pkgversion}-capstone
BuildRequires:  python%{python3_pkgversion}-mako
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-paramiko
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-pyelftools
BuildRequires:  python%{python3_pkgversion}-pygments
BuildRequires:  python%{python3_pkgversion}-pyserial
BuildRequires:  python%{python3_pkgversion}-pysocks
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sortedcontainers
BuildRequires:  python%{python3_pkgversion}-wheel

# some packages missing on EPEL
%if (0%{?fedora})
BuildRequires:  python%{python3_pkgversion}-intervaltree
BuildRequires:  python%{python3_pkgversion}-colored-traceback
BuildRequires:  python%{python3_pkgversion}-ROPGadget
BuildRequires:  python%{python3_pkgversion}-rpyc
BuildRequires:  python%{python3_pkgversion}-unicorn
%endif

# Some packages are missing in EPEL9/8
# limited functionality will be available
%if 0%{?rhel}
%global __requires_exclude python%{python3_pkgversion}-unicorn,python%{python3_pkgversion}-intervaltree,python%{python3_pkgversion}-colored-traceback,python%{python3_pkgversion}-ROPGadget,python%{python3_pkgversion}-rpyc
%endif

%description
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       binutils

%description -n python%{python3_pkgversion}-%{srcname}
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%package doc
# Summary:        pwntools documentation
#
# %%description doc
# Documentation for pwntools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# Allow installation with unicorn 2.1.4, which is the version Fedora ships.
# See https://github.com/unicorn-engine/unicorn/issues/2134.
# Remove once fixed.
sed -i '/!=2.1.4/d' pyproject.toml

#wrong permission
chmod -x docs/requirements.txt

# Generate buildrequres is failing to generate viable deps:
# - epel due to missing python3 modules colored-traceback, intervaltree, rpyc, unicorn
# generate_buildrequires
# pyproject_buildrequires

%build
%pyproject_wheel
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# # Generate html documentation.
# PYTHONPATH=${PWD} sphinx-build-2 docs/source html
# # Remove the sphinx-build leftovers.
# rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

mv %{buildroot}%{_bindir}/checksec %{buildroot}%{_bindir}/checksec-pwntools

# setuptools < 60 installs pwntools-doc to sitelib
# setuptools >= 60 changes the installation location
# remove pwntools-doc from both locations
rm -rf %{buildroot}%{python3_sitelib}/pwntools-doc
rm -rf %{buildroot}%{_prefix}/pwntools-doc

%check
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
%py3_check_import pwn pwnlib
%{__python3} -c "from pwn import *; sh=process('bash'); sh.sendline(b'echo hello | md5sum'); x=sh.read(); assert (x == b'b1946ac92492d2347c6235b4d2611184  -\n');"

%files -n python%{python3_pkgversion}-%{srcname}
%doc CHANGELOG.md CONTRIBUTING.md README.md TESTING.md docs/requirements.txt
%license LICENSE-pwntools.txt
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{python3_sitelib}/pwn/
%{python3_sitelib}/pwnlib/
%{_bindir}/asm
%{_bindir}/checksec-pwntools
%{_bindir}/constgrep
%{_bindir}/cyclic
%{_bindir}/debug
%{_bindir}/disablenx
%{_bindir}/disasm
%{_bindir}/elfdiff
%{_bindir}/elfpatch
%{_bindir}/errno
%{_bindir}/hex
%{_bindir}/libcdb
%{_bindir}/phd
%{_bindir}/pwn
%{_bindir}/pwnstrip
%{_bindir}/scramble
%{_bindir}/shellcraft
%{_bindir}/template
%{_bindir}/unhex

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%files doc
# %%doc html
# %%license LICENSE-pwntools.txt

%changelog
%autochangelog
