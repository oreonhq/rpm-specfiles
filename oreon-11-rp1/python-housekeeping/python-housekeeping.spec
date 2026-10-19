%global source0_hash 75e71f1cc501885406f6be81410c9b05361871a3ecccde3891336da1e92426b5
Name:           python-housekeeping
Version:        1.1
Release:        1%{?dist}
Summary:        Python utilities for helping deprecate and remove code
License:        MIT
URL:            https://pypi.org/project/housekeeping/
Source0:        https://files.pythonhosted.org/packages/source/h/housekeeping/housekeeping-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-housekeeping = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-housekeeping
Summary:        Python utilities for helping deprecate and remove code
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.4
# /oreon:reqs
%description -n python3-housekeeping

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir housekeeping-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-housekeeping usr/lib/python3*/site-packages/housekeeping* usr/lib64/python3*/site-packages/housekeeping* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/housekeeping* usr/lib64/python3*/site-packages/housekeeping* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-housekeeping -f %{oreon_filedir}/python3-housekeeping.list

%changelog

%autochangelog
