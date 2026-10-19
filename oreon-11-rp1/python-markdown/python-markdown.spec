%global source0_hash 180224db6aed87ba9ce1f2781ebcd5826253de8ff637112090e24b84502bbf9f
Name:           python-markdown
Version:        3.11
Release:        1%{?dist}
Summary:        Python implementation of John Gruber_s Markdown.
License:        BSD-3-Clause
URL:            https://Python-Markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/m/markdown/markdown-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-markdown = %{version}-%{release}
# /oreon:deps
%package -n       python3-markdown+testing
Summary:        Metapackage for python3-markdown testing extras
Requires:       python3-markdown = %{version}-%{release}
Provides:       python3dist(markdown[testing]) = %{version}-%{release}

%description -n python3-markdown+testing
Metapackage for python3-markdown testing extras.

%package -n       python3-markdown+docs
Summary:        Metapackage for python3-markdown docs extras
Requires:       python3-markdown = %{version}-%{release}
Requires:       python3dist(zensical) == 0.0.62
Requires:       python3dist(mdx-gh-links) == 0.4
Requires:       python3dist(mkdocstrings) == 1.0.6
Requires:       python3dist(mkdocstrings-python) == 1.16.8
Requires:       python3dist(pygments) == 2.21.0
Requires:       python3dist(pymdown-extensions) == 11.0.2
Requires:       python3dist(justhtml) == 3.11.2
Requires:       python3dist(ghp-import) == 2.1.0
Provides:       python3dist(markdown[docs]) = %{version}-%{release}

%description -n python3-markdown+docs
Metapackage for python3-markdown docs extras.

%description

%package -n     python3-markdown
Summary:        Python implementation of John Gruber_s Markdown.
%description -n python3-markdown

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir markdown-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markdown usr/lib/python3*/site-packages/markdown* usr/lib64/python3*/site-packages/markdown* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markdown* usr/lib64/python3*/site-packages/markdown* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-markdown -f %{oreon_filedir}/python3-markdown.list

%changelog

%autochangelog
