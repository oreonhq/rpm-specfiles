%global source0_hash aba10bf2dd25ef25b0a6e116e5ee10e43852fe285f66a4092984c87cbfcf5b18
Name:           python-pytest-relaxed
Version:        2.0.2
Release:        1%{?dist}
Summary:        Relaxed test discovery/organization for pytest
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/pytest-relaxed
Source0:        https://github.com/bitprophet/pytest-relaxed/archive/%{version}/pytest-relaxed-%{version}.tar.gz
Patch:          https://github.com/bitprophet/pytest-relaxed/pull/34.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-relaxed = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-relaxed
Summary:        Relaxed test discovery/organization for pytest
%description -n python3-pytest-relaxed

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-relaxed-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-relaxed usr/lib/python3*/site-packages/pytest_relaxed* usr/lib64/python3*/site-packages/pytest_relaxed* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_relaxed* usr/lib64/python3*/site-packages/pytest_relaxed* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-pytest-relaxed -f %{oreon_filedir}/python3-pytest-relaxed.list

%changelog

%autochangelog
