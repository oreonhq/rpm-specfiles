%global source0_hash 38eb50fd3284c7353ccd4fcd3cbe149f97a3636c6e7f37b033797ebe6eb09a4d
Name:           python-pytest-freezegun
Version:        0.4.2
Release:        1%{?dist}
Summary:        Wrap pytest tests with fixtures in freeze_time
License:        MIT
URL:            https://github.com/ktosiek/pytest-freezegun
Source0:        https://github.com/ktosiek/pytest-freezegun/archive/%{version}/pytest-freezegun-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-freezegun = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-freezegun
Summary:        Wrap pytest tests with fixtures in freeze_time
%description -n python3-pytest-freezegun

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-freezegun-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-freezegun usr/lib/python3*/site-packages/pytest_freezegun* usr/lib64/python3*/site-packages/pytest_freezegun* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_freezegun* usr/lib64/python3*/site-packages/pytest_freezegun* usr/bin/*

%check

%pytest -v
%files
%files -n python3-pytest-freezegun -f %{oreon_filedir}/python3-pytest-freezegun.list

%changelog

%autochangelog
