%global source0_hash 5e980330999299729a2d6a125347d1af78023d68a23681a4de3053ce7dfe2e51
Name:           python-mkdocs-redirects
Version:        1.2.3
Release:        1%{?dist}
Summary:        A MkDocs plugin for dynamic page redirects to prevent broken links
License:        MIT
URL:            https://github.com/ProperDocs/properdocs-redirects
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_redirects/mkdocs_redirects-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-redirects = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-redirects
Summary:        A MkDocs plugin for dynamic page redirects to prevent broken links
# oreon:reqs
Requires:       python3dist(mkdocs) <= 1.6.1
Requires:       python3dist(mkdocs) >= 1.2
Requires:       python3dist(properdocs) >= 1.6.5
# /oreon:reqs
%description -n python3-mkdocs-redirects

%prep
%global oreon_srcdir mkdocs_redirects-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-redirects usr/lib/python3*/site-packages/mkdocs_redirects* usr/lib64/python3*/site-packages/mkdocs_redirects* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_redirects* usr/lib64/python3*/site-packages/mkdocs_redirects* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-redirects -f %{oreon_filedir}/python3-mkdocs-redirects.list

%changelog

%autochangelog
