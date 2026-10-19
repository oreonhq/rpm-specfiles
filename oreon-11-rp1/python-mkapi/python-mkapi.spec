%global source0_hash 214c34c223d7e33ac966175365ef672d5133154784589416960333ce48a21265
Name:           python-mkapi
Version:        4.5.0
Release:        1%{?dist}
Summary:        MkDocs plugin for automatic API documentation generation from Python docstrings
License:        MIT
URL:            https://github.com/daizutabi/mkapi
Source0:        https://files.pythonhosted.org/packages/source/m/mkapi/mkapi-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/commit/e0777398e7f5e285bf88fbd0b048f2eeb3d9ceaa.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkapi
Summary:        MkDocs plugin for automatic API documentation generation from Python docstrings
# oreon:reqs
Requires:       python3dist(astdoc) >= 1.3.0
Requires:       python3dist(mkdocs) >= 1.6.0
Requires:       python3dist(tomli) >= 1.1.0
# /oreon:reqs
%description -n python3-mkapi

%prep
%global oreon_srcdir mkapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkapi usr/lib/python3*/site-packages/mkapi* usr/lib64/python3*/site-packages/mkapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkapi* usr/lib64/python3*/site-packages/mkapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkapi -f %{oreon_filedir}/python3-mkapi.list

%changelog

%autochangelog
