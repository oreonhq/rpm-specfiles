%global source0_hash ee2c1e74cad61124097c5f540f063fa2dd3b8cd3159f1706f11167814c9bfcd5
Name:		python-augeas
Version:	1.2.0
Release:        1%{?dist}
Summary:        Python bindings to augeas
License:	LGPL-2.1-or-later
URL:		http://augeas.net/
Source0:        https://github.com/hercules-team/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-augeas = %{version}-%{release}
# /oreon:deps
%description
python-augeas is a set of Python bindings around augeas.

%package -n python3-augeas
Summary:	Python 3 bindings to augeas
Requires:	augeas-libs
Requires:	python3-cffi
%{?python_provide:%python_provide python3-augeas}
%description -n python3-augeas
python3-augeas is a set of Python bindings around augeas.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-augeas usr/lib/python3*/site-packages/augeas* usr/lib64/python3*/site-packages/augeas* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/augeas* usr/lib64/python3*/site-packages/augeas* usr/bin/*

%check

%{pytest}
%files
%files -n python3-augeas -f %{oreon_filedir}/python3-augeas.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-7
- Prepare for Oreon 11 (RP1)
