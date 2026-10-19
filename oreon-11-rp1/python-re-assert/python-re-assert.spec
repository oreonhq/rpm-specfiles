%global source0_hash 01c4a849ed520923e4bab9afdf73b5f2698c4f92ad7f580ccb3f68ea79c69c0c
Name:           python-re-assert
Version:        1.1.0
Release:        1%{?dist}
Summary:        Show where your regex match assertion failed
License:        MIT
URL:            https://github.com/asottile/re-assert
Source0:        https://github.com/asottile/re-assert/archive/v%{version}/re-assert-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}!}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-re-assert = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-re-assert
Summary:        Show where your regex match assertion failed
%description -n python3-re-assert %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir re-assert-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-re-assert usr/lib/python3*/site-packages/re_assert* usr/lib64/python3*/site-packages/re_assert* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/re_assert* usr/lib64/python3*/site-packages/re_assert* usr/bin/*

%check

%pytest
%files
%files -n python3-re-assert -f %{oreon_filedir}/python3-re-assert.list

%changelog

%autochangelog
