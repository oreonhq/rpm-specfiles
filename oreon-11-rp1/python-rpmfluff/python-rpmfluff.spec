%global source0_hash d1a680f9db7ce67b3c96be62042d279dfe00c9ed966863e0f950652f6cb3badc
%global modname rpmfluff
Name:          python-%{modname}
Version:       0.6.7
Release:        1%{?dist}
Summary:        Lightweight way of building RPMs, and sabotaging them
License:       GPL-2.0-or-later
URL:           https://pagure.io/rpmfluff
Source0:        https://files.pythonhosted.org/packages/fb/e6/7892e71218d86c84c434aecc62f2a87f42e802768ca5496bb814e36ba9e5/rpmfluff-0.6.7.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpmfluff = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        Lightweight way of building RPMs, and sabotaging them
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
Requires:       rpm-build
Requires:       createrepo_c
%description -n python3-%{modname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{modname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/rpmfluff* usr/lib64/python3*/site-packages/rpmfluff* usr/bin/*

%check

python3 -m unittest %{modname}.test
%files
%files -n python3-rpmfluff -f %{oreon_filedir}/python3-rpmfluff.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.7-1
- Prepare for Oreon 11 (RP1)
