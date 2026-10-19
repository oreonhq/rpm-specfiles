%global source0_hash 04a21681d6fbb623de53f6f364d352309d4094dd4194040a10fd51833e418d49
Name:           python-markdown-it-py
Version:        4.2.0
Release:        1%{?dist}
Summary:        Python port of markdown-it. Markdown parsing, done right!
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py
Source0:        https://files.pythonhosted.org/packages/source/m/markdown_it_py/markdown_it_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-markdown-it-py = %{version}-%{release}
# /oreon:deps
%package -n       python3-markdown-it-py+compare
Summary:        Metapackage for python3-markdown-it-py compare extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Requires:       python3dist(commonmark) >= 0.9
Requires:       python3dist(markdown) >= 3.4
Requires:       python3dist(mistletoe) >= 1.0
Requires:       python3dist(mistune) >= 3.0
Requires:       python3dist(panflute) >= 2.3
Provides:       python3dist(markdown-it-py[compare]) = %{version}-%{release}

%description -n python3-markdown-it-py+compare
Metapackage for python3-markdown-it-py compare extras.

%package -n       python3-markdown-it-py+linkify
Summary:        Metapackage for python3-markdown-it-py linkify extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Requires:       python3dist(linkify-it-py) >= 1
Requires:       python3dist(linkify-it-py) < 3
Provides:       python3dist(markdown-it-py[linkify]) = %{version}-%{release}

%description -n python3-markdown-it-py+linkify
Metapackage for python3-markdown-it-py linkify extras.

%package -n       python3-markdown-it-py+plugins
Summary:        Metapackage for python3-markdown-it-py plugins extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Requires:       python3dist(mdit-py-plugins) >= 0.5.0
Provides:       python3dist(markdown-it-py[plugins]) = %{version}-%{release}

%description -n python3-markdown-it-py+plugins
Metapackage for python3-markdown-it-py plugins extras.

%package -n       python3-markdown-it-py+rtd
Summary:        Metapackage for python3-markdown-it-py rtd extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Requires:       python3dist(mdit-py-plugins) >= 0.5.0
Requires:       python3dist(sphinx-book-theme) >= 1.0
Provides:       python3dist(markdown-it-py[rtd]) = %{version}-%{release}

%description -n python3-markdown-it-py+rtd
Metapackage for python3-markdown-it-py rtd extras.

%package -n       python3-markdown-it-py+testing
Summary:        Metapackage for python3-markdown-it-py testing extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Provides:       python3dist(markdown-it-py[testing]) = %{version}-%{release}

%description -n python3-markdown-it-py+testing
Metapackage for python3-markdown-it-py testing extras.

%package -n       python3-markdown-it-py+benchmarking
Summary:        Metapackage for python3-markdown-it-py benchmarking extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Provides:       python3dist(markdown-it-py[benchmarking]) = %{version}-%{release}

%description -n python3-markdown-it-py+benchmarking
Metapackage for python3-markdown-it-py benchmarking extras.

%package -n       python3-markdown-it-py+profiling
Summary:        Metapackage for python3-markdown-it-py profiling extras
Requires:       python3-markdown-it-py = %{version}-%{release}
Provides:       python3dist(markdown-it-py[profiling]) = %{version}-%{release}

%description -n python3-markdown-it-py+profiling
Metapackage for python3-markdown-it-py profiling extras.

%description

%package -n     python3-markdown-it-py
Summary:        Python port of markdown-it. Markdown parsing, done right!
# oreon:reqs
Requires:       python3dist(mdurl) >= 0.1
# /oreon:reqs
%description -n python3-markdown-it-py

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir markdown_it_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-markdown-it-py usr/lib/python3*/site-packages/markdown_it_py* usr/lib64/python3*/site-packages/markdown_it_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/markdown_it_py* usr/lib64/python3*/site-packages/markdown_it_py* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-markdown-it-py -f %{oreon_filedir}/python3-markdown-it-py.list

%changelog

%autochangelog
