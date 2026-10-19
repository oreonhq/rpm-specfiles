%global source0_hash 44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8
%global srcname referencing
Name:           python-%{srcname}
Version:        0.37.0
Release:        1%{?dist}
Summary:        An implementation-agnostic implementation of JSON reference resolution
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/r/referencing/referencing-0.37.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-referencing = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{srcname}
Summary:        An implementation-agnostic implementation of JSON reference resolution
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/referencing* usr/lib64/python3*/site-packages/referencing* usr/bin/*

%check

%pyproject_check_import -e referencing.tests*
%pytest referencing/tests
%files
%files -n python3-referencing -f %{oreon_filedir}/python3-referencing.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37.0-1
- Prepare for Oreon 11 (RP1)
