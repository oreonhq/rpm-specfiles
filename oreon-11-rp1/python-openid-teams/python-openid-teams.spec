%global source0_hash 7b815a75a135a3b6074e4c719ffee03584f336c2baa6e4fd7aa195297d16dc5a
Name:           python-openid-teams
Version:        1.1
Release:        1%{?dist}
Summary:        Teams extension for python-openid
License:        BSD-3-Clause
URL:            https://github.com/puiterwijk/python-openid-teams
Source0:        https://github.com/puiterwijk/python-openid-teams/releases/download/v%{version}/python-openid-teams-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-openid-teams = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-openid-teams
Summary:        OpenID support for Flask
Requires:       python3-openid
%description -n python3-openid-teams
Teams extension implementation for python-openid

This package includes the python 3 version of the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openid-teams usr/lib/python3*/site-packages/openid_teams* usr/lib64/python3*/site-packages/openid_teams* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openid_teams* usr/lib64/python3*/site-packages/openid_teams* usr/bin/*

%files
%files -n python3-openid-teams -f %{oreon_filedir}/python3-openid-teams.list

%changelog

%autochangelog
