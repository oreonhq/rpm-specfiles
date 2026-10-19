%global source0_hash 63d27fac1684f052e4ce909cffd2abb6be952a4dc53eb4abe0d3bba61db85b8e
Name:           python-unique-log-filter
Version:        0.1.0
Release:        1%{?dist}
Summary:        A log filter that removes duplicate log messages
License:        BSD-2-Clause
URL:            https://github.com/twizmwazin/unique_log_filter
Source0:        https://github.com/twizmwazin/unique_log_filter/archive/v%{version}/unique_log_filter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-unique-log-filter = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-unique-log-filter
Summary:        A log filter that removes duplicate log messages
%description -n python3-unique-log-filter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir unique_log_filter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-unique-log-filter usr/lib/python3*/site-packages/unique_log_filter* usr/lib64/python3*/site-packages/unique_log_filter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/unique_log_filter* usr/lib64/python3*/site-packages/unique_log_filter* usr/bin/*

%check

%{py3_test_envvars} %{python3} test_unique_log_filter.py
%files
%files -n python3-unique-log-filter -f %{oreon_filedir}/python3-unique-log-filter.list

%changelog

%autochangelog
