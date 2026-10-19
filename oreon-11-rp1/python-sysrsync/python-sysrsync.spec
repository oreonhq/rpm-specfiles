%global source0_hash dea4abe60e37304e9ce5fe3d0547d5cd09805b2f643acb2f336c82ffb59eb0b8
Name:           python-sysrsync
Version:        1.1.1
Release:        1%{?dist}
Summary:        Simple and safe python wrapper for calling system rsync
License:        MIT
URL:            https://github.com/gchamon/sysrsync
Source0:        https://github.com/gchamon/sysrsync/archive/%{version}/sysrsync-%{version}.tar.gz
Patch:          %{url}/pull/39.patch
Patch:          0001-In-Python-3.11-and-later-use-tomllib-instead-of-toml.patch
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sysrsync = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-sysrsync
Summary:        Simple and safe python wrapper for calling system rsync
Requires:       rsync
%description -n python3-sysrsync %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sysrsync usr/lib/python3*/site-packages/sysrsync* usr/lib64/python3*/site-packages/sysrsync* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sysrsync* usr/lib64/python3*/site-packages/sysrsync* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover -v -s test/
%files
%files -n python3-sysrsync -f %{oreon_filedir}/python3-sysrsync.list

%changelog

%autochangelog
