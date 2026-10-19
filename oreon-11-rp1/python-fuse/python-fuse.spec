%global source0_hash 72ff783ec2f43de3ab394e3f7457605bf04c8cf288a2f4068b4cde141d4ee6bd
%global srcname fusepy
Name:    python-fuse
Version: 3.0.1
Release:        1%{?dist}
Summary:        Python module that provides a simple interface to FUSE and MacFUSE
License: ISC
URL: https://github.com/fusepy/fusepy
Source0:        https://files.pythonhosted.org/packages/source/%/%{srcname/%{srcname-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
fusepy is a Python module that provides a simple interface to FUSE and MacFUSE.
It's just one file and is implemented using ctypes.

%package -n python3-fusepy
Summary:        Python module that provides a simple interface to FUSE and MacFUSE
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
%oreon_autofiles python3-fusepy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-fusepy -f %{oreon_filedir}/python3-fusepy.list

%changelog

%autochangelog
