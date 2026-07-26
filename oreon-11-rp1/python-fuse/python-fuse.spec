%global source0_hash 72ff783ec2f43de3ab394e3f7457605bf04c8cf288a2f4068b4cde141d4ee6bd

%global srcname fusepy

Name:    python-fuse
# TODO rename to python-fusepy
Version: 3.0.1
Release: 6%{?dist}
Summary: Python module that provides a simple interface to FUSE and MacFUSE
License: ISC
URL: https://github.com/fusepy/fusepy
Source: %{pypi_source %{srcname}}
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
fusepy is a Python module that provides a simple interface to FUSE and MacFUSE.
It's just one file and is implemented using ctypes.

%package -n python3-fusepy
Summary: %{summary}
%{?python_provide:%python_provide python3-fuse}
%{?python_provide:%python_provide python3-fusepy}
Provides: python3-fuse = %{version}-%{release}
Obsoletes: python3-fuse < 2.0.4-10
Requires: fuse-libs

%description -n python3-fusepy
fusepy is a Python module that provides a simple interface to FUSE and MacFUSE.
It's just one file and is implemented using ctypes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-fusepy
%doc README.rst
%{python3_sitelib}/fuse.py
%{python3_sitelib}/fusepy-*egg-info/
%{python3_sitelib}/__pycache__

%changelog
%autochangelog
