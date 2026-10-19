%global source0_hash a0cbbd6634166ea8dfc16d0744d06f3205d51b86d539d0114decfb3f8fd85b41
Name:           python-htmlmin2
Version:        0.1.13
Release:        1%{?dist}
Summary:        Configurable HTML Minifier with safety features
License:        BSD-3-Clause AND Python-2.0.1
URL:            https://github.com/wilhelmer/htmlmin
Source0:        https://github.com/wilhelmer/htmlmin/archive/v%{version}/htmlmin-%{version}.tar.gz
BuildArch:      noarch
Provides:       bundled(cpython) = 3.6
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-htmlmin2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-htmlmin2
Summary:        Configurable HTML Minifier with safety features
%description -n python3-htmlmin2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir htmlmin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-htmlmin2 usr/lib/python3*/site-packages/htmlmin2* usr/lib64/python3*/site-packages/htmlmin2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/htmlmin2* usr/lib64/python3*/site-packages/htmlmin2* usr/bin/*

%check

%pytest -v
%files
%files -n python3-htmlmin2 -f %{oreon_filedir}/python3-htmlmin2.list

%changelog

%autochangelog
