%global source0_hash 292510982205c12b1248696f44959db3cdd1740237a968ea1e2e7a900eeb2015
Name:           python-docstring-parser
Version:        0.18.0
Release:        1%{?dist}
Summary:        Parse Python docstrings in reST, Google and Numpydoc format
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source0:        https://files.pythonhosted.org/packages/source/d/docstring_parser/docstring_parser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-docstring-parser = %{version}-%{release}
# /oreon:deps
%package -n       python3-docstring-parser+test
Summary:        Metapackage for python3-docstring-parser test extras
Requires:       python3-docstring-parser = %{version}-%{release}
Provides:       python3dist(docstring-parser[test]) = %{version}-%{release}

%description -n python3-docstring-parser+test
Metapackage for python3-docstring-parser test extras.

%package -n       python3-docstring-parser+docs
Summary:        Metapackage for python3-docstring-parser docs extras
Requires:       python3-docstring-parser = %{version}-%{release}
Requires:       python3dist(pydoctor) >= 25.4.0
Provides:       python3dist(docstring-parser[docs]) = %{version}-%{release}

%description -n python3-docstring-parser+docs
Metapackage for python3-docstring-parser docs extras.

%package -n       python3-docstring-parser+dev
Summary:        Metapackage for python3-docstring-parser dev extras
Requires:       python3-docstring-parser = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 2.16.0
Provides:       python3dist(docstring-parser[dev]) = %{version}-%{release}

%description -n python3-docstring-parser+dev
Metapackage for python3-docstring-parser dev extras.

%description

%package -n     python3-docstring-parser
Summary:        Parse Python docstrings in reST, Google and Numpydoc format
%description -n python3-docstring-parser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir docstring_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docstring-parser usr/lib/python3*/site-packages/docstring_parser* usr/lib64/python3*/site-packages/docstring_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docstring_parser* usr/lib64/python3*/site-packages/docstring_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-docstring-parser -f %{oreon_filedir}/python3-docstring-parser.list

%changelog

%autochangelog
