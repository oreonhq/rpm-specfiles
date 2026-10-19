%global source0_hash 81366870bee75cc70e88d46efe52b9577ff9d0cf2c621d179da8405059d8524f
Name:           python-assertpy
Version:        1.1
Release:        1%{?dist}
Summary:        Simple assertion library for unit testing in Python with a fluent API
License:        BSD-3-Clause
URL:            https://github.com/assertpy/assertpy
Source0:        https://github.com/assertpy/assertpy/archive/%{version}/assertpy-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Simple assertions library for unit testing in Python with a nice fluent API.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-assertpy = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-assertpy
Summary:        Simple assertion library for unit testing in Python with a fluent API
%description -n python3-assertpy %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-assertpy usr/lib/python3*/site-packages/assertpy* usr/lib64/python3*/site-packages/assertpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/assertpy* usr/lib64/python3*/site-packages/assertpy* usr/bin/*

%check

%pytest
%files
%files -n python3-assertpy -f %{oreon_filedir}/python3-assertpy.list

%changelog

%autochangelog
