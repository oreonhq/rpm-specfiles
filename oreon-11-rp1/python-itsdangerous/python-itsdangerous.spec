%global source0_hash e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173
%global srcname itsdangerous
Name:           python-%{srcname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Library for passing trusted data to untrusted environments
License:        BSD-3-Clause
URL:            https://itsdangerous.palletsprojects.com
Source0:        https://files.pythonhosted.org/packages/source/i/itsdangerous/itsdangerous-2.2.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-itsdangerous = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Library for passing trusted data to untrusted environments
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/itsdangerous* usr/lib64/python3*/site-packages/itsdangerous* usr/bin/*

%check

%pytest -Wdefault
%files
%files -n python3-itsdangerous -f %{oreon_filedir}/python3-itsdangerous.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0-7
- Prepare for Oreon 11 (RP1)
