%global source0_hash 69d9d737dbe694867fec26a7dc5dc116dcf4cf4fb4d57acd6d9273a9371a04f7

Name:           python-smbpasswd
Version:        1.0.2
Release:        24%{?dist}
Summary:        Python SMB Password Hash Generator Module

License:        GPL-2.0-only
URL:            https://github.com/barryp/py-smbpasswd/
#               http://barryp.org/software/py-smbpasswd/
#               https://github.com/barryp/py-smbpasswd/releases
# Source0:      http://barryp.org/software/py-smbpasswd/files/py-smbpasswd-%%{version}.tar.gz
Source0:        https://github.com/barryp/py-smbpasswd/archive/%{version}.tar.gz#/py-smbpasswd-%{version}.tar.gz
Patch1:         python-smbpasswd-1.0.1-py3.patch

# For python3 the modules using # format needs to define PY_SSIZE_T_CLEAN
Patch2:         python-smbpasswd-1.0.2-py3.10.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

%global _description\
This package contains a python module, which is able to generate LANMAN and\
NT password hashes suitable to us with Samba.

%description %_description

%package -n python3-smbpasswd
Summary:        %{summary} for Python 3
%{?python_provide:%python_provide python3-smbpasswd}

%description -n python3-smbpasswd
This package contains a python module, which is able to generate LANMAN and
NT password hashes suitable to us with Samba.

This is a ported release for python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n py-smbpasswd-%{version}

%build
%py3_build

%install
%py3_install

%check
# there are no tests, let's do some sanity check ourselves
%{py3_test_envvars} %{python3} -c '
import smbpasswd
lmhash = "316AEBE722192264AAD3B435B51404EE"
nthash = "B16315C81C204B3CB1E9D00A34C13103"
assert smbpasswd.lmhash("check") == lmhash
assert smbpasswd.nthash("check") == nthash
assert smbpasswd.hash("check") == (lmhash, nthash)'

%files -n python3-smbpasswd
%license COPYING.txt
%doc README.txt
%{python3_sitearch}/smbpasswd.cpython-3*.so
%{python3_sitearch}/*egg-info/

%changelog
%autochangelog
