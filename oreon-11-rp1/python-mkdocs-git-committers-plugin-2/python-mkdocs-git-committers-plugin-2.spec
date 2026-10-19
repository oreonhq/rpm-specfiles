%global source0_hash a01f17369e79ca28651681cddf212770e646e6191954bad884ca3067316aae60
Name:           python-mkdocs-git-committers-plugin-2
Version:        2.5.0
Release:        1%{?dist}
Summary:        An MkDocs plugin to create a list of contributors on the page. The git-committers plugin will seed the template context with a list of GitHub or GitLab committers and other useful GIT info such as last modified date
License:        MIT
URL:            https://github.com/ojacques/mkdocs-git-committers-plugin-2/
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_git_committers_plugin_2/mkdocs_git_committers_plugin_2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-git-committers-plugin-2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-git-committers-plugin-2
Summary:        An MkDocs plugin to create a list of contributors on the page. The git-committers plugin will seed the template context with a list of GitHub or GitLab committers and other useful GIT info such as last modified date
%description -n python3-mkdocs-git-committers-plugin-2

%prep
%global oreon_srcdir mkdocs_git_committers_plugin_2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-git-committers-plugin-2 usr/lib/python3*/site-packages/mkdocs_git_committers_plugin_2* usr/lib64/python3*/site-packages/mkdocs_git_committers_plugin_2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_git_committers_plugin_2* usr/lib64/python3*/site-packages/mkdocs_git_committers_plugin_2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-git-committers-plugin-2 -f %{oreon_filedir}/python3-mkdocs-git-committers-plugin-2.list

%changelog

%autochangelog
