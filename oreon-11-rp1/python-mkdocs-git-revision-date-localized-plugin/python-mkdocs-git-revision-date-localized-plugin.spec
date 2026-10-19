%global source0_hash 469af4b344a4d493a6402aa92eec87a6138e1dac444e9551c1af06991453954b
Name:           python-mkdocs-git-revision-date-localized-plugin
Version:        1.6.0
Release:        1%{?dist}
Summary:        Mkdocs plugin that enables displaying the localized date of the last git modification of a markdown file.
License:        MIT
URL:            https://github.com/timvink/mkdocs-git-revision-date-localized-plugin
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_git_revision_date_localized_plugin/mkdocs_git_revision_date_localized_plugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 70.0
Requires:       python3-mkdocs-git-revision-date-localized-plugin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mkdocs-git-revision-date-localized-plugin
Summary:        Mkdocs plugin that enables displaying the localized date of the last git modification of a markdown file.
# oreon:reqs
Requires:       python3dist(babel) >= 2.7.0
Requires:       python3dist(gitpython) >= 3.1.59
Requires:       python3dist(mkdocs) < 2
Requires:       python3dist(mkdocs) >= 1.4
Requires:       python3dist(packaging) >= 20.0
Requires:       python3dist(tzdata) >= 2023.3
# /oreon:reqs
%description -n python3-mkdocs-git-revision-date-localized-plugin

%prep
%global oreon_srcdir mkdocs_git_revision_date_localized_plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-git-revision-date-localized-plugin usr/lib/python3*/site-packages/mkdocs_git_revision_date_localized_plugin* usr/lib64/python3*/site-packages/mkdocs_git_revision_date_localized_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_git_revision_date_localized_plugin* usr/lib64/python3*/site-packages/mkdocs_git_revision_date_localized_plugin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-git-revision-date-localized-plugin -f %{oreon_filedir}/python3-mkdocs-git-revision-date-localized-plugin.list

%changelog

%autochangelog
