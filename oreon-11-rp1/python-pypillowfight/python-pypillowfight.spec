%global source0_hash 136e59bd1cf480ec7fe2831faed47217e2f37d25fa2a0eb33f725b5514b30962
%global srcname pypillowfight
Name:           python-%{srcname}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Various image processing algorithms
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/-/archive/%{version}/libpillowfight-%{version}.tar.gz
Patch0001:      0001-Do-not-override-compile-args.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pypillowfight = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{srcname}
Summary:        Various image processing algorithms
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-%{srcname}

%prep

%autosetup -n libpillowfight-%{version} -p1

echo "#define INTERNAL_PILLOWFIGHT_VERSION \"%{version}\"" > src/pillowfight/_version.h

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pypillowfight* usr/lib64/python3*/site-packages/pypillowfight* usr/bin/*

%check

%{pytest} -ra --ignore 'tests/test_swt.py' --ignore 'tests/test_canny.py'
%files
%files -n python3-pypillowfight -f %{oreon_filedir}/python3-pypillowfight.list

%changelog

%autochangelog
