%global source0_hash c04be774e1c09ff4acbfc4de686e9a0f18e3ae1c6daabc852a65456f36d4272f
Name:           python-reretry
Version:        0.11.8
Release:        1%{?dist}
Summary:        Easy to use retry decorator
License:        Apache-2.0
URL:            https://github.com/leshchenko1979/reretry
Source0:        https://github.com/leshchenko1979/reretry/archive/%{version}/reretry-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
An easy to use retry decorator.
This package is a fork from the retry package, but with some of added
community-sourced features.
Features
New features in reretry:
  • Log traceback of an error that lead to a failed attempt.
  • Call a custom callback after each failed attempt.
  • Can be used with async functions.
From original retry:
  • Retry on specific exceptions.
  • Set a maximum number of retries.
  • Set a delay between retries.
  • Set a maximum delay between retries.
  • Set backoff and jitter parameters.
  • Use a custom logger.
  • No external dependencies (stdlib only).
  • (Optionally) Preserve function signatures (pip install decorator).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-reretry = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-reretry
Summary:        Easy to use retry decorator
Recommends:     %{py3_dist decorator}
%description -n python3-reretry %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-reretry usr/lib/python3*/site-packages/reretry* usr/lib64/python3*/site-packages/reretry* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/reretry* usr/lib64/python3*/site-packages/reretry* usr/bin/*

%check

%pytest
%files
%files -n python3-reretry -f %{oreon_filedir}/python3-reretry.list

%changelog

%autochangelog
