%global source0_hash 09584397ef42ee1adc042a1198e4916686d9e4e6290640b38a465af9e4271aa5
%bcond old_poetry 1
Name:           python-asyncmy
Summary:        A fast asyncio MySQL/MariaDB driver
Version:        0.2.14
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/long2ice/asyncmy
Source0:        https://github.com/long2ice/asyncmy/archive/v%{version}/asyncmy-%{version}.tar.gz
Patch0:         python-asyncmy-0.2.11-text-files-in-sdist.patch
Patch1:         python-asyncmy-0.2.11-old-poetry.patch
ExcludeArch:    %{ix86}
%global common_description %{expand:
asyncmy is a fast asyncio MySQL/MariaDB driver, which reuses most of pymysql
and aiomysql but rewrites the core protocol with Cython to speed it up.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
Requires:       python3-asyncmy = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-asyncmy
Summary:        A fast asyncio MySQL/MariaDB driver
%description -n python3-asyncmy %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n asyncmy-%{version}
%patch 0 -p1 -b .text-files-in-sdist
%if %{with old_poetry}
%patch 1 -p1 -b .old-poetry
%endif

%install
%pyproject_install
find '%{buildroot}%{python3_sitearch}/asyncmy' \
    -type f -name '*.c' -print -delete
sed -r -i '/\.c$/d' '%{pyproject_files}'
%oreon_autofiles python3-asyncmy usr/lib/python3*/site-packages/asyncmy* usr/lib64/python3*/site-packages/asyncmy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asyncmy* usr/lib64/python3*/site-packages/asyncmy* usr/bin/*

%build

%pyproject_wheel
%files
%files -n python3-asyncmy -f %{oreon_filedir}/python3-asyncmy.list

%changelog

%autochangelog
