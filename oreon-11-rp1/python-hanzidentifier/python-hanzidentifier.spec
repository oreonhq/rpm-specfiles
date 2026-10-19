%global source0_hash e855b1fe2108f63127794411f7bc8ba8b44557f38bdbbc65b7a63b7973fdc8ac
Name:           python-hanzidentifier
Version:        1.3.0
Release:        1%{?dist}
Summary:        Identify Chinese text as Simplified or Traditional
License:        MIT
URL:            https://github.com/tsroten/hanzidentifier
Source0:        https://github.com/tsroten/hanzidentifier/archive/v%{version}/hanzidentifier-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hanzidentifier = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hanzidentifier
Summary:        Identify Chinese text as Simplified or Traditional
# oreon:reqs
Requires:       python3dist(zhon) >= 2.1
# /oreon:reqs
%description -n python3-hanzidentifier

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hanzidentifier-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hanzidentifier usr/lib/python3*/site-packages/hanzidentifier* usr/lib64/python3*/site-packages/hanzidentifier* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hanzidentifier* usr/lib64/python3*/site-packages/hanzidentifier* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-hanzidentifier -f %{oreon_filedir}/python3-hanzidentifier.list

%changelog

%autochangelog
