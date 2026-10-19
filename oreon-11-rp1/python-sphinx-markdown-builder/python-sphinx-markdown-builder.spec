%global source0_hash ba3bf33e0e42ff30ae686ac73957a95e6d045790dcfbaca012dd8ae01794e577
Name:           python-sphinx-markdown-builder
Version:        0.6.11
Release:        1%{?dist}
Summary:        A Sphinx extension to add markdown generation support.
License:        MIT
URL:            https://github.com/liran-funaro/sphinx-markdown-builder
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_markdown_builder/sphinx_markdown_builder-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Relax-setuptools-req.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80.9.0
BuildRequires:  python3dist(wheel) >= 0.45.1
Requires:       python3-sphinx-markdown-builder = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-markdown-builder+dev
Summary:        Metapackage for python3-sphinx-markdown-builder dev extras
Requires:       python3-sphinx-markdown-builder = %{version}-%{release}
Requires:       python3dist(sphinx) >= 9.0.4
Provides:       python3dist(sphinx-markdown-builder[dev]) = %{version}-%{release}

%description -n python3-sphinx-markdown-builder+dev
Metapackage for python3-sphinx-markdown-builder dev extras.

%description

%package -n     python3-sphinx-markdown-builder
Summary:        A Sphinx extension to add markdown generation support.
# oreon:reqs
Requires:       python3dist(sphinx) >= 5.1.0
# /oreon:reqs
%description -n python3-sphinx-markdown-builder

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_markdown_builder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-markdown-builder usr/lib/python3*/site-packages/sphinx_markdown_builder* usr/lib64/python3*/site-packages/sphinx_markdown_builder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_markdown_builder* usr/lib64/python3*/site-packages/sphinx_markdown_builder* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-markdown-builder -f %{oreon_filedir}/python3-sphinx-markdown-builder.list

%changelog

%autochangelog
