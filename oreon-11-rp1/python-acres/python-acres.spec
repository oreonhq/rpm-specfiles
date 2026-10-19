%global source0_hash 2164555a74079a74d647ed2b139a5fbbb8766c3a733077a2835837ce421e8b28
Name:           python-acres
Version:        0.5.0
Release:        1%{?dist}
Summary:        Access resources on your terms
License:        Apache-2.0
URL:            https://github.com/nipreps/acres
Source0:        https://github.com/nipreps/acres/archive/%{version}/acres-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This module aims to provide a simple way to access package resources
that will fit most use cases.}
# oreon:deps
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n python3-acres
Summary:        Access resources on your terms
%description -n python3-acres %{common_description}

%build -p

export PDM_BUILD_SCM_VERSION='%{version}'
%prep
%oreon_prep
%install
%pyproject_install
%oreon_autofiles python3-acres usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-acres -f %{oreon_filedir}/python3-acres.list

%changelog

%autochangelog
