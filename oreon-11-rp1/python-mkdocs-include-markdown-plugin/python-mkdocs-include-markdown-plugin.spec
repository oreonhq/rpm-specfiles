%global source0_hash 2800126746452e31c2e321bbd43c8190b356e0de353e20cbc16a34a3c3d6796c
Name:           python-mkdocs-include-markdown-plugin
Version:        7.3.0
Release:        1%{?dist}
Summary:        Mkdocs Markdown includer plugin.
License:        Apache-2.0
URL:            https://github.com/mondeja/mkdocs-include-markdown-plugin
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_include_markdown_plugin/mkdocs_include_markdown_plugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-include-markdown-plugin = %{version}-%{release}
# /oreon:deps
%package -n       python3-mkdocs-include-markdown-plugin+cache
Summary:        Metapackage for python3-mkdocs-include-markdown-plugin cache extras
Requires:       python3-mkdocs-include-markdown-plugin = %{version}-%{release}
Provides:       python3dist(mkdocs-include-markdown-plugin[cache]) = %{version}-%{release}

%description -n python3-mkdocs-include-markdown-plugin+cache
Metapackage for python3-mkdocs-include-markdown-plugin cache extras.

%description

%package -n     python3-mkdocs-include-markdown-plugin
Summary:        Mkdocs Markdown includer plugin.
# oreon:reqs
Requires:       python3dist(mkdocs) >= 1.4
# /oreon:reqs
%description -n python3-mkdocs-include-markdown-plugin

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mkdocs_include_markdown_plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-include-markdown-plugin usr/lib/python3*/site-packages/mkdocs_include_markdown_plugin* usr/lib64/python3*/site-packages/mkdocs_include_markdown_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_include_markdown_plugin* usr/lib64/python3*/site-packages/mkdocs_include_markdown_plugin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-include-markdown-plugin -f %{oreon_filedir}/python3-mkdocs-include-markdown-plugin.list

%changelog

%autochangelog
