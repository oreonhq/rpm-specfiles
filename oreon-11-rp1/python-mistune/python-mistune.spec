%global source0_hash 58b5c96d6fcb61190dfe5fae498d2b2065f99cf61e9649418fd54cf1ada86dfe
Name:           python-mistune
Version:        3.3.4
Release:        1%{?dist}
Summary:        A sane and fast Markdown parser with useful plugins and renderers
License:        BSD-3-Clause
URL:            https://github.com/lepture/mistune
Source0:        https://files.pythonhosted.org/packages/source/m/mistune/mistune-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mistune = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mistune
Summary:        A sane and fast Markdown parser with useful plugins and renderers
%description -n python3-mistune

%prep
%global oreon_srcdir mistune-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mistune usr/lib/python3*/site-packages/mistune* usr/lib64/python3*/site-packages/mistune* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mistune* usr/lib64/python3*/site-packages/mistune* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mistune -f %{oreon_filedir}/python3-mistune.list

%changelog

%autochangelog
