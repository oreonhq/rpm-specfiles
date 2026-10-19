%global source0_hash fe48c8955a84428af77bff2642ba47041e1b8f7c867a5b7cc94f8bc255a8f0cf
Name:           python-progressbar2
Version:        4.6.0
Release:        1%{?dist}
Summary:        A Python Progressbar library to provide visual _yet text based_ progress to long running operations.
License:        BSD-3-Clause
URL:            https://github.com/wolph/python-progressbar/
Source0:        https://files.pythonhosted.org/packages/source/p/progressbar2/progressbar2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-progressbar2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-progressbar2+fast
Summary:        Metapackage for python3-progressbar2 fast extras
Requires:       python3-progressbar2 = %{version}-%{release}
Requires:       python3dist(speedups) >= 2.1.0
Provides:       python3dist(progressbar2[fast]) = %{version}-%{release}

%description -n python3-progressbar2+fast
Metapackage for python3-progressbar2 fast extras.

%package -n       python3-progressbar2+docs
Summary:        Metapackage for python3-progressbar2 docs extras
Requires:       python3-progressbar2 = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.8.5
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.6.0
Provides:       python3dist(progressbar2[docs]) = %{version}-%{release}

%description -n python3-progressbar2+docs
Metapackage for python3-progressbar2 docs extras.

%package -n       python3-progressbar2+tests
Summary:        Metapackage for python3-progressbar2 tests extras
Requires:       python3-progressbar2 = %{version}-%{release}
Requires:       python3dist(dill) >= 0.3.6
Requires:       python3dist(freezegun) >= 0.3.11
Requires:       python3dist(pytest-cov) >= 2.6.1
Requires:       python3dist(pytest) >= 4.6.9
Provides:       python3dist(progressbar2[tests]) = %{version}-%{release}

%description -n python3-progressbar2+tests
Metapackage for python3-progressbar2 tests extras.

%package -n       python3-progressbar2+docs-tests
Summary:        Metapackage for python3-progressbar2 docs-tests extras
Requires:       python3-progressbar2 = %{version}-%{release}
Requires:       python3dist(playwright) >= 1.48.0
Requires:       python3dist(pytest) >= 4.6.9
Provides:       python3dist(progressbar2[docs-tests]) = %{version}-%{release}

%description -n python3-progressbar2+docs-tests
Metapackage for python3-progressbar2 docs-tests extras.

%description

%package -n     python3-progressbar2
Summary:        A Python Progressbar library to provide visual _yet text based_ progress to long running operations.
# oreon:reqs
Requires:       python3dist(python-utils) >= 3.8.1
# /oreon:reqs
%description -n python3-progressbar2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir progressbar2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-progressbar2 usr/lib/python3*/site-packages/progressbar2* usr/lib64/python3*/site-packages/progressbar2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/progressbar2* usr/lib64/python3*/site-packages/progressbar2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-progressbar2 -f %{oreon_filedir}/python3-progressbar2.list

%changelog

%autochangelog
