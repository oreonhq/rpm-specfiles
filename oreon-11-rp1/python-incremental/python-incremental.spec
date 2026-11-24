# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b01ca8b6fe7d53dfc1b3fe642a6ede28e8cc8a98526a041f7a485a15f9c34e7b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname incremental

%global common_description %{expand:
Incremental is a small library that versions your Python projects.}

Name:           python-%{srcname}
Version:        24.7.2
Release:        %{autorelease}
Summary:        It versions your Python projects

License:        MIT
URL:            https://github.com/twisted/incremental
Source0:        %{url}/archive/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname} %{common_description}

%prep
%oreon_sha256
%autosetup -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
