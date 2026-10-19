%global source0_hash 63822ef6bfe5644c169bfc7ff225252f0769c86b6957a4aa2f08493a8173929b
Name:           python-cheetah
Version:        3.4.0.post5
Release:        1%{?dist}
Summary:        Template engine and code generator
License:        MIT AND BSD-3-Clause-HP AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://cheetahtemplate.org/
Source0:        https://github.com/CheetahTemplate3/cheetah3/archive/refs/tags/%{version}.tar.gz#/cheetah3-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cheetah = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-cheetah
Summary:        Template engine and code generator
%description -n python3-cheetah

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n cheetah3-%{version}

# remove unnecessary shebang lines to silence rpmlint
find Cheetah -type f -name '*.py' -print0 | xargs -0 sed -i -e '1 {/^#!/d}'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cheetah usr/lib/python3*/site-packages/cheetah* usr/lib64/python3*/site-packages/cheetah* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cheetah* usr/lib64/python3*/site-packages/cheetah* usr/bin/*

%check

sed -e 's|{envsitepackagesdir}|%{buildroot}%{python3_sitearch}|' -i tox.ini
%tox
%files
%files -n python3-cheetah -f %{oreon_filedir}/python3-cheetah.list

%changelog

%autochangelog
