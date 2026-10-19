%global source0_hash be81511af7494eec8e5970c56a10e51aada6253246649e4ea6714fd6aeb654ee
Name:           python-ytmusicapi
Version:        1.12.3
Release:        1%{?dist}
Summary:        Unofficial API for YouTube Music
License:        MIT
URL:            https://github.com/sigma67/ytmusicapi
Source0:        https://files.pythonhosted.org/packages/source/y/ytmusicapi/ytmusicapi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7
Requires:       python3-ytmusicapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ytmusicapi
Summary:        Unofficial API for YouTube Music
# oreon:reqs
Requires:       python3dist(requests) >= 2.22
# /oreon:reqs
%description -n python3-ytmusicapi

%prep
%global oreon_srcdir ytmusicapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ytmusicapi usr/lib/python3*/site-packages/ytmusicapi* usr/lib64/python3*/site-packages/ytmusicapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ytmusicapi* usr/lib64/python3*/site-packages/ytmusicapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ytmusicapi -f %{oreon_filedir}/python3-ytmusicapi.list

%changelog

%autochangelog

