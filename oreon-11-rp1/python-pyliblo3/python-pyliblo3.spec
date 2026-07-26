%global source0_hash 625ddf1b435eb7c1f1a1f187e11cd74e14995e108ba5d32482ff709bf6ffb2a8

%global commit 91d17815b911ccc2c1d1408412e7885c32f2d460
%global snapdate 20240801

Name:           python-pyliblo3
%global snapinfo ^%{snapdate}git%{sub %{commit} 1 7}
#Version:        0.16.2%%{snapinfo}
Version:        0.16.3
Release:        8%{?dist}
Summary:        Python bindings for the liblo Open Sound Control (OSC) library
# Main code is LGPL-2.1-or-later
License:        LGPL-2.1-or-later
URL:            https://github.com/gesellkammer/pyliblo3
#Source:         https://github.com/gesellkammer/pyliblo3/archive/%%{commit}/pyliblo3-%%{commit}.tar.gz
Source:         https://github.com/gesellkammer/pyliblo3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch:          https://github.com/gesellkammer/pyliblo3/pull/11/commits/6f0c8a73fd25fd05f528f79ac204a25657cebab7.patch

# Fix build with Cython >= 3.1
# Backported from upstream PR: https://github.com/gesellkammer/pyliblo3/pull/15
Patch: fix-cython-3.1-build.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  liblo-devel

%global _description %{expand:
python-pyliblo3 is a Python wrapper for the liblo OSC library.
It supports almost the complete functionality of liblo,
allowing you to send and receive OSC messages using a nice and simple
Python API.

This is a Python3 fork of the original bindings for liblo.}

%description %_description

%package -n     python3-pyliblo3
Summary:        %{summary}
Obsoletes:      python3-pyliblo < 0.10.0-30

%description -n python3-pyliblo3 %_description

%package doc
Summary:        Documentation for python-pyliblo3
BuildArch:      noarch

%description doc
This package contains HTML documentation, including tutorials and API
reference for python-pyliblo3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n pyliblo3-%%{commit}
%autosetup -p1 -n pyliblo3-%{version}
# Remove pregenerated Cython C sources and build it again
rm -rf pyliblo3/_liblo.c

# Fix permissions (fix for rpmlint warning "spurious-executable-perm")
chmod 644 NEWS README.md COPYING

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%generate_buildrequires
%pyproject_buildrequires

%build
cython -I pyliblo3 pyliblo3/_liblo.pyx
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyliblo3

mkdir -p %{buildroot}%{_mandir}/man1
cp -a scripts/dump_osc.1 scripts/send_osc.1 %{buildroot}%{_mandir}/man1/

%check
%pyproject_check_import

%{py3_test_envvars} %{python3} -P -m unittest discover -s ./test -p '*.py'

%files -n python3-pyliblo3 -f %{pyproject_files}
%doc README.md NEWS
%{_bindir}/dump_osc.py
%{_bindir}/send_osc.py
%_mandir/*/*

%files doc
%doc doc/
%doc examples/

%changelog
%autochangelog
