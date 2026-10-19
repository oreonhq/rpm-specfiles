%global source0_hash 2fef7597bc2ee7542f22975142922adc77c0cf0f3908879717496708cb7c0f06
%global srcname stdnum
Name:           python-%{srcname}
Version:        2.2
Release:        1%{?dist}
Summary:        Python module to handle standardized numbers and codes
License:        LGPL-2.0-or-later
URL:            https://arthurdejong.org/python-stdnum/
Source0:        https://github.com/arthurdejong/python-stdnum/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-stdnum = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{srcname}
Summary:        Python module to handle standardized numbers and codes
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Patch out coverage options
sed -r -i 's/--cov[^[:blank:]]*//g' setup.cfg

# Patch out unnecessary coverage dependencies:
sed -r -i '/pytest-cov/d' tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/stdnum* usr/lib64/python3*/site-packages/stdnum* usr/bin/*

%check

export LANG=C.utf-8
%tox
%files
%files -n python3-stdnum -f %{oreon_filedir}/python3-stdnum.list

%changelog

%autochangelog
