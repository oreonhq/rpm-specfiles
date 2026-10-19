%global source0_hash edbaca22343f861fe4e34aac47d55a0c9955c640dbf02eea99fe631e914cf9ee
Name:           python-mkdocs-literate-nav
Version:        0.6.3
Release:        1%{?dist}
Summary:        MkDocs plugin to specify the navigation in Markdown instead of YAML
License:        MIT
URL:            https://github.com/oprypin/mkdocs-literate-nav
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_literate_nav/mkdocs_literate_nav-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-literate-nav = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-literate-nav
Summary:        MkDocs plugin to specify the navigation in Markdown instead of YAML
# oreon:reqs
Requires:       python3dist(mkdocs) <= 1.6.1
Requires:       python3dist(mkdocs) >= 1.4.1
Requires:       python3dist(properdocs) >= 1.6.5
# /oreon:reqs
%description -n python3-mkdocs-literate-nav

%prep
%global oreon_srcdir mkdocs_literate_nav-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-literate-nav usr/lib/python3*/site-packages/mkdocs_literate_nav* usr/lib64/python3*/site-packages/mkdocs_literate_nav* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_literate_nav* usr/lib64/python3*/site-packages/mkdocs_literate_nav* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-literate-nav -f %{oreon_filedir}/python3-mkdocs-literate-nav.list

%changelog

%autochangelog
