%global source0_hash 27d7f9853bf2f1a67111478d919fba297f9a4fb2b6785fbdea4d9f1cef967680
%bcond tests 1
%bcond old_setuptools 0
Name:           python-standard-nntplib
Version:        3.13.0
Release:        1%{?dist}
Summary:        Standard library nntplib redistribution
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source0:        https://files.pythonhosted.org/packages/source/s/standard_nntplib/standard_nntplib-%{version}.tar.gz
BuildArch:      noarch
%if %{with old_setuptools}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.0
Requires:       python3-standard-nntplib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-standard-nntplib
Summary:        Standard library nntplib redistribution
%description -n python3-standard-nntplib

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n standard_nntplib-%{version}
%if %{with old_setuptools}
sed -i 's:setuptools>=75.0:setuptools>=74.0:' pyproject.toml
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-standard-nntplib usr/lib/python3*/site-packages/standard_nntplib* usr/lib64/python3*/site-packages/standard_nntplib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/standard_nntplib* usr/lib64/python3*/site-packages/standard_nntplib* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest -v \
  --deselect tests/test_nntplib.py::LocalServerTests::test_starttls
%endif
%files
%files -n python3-standard-nntplib -f %{oreon_filedir}/python3-standard-nntplib.list

%changelog

%autochangelog
