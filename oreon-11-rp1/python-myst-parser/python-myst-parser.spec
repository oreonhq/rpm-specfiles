%global source0_hash ab69322dc6719dcc7f296479dbb70181b66df6ed315064f92dbc85c0e1bf2f02
Name:           python-myst-parser
Version:        5.1.0
Release:        1%{?dist}
Summary:        An extended _CommonMark__https://spec.commonmark.org/_ compliant parser,
License:        MIT
URL:            https://github.com/executablebooks/MyST-Parser
Source0:        https://files.pythonhosted.org/packages/source/m/myst_parser/myst_parser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-myst-parser = %{version}-%{release}
# /oreon:deps
%package -n       python3-myst-parser+code_style
Summary:        Metapackage for python3-myst-parser code_style extras
Requires:       python3-myst-parser = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 4.0
Provides:       python3dist(myst-parser[code_style]) = %{version}-%{release}

%description -n python3-myst-parser+code_style
Metapackage for python3-myst-parser code_style extras.

%package -n       python3-myst-parser+linkify
Summary:        Metapackage for python3-myst-parser linkify extras
Requires:       python3-myst-parser = %{version}-%{release}
Requires:       python3dist(linkify-it-py) >= 2.0
Provides:       python3dist(myst-parser[linkify]) = %{version}-%{release}

%description -n python3-myst-parser+linkify
Metapackage for python3-myst-parser linkify extras.

%package -n       python3-myst-parser+rtd
Summary:        Metapackage for python3-myst-parser rtd extras
Requires:       python3-myst-parser = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8
Requires:       python3dist(sphinx-book-theme) >= 1.1
Requires:       python3dist(sphinxext-rediraffe) >= 0.3.0
Requires:       python3dist(sphinxext-opengraph) >= 0.13.0
Requires:       python3dist(sphinx-tippy) >= 0.4.3
Requires:       python3dist(sphinx-autodoc2) >= 0.5.0
Provides:       python3dist(myst-parser[rtd]) = %{version}-%{release}

%description -n python3-myst-parser+rtd
Metapackage for python3-myst-parser rtd extras.

%package -n       python3-myst-parser+testing
Summary:        Metapackage for python3-myst-parser testing extras
Requires:       python3-myst-parser = %{version}-%{release}
Requires:       python3dist(pytest) >= 9
Requires:       python3dist(pytest) < 10
Requires:       python3dist(pytest-param-files) >= 0.6.0
Requires:       python3dist(sphinx-pytest) >= 0.3.0
Requires:       python3dist(pygments) < 2.21
Provides:       python3dist(myst-parser[testing]) = %{version}-%{release}

%description -n python3-myst-parser+testing
Metapackage for python3-myst-parser testing extras.

%package -n       python3-myst-parser+testing-docutils
Summary:        Metapackage for python3-myst-parser testing-docutils extras
Requires:       python3-myst-parser = %{version}-%{release}
Requires:       python3dist(pytest) >= 9
Requires:       python3dist(pytest) < 10
Requires:       python3dist(pytest-param-files) >= 0.6.0
Provides:       python3dist(myst-parser[testing-docutils]) = %{version}-%{release}

%description -n python3-myst-parser+testing-docutils
Metapackage for python3-myst-parser testing-docutils extras.

%description

%package -n     python3-myst-parser
Summary:        An extended _CommonMark__https://spec.commonmark.org/_ compliant parser,
# oreon:reqs
Requires:       python3dist(docutils) < 0.23
Requires:       python3dist(docutils) >= 0.20
Requires:       python3dist(markdown-it-py) >= 4.2
Requires:       python3dist(mdit-py-plugins) >= 0.6
Requires:       python3dist(mdit-py-plugins) >= 0.6.1
Requires:       python3dist(sphinx) < 10
Requires:       python3dist(sphinx) >= 8
# /oreon:reqs
%description -n python3-myst-parser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir myst_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-myst-parser usr/lib/python3*/site-packages/myst_parser* usr/lib64/python3*/site-packages/myst_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/myst_parser* usr/lib64/python3*/site-packages/myst_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-myst-parser -f %{oreon_filedir}/python3-myst-parser.list

%changelog

%autochangelog
