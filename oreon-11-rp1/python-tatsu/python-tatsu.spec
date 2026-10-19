%global source0_hash e79230f6b70d570b1314075ac1a0ca4088730955981ae5d0b6ab2f88a293117e
Name:           python-tatsu
Version:        5.24.0
Release:        1%{?dist}
Summary:        TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
License:        ...
URL:            https://github.com/neogeny/TatSu
Source0:        https://files.pythonhosted.org/packages/source/t/tatsu/tatsu-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/367.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tatsu = %{version}-%{release}
# /oreon:deps
%package -n       python3-tatsu+diagrams
Summary:        Metapackage for python3-tatsu diagrams extras
Requires:       python3-tatsu = %{version}-%{release}
Requires:       python3dist(graphviz) >= 0.21
Provides:       python3dist(tatsu[diagrams]) = %{version}-%{release}

%description -n python3-tatsu+diagrams
Metapackage for python3-tatsu diagrams extras.

%package -n       python3-tatsu+cling
Summary:        Metapackage for python3-tatsu cling extras
Requires:       python3-tatsu = %{version}-%{release}
Requires:       python3dist(pygments) >= 2.20.0
Provides:       python3dist(tatsu[cling]) = %{version}-%{release}

%description -n python3-tatsu+cling
Metapackage for python3-tatsu cling extras.

%package -n       python3-tatsu+full
Summary:        Metapackage for python3-tatsu full extras
Requires:       python3-tatsu = %{version}-%{release}
Requires:       python3dist(graphviz) >= 0.21
Requires:       python3dist(invoke) >= 2.2.1
Requires:       python3dist(pygments) >= 2.20.0
Provides:       python3dist(tatsu[full]) = %{version}-%{release}

%description -n python3-tatsu+full
Metapackage for python3-tatsu full extras.

%description

%package -n     python3-tatsu
Summary:        TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
%description -n python3-tatsu

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tatsu-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tatsu usr/lib/python3*/site-packages/tatsu* usr/lib64/python3*/site-packages/tatsu* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tatsu* usr/lib64/python3*/site-packages/tatsu* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tatsu -f %{oreon_filedir}/python3-tatsu.list

%changelog

%autochangelog
