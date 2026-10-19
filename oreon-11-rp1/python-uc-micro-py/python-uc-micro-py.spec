%global source0_hash 3225a494ec63b39a3542d3e2b88ed2bd85b41aad1e926c3d4453e5fae57efc45
Name:           python-uc-micro-py
Version:        2.0.0
Release:        1%{?dist}
Summary:        Micro subset of Unicode data files for linkify-it.py projects
License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
VCS:            git:%{url}.git
Source0:        https://github.com/tsutsu3/uc.micro-py/archive/v%{version}/uc.micro-py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-uc-micro-py = %{version}-%{release}
# /oreon:deps
%package -n       python3-uc-micro-py+test
Summary:        Metapackage for python3-uc-micro-py test extras
Requires:       python3-uc-micro-py = %{version}-%{release}
Provides:       python3dist(uc-micro-py[test]) = %{version}-%{release}

%description -n python3-uc-micro-py+test
Metapackage for python3-uc-micro-py test extras.

%description
Micro subset of Unicode data files for linkify-it.py projects.  This is a
Python port of uc.micro (https://github.com/markdown-it/uc.micro).

%package     -n python3-uc-micro-py
Summary:        Micro subset of Unicode data files for linkify-it.py projects
%description -n python3-uc-micro-py
Micro subset of Unicode data files for linkify-it.py projects.  This is a
Python port of uc.micro (https://github.com/markdown-it/uc.micro).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n uc.micro-py-%{version}

# Do not run coverage tools in RPM builds
sed -i 's/, "coverage", "pytest-cov"//' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uc-micro-py usr/lib/python3*/site-packages/uc_micro_py* usr/lib64/python3*/site-packages/uc_micro_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uc_micro_py* usr/lib64/python3*/site-packages/uc_micro_py* usr/bin/*

%check

%pytest -v
%files
%files -n python3-uc-micro-py -f %{oreon_filedir}/python3-uc-micro-py.list

%changelog

%autochangelog
