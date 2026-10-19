%global source0_hash 13d7bd4125dd3deed477cbfad9e8fb44a442f0bb627b5cd03afb6bc1899538db
Name:           python-cfgv
Version:        3.5.0
Release:        1%{?dist}
Summary:        Validate configuration and produce human readable error messages
License:        MIT
URL:            https://github.com/asottile/cfgv
Source0:        https://github.com/asottile/cfgv/archive/v%{version}/cfgv-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cfgv = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-cfgv
Summary:        Validate configuration and produce human readable error messages
%description -n python3-cfgv %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cfgv usr/lib/python3*/site-packages/cfgv* usr/lib64/python3*/site-packages/cfgv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cfgv* usr/lib64/python3*/site-packages/cfgv* usr/bin/*

%check

%pytest
%files
%files -n python3-cfgv -f %{oreon_filedir}/python3-cfgv.list

%changelog

%autochangelog
