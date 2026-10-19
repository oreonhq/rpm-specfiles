%global source0_hash bfe279073da97a97d2ef815c1fdfc1d0e07b52fca843e4a7e4683ef9a500a0d3
%global srcname walkdir
Name:           python-%{srcname}
Version:        0.4.1
Release:        35%{?dist}
Summary:        Python module to manipulate and filter os.walk() style iteration
License:        LicenseRef-Callaway-BSD
URL:            http://walkdir.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
walkdir is a simple set of iterator tools intended to
make it easy to manipulate and filter the output of os.walk()
in a way that is also easily applicable to any source iterator
that produces data in the same format

%package -n python3-%{srcname}
Summary:        Python module to manipulate and filter os.walk() style iteration
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
walkdir is a simple set of iterator tools intended to
make it easy to manipulate and filter the output of os.walk()
in a way that is also easily applicable to any source iterator
that produces data in the same format

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build

%py3_build
%install
rm -rf $RPM_BUILD_ROOT
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-walkdir -f %{oreon_filedir}/python3-walkdir.list

%changelog

%autochangelog
