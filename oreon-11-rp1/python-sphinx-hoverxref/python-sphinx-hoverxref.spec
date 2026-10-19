%global source0_hash 74fab961b1b8c0e9c2cf22fa195c0e783d635e78686d39dd06ff157c196ca0c9
Name:           python-sphinx-hoverxref
Version:        1.4.2
Release:        1%{?dist}
Summary:        Sphinx extension to show tooltips with content embedded when hover a reference.
License:        MIT
URL:            https://github.com/readthedocs/sphinx-hoverxref
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_hoverxref/sphinx_hoverxref-%{version}.tar.gz
BuildArch:      noarch
Patch:          sphinx-hoverxref-fix_tox_ini.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-sphinx-hoverxref = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-hoverxref+test
Summary:        Metapackage for python3-sphinx-hoverxref test extras
Requires:       python3-sphinx-hoverxref = %{version}-%{release}
Provides:       python3dist(sphinx-hoverxref[test]) = %{version}-%{release}

%description -n python3-sphinx-hoverxref+test
Metapackage for python3-sphinx-hoverxref test extras.

%package -n       python3-sphinx-hoverxref+doc
Summary:        Metapackage for python3-sphinx-hoverxref doc extras
Requires:       python3-sphinx-hoverxref = %{version}-%{release}
Requires:       python3dist(sphinxcontrib-bibtex) >= 2.6.0
Provides:       python3dist(sphinx-hoverxref[doc]) = %{version}-%{release}

%description -n python3-sphinx-hoverxref+doc
Metapackage for python3-sphinx-hoverxref doc extras.

%description

%package -n     python3-sphinx-hoverxref
Summary:        Sphinx extension to show tooltips with content embedded when hover a reference.
# oreon:reqs
Requires:       python3dist(sphinx) >= 5.0
# /oreon:reqs
%description -n python3-sphinx-hoverxref

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_hoverxref-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-hoverxref usr/lib/python3*/site-packages/sphinx_hoverxref* usr/lib64/python3*/site-packages/sphinx_hoverxref* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_hoverxref* usr/lib64/python3*/site-packages/sphinx_hoverxref* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-hoverxref -f %{oreon_filedir}/python3-sphinx-hoverxref.list

%changelog

%autochangelog
