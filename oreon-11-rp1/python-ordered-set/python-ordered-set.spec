%global source0_hash 694a8e44c87657c59292ede72891eb91d34131f6531463aab3009191c77364a8
%global srcname ordered-set
%global dir_name ordered_set
Name:           python-%{srcname}
Version:        4.1.0
Release:        1%{?dist}
Summary:        Custom MutableSet that remembers its order
License:        MIT
URL:            https://github.com/rspeer/ordered-set
Source0:        https://files.pythonhosted.org/packages/source/o/ordered-set/ordered-set-4.1.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-ordered-set = %{version}-%{release}
# /oreon:deps
%package -n       python3-ordered-set+dev
Summary:        Metapackage for python3-ordered-set dev extras
Requires:       python3-ordered-set = %{version}-%{release}
Provides:       python3dist(ordered-set[dev]) = %{version}-%{release}

%description -n python3-ordered-set+dev
Metapackage for python3-ordered-set dev extras.

%description

%package     -n python3-%{srcname}
Summary:        Custom MutableSet that remembers its order
%{?python_provide:%python_provide python2-%{srcname}}
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/ordered_set* usr/lib64/python3*/site-packages/ordered_set* usr/bin/*

%check

%pytest
%files
%files -n python3-ordered-set -f %{oreon_filedir}/python3-ordered-set.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.0-1
- Prepare for Oreon 11 (RP1)
