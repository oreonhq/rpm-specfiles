%global source0_hash 98e5854d805f50a5b58ac2333411b0482516a8210f23f43308baeb58d77c157d
%bcond tests 1
Name:           python-blessings
Version:        1.7
Release:        1%{?dist}
Summary:        Thin, practical wrapper around terminal coloring, styling, and positioning
License:        MIT
URL:            https://github.com/erikrose/blessings
Source0:        https://files.pythonhosted.org/packages/source/b/blessings/blessings-%{version}.tar.gz
Patch:          0001-fix-tests-when-run-without-a-tty-fixes-25.patch
Patch:          0002-more-fixes-for-tests-without-a-tty.patch
Patch:          0003-chore-replace-nose-with-pytest.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-blessings = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-blessings
Summary:        Thin, practical wrapper around terminal coloring, styling, and positioning
BuildRequires:  python3-devel
%description -n python3-blessings

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir blessings-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blessings usr/lib/python3*/site-packages/blessings* usr/lib64/python3*/site-packages/blessings* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blessings* usr/lib64/python3*/site-packages/blessings* usr/bin/*

%check

%if %{with tests}
%tox
%else
%pyproject_check_import -e blessings.tests
%endif
%files
%files -n python3-blessings -f %{oreon_filedir}/python3-blessings.list

%changelog

%autochangelog
