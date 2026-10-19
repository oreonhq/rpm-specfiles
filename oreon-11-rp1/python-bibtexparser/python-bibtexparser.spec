%global source0_hash 672a59f4ba431c4e9a6647cc7c42a267b22e257bcd2cfdb661863f3756c9ab14
Name:           python-bibtexparser
Version:        2.0.1
Release:        1%{?dist}
Summary:        Bibtex parser for python 3
License:        MIT
URL:            https://github.com/sciunto-org/python-bibtexparser
Source0:        https://files.pythonhosted.org/packages/source/b/bibtexparser/bibtexparser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-bibtexparser = %{version}-%{release}
# /oreon:deps
%package -n       python3-bibtexparser+docs
Summary:        Metapackage for python3-bibtexparser docs extras
Requires:       python3-bibtexparser = %{version}-%{release}
Provides:       python3dist(bibtexparser[docs]) = %{version}-%{release}

%description -n python3-bibtexparser+docs
Metapackage for python3-bibtexparser docs extras.

%package -n       python3-bibtexparser+test
Summary:        Metapackage for python3-bibtexparser test extras
Requires:       python3-bibtexparser = %{version}-%{release}
Provides:       python3dist(bibtexparser[test]) = %{version}-%{release}

%description -n python3-bibtexparser+test
Metapackage for python3-bibtexparser test extras.

%description

%package -n     python3-bibtexparser
Summary:        Bibtex parser for python 3
# oreon:reqs
Requires:       python3dist(pylatexenc) >= 2.10
# /oreon:reqs
%description -n python3-bibtexparser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir bibtexparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bibtexparser usr/lib/python3*/site-packages/bibtexparser* usr/lib64/python3*/site-packages/bibtexparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bibtexparser* usr/lib64/python3*/site-packages/bibtexparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bibtexparser -f %{oreon_filedir}/python3-bibtexparser.list

%changelog

%autochangelog
