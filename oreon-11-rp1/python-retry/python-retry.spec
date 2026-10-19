%global source0_hash 9bffdf1a1cee51602b7bc6cc00dfac13d89528aaef34f5bd8f596d2b1ef1b7d8
Name:           python-retry
Version:        0.9.4
Release:        14%{?dist}
Summary:        Easy to use retry decorator
License:        Apache-2.0
URL:            https://github.com/eSAMTrade/retry
Source0:        https://github.com/eSAMTrade/retry/archive/%{version}/retry-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix_requirements.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-retry = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-retry
Summary:        Easy to use retry decorator
%description -n python3-retry

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir retry-%{version}
%oreon_prep
%build

export PBR_VERSION="%{version}"
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-retry usr/lib/python3*/site-packages/retry* usr/lib64/python3*/site-packages/retry* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/retry* usr/lib64/python3*/site-packages/retry* usr/bin/*

%check

%tox
%files
%files -n python3-retry -f %{oreon_filedir}/python3-retry.list

%changelog

%autochangelog
