%global source0_hash 607462a3bf3d28b0574214d400820f86c0c9f43466fdf73243e7f9f2e3d21584
Name:           python-mkdocs-d2-plugin
Version:        1.7.0
Release:        1%{?dist}
Summary:        MkDocs plugin for D2
License:        MIT
URL:            https://github.com/landmaj/mkdocs-d2-plugin
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_d2_plugin/mkdocs_d2_plugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-d2-plugin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-d2-plugin
Summary:        MkDocs plugin for D2
%description -n python3-mkdocs-d2-plugin

%prep
%global oreon_srcdir mkdocs_d2_plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-d2-plugin usr/lib/python3*/site-packages/mkdocs_d2_plugin* usr/lib64/python3*/site-packages/mkdocs_d2_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_d2_plugin* usr/lib64/python3*/site-packages/mkdocs_d2_plugin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-d2-plugin -f %{oreon_filedir}/python3-mkdocs-d2-plugin.list

%changelog

%autochangelog
