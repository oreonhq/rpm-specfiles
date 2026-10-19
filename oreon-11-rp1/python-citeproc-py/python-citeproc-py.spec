%global source0_hash f2f9a64cd980706a0cac5deb7579e6f8acc87ce0140520cc9f30262d20c35307
Name:           python-citeproc-py
Version:        0.11.1
Release:        1%{?dist}
Summary:        Citations and bibliography formatter
License:        BSD-2-Clause-Views
URL:            https://github.com/citeproc-py/citeproc-py
Source0:        https://files.pythonhosted.org/packages/source/c/citeproc_py/citeproc_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(rnc2rng) >= 2.6.1
Requires:       python3-citeproc-py = %{version}-%{release}
# /oreon:deps
%package -n       python3-citeproc-py+full
Summary:        Metapackage for python3-citeproc-py full extras
Requires:       python3-citeproc-py = %{version}-%{release}
Provides:       python3dist(citeproc-py[full]) = %{version}-%{release}

%description -n python3-citeproc-py+full
Metapackage for python3-citeproc-py full extras.

%package -n       python3-citeproc-py+tests
Summary:        Metapackage for python3-citeproc-py tests extras
Requires:       python3-citeproc-py = %{version}-%{release}
Provides:       python3dist(citeproc-py[tests]) = %{version}-%{release}

%description -n python3-citeproc-py+tests
Metapackage for python3-citeproc-py tests extras.

%description

%package -n     python3-citeproc-py
Summary:        Citations and bibliography formatter
%description -n python3-citeproc-py

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir citeproc_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-citeproc-py usr/lib/python3*/site-packages/citeproc_py* usr/lib64/python3*/site-packages/citeproc_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/citeproc_py* usr/lib64/python3*/site-packages/citeproc_py* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-citeproc-py -f %{oreon_filedir}/python3-citeproc-py.list

%changelog

%autochangelog
