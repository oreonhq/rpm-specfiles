%global source0_hash 21392b91fafd81c09bba3a6b57c31d9147e5d311fa652e72153a7eda5d4a726f
Name:           python-retask
Version:        1.1.0
Release:        1%{?dist}
Summary:        Python module to create and manage distributed task queues
License:        MIT
URL:            http://retask.readthedocs.org/en/latest/index.html
Source0:        https://pypi.python.org/packages/source/r/retask/retask-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-retask = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-retask
Summary:        Python module to create and manage distributed task queues
%{?python_provide:%python_provide python3-retask}
Requires:       python3-redis
%description -n python3-retask

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n retask-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-retask usr/lib/python3*/site-packages/retask* usr/lib64/python3*/site-packages/retask* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/retask* usr/lib64/python3*/site-packages/retask* usr/bin/*

%files
%files -n python3-retask -f %{oreon_filedir}/python3-retask.list

%changelog

%autochangelog
