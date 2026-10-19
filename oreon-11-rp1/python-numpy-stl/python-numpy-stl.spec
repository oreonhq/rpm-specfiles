%global source0_hash 1e15e32d7de01fec66706a54c40b234f357c877c07d3add0fbe247aa9151a583
Name:           python-numpy-stl
Version:        4.0.1
Release:        1%{?dist}
Summary:        Library to make reading, writing and modifying both binary and ascii STL files easy.
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/numpy-stl/
Source0:        https://files.pythonhosted.org/packages/source/n/numpy_stl/numpy_stl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.12
BuildRequires:  python3dist(uv-build) >= 0.11.0
Requires:       python3-numpy-stl = %{version}-%{release}
# /oreon:deps
%package -n       python3-numpy-stl+docs
Summary:        Metapackage for python3-numpy-stl docs extras
Requires:       python3-numpy-stl = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.0
Requires:       python3dist(sphinx) >= 9.0
Requires:       python3dist(furo) >= 2025.1
Provides:       python3dist(numpy-stl[docs]) = %{version}-%{release}

%description -n python3-numpy-stl+docs
Metapackage for python3-numpy-stl docs extras.

%package -n       python3-numpy-stl+tests
Summary:        Metapackage for python3-numpy-stl tests extras
Requires:       python3-numpy-stl = %{version}-%{release}
Requires:       python3dist(pytest) >= 9.0
Requires:       python3dist(pytest-cov) >= 7.0
Requires:       python3dist(coverage) >= 7.0
Provides:       python3dist(numpy-stl[tests]) = %{version}-%{release}

%description -n python3-numpy-stl+tests
Metapackage for python3-numpy-stl tests extras.

%package -n       python3-numpy-stl+dev
Summary:        Metapackage for python3-numpy-stl dev extras
Requires:       python3-numpy-stl = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.15.0
Requires:       python3dist(mypy) >= 1.0
Requires:       python3dist(basedpyright) >= 1.0
Requires:       python3dist(pyrefly) >= 0.1
Requires:       python3dist(ty) >= 0.0.1
Provides:       python3dist(numpy-stl[dev]) = %{version}-%{release}

%description -n python3-numpy-stl+dev
Metapackage for python3-numpy-stl dev extras.

%package -n       python3-numpy-stl+fast
Summary:        Metapackage for python3-numpy-stl fast extras
Requires:       python3-numpy-stl = %{version}-%{release}
Requires:       python3dist(speedups) >= 2.1.0
Provides:       python3dist(numpy-stl[fast]) = %{version}-%{release}

%description -n python3-numpy-stl+fast
Metapackage for python3-numpy-stl fast extras.

%package -n       python3-numpy-stl+tox
Summary:        Metapackage for python3-numpy-stl tox extras
Requires:       python3-numpy-stl = %{version}-%{release}
Requires:       python3dist(tox) >= 4.0
Requires:       python3dist(tox-uv) >= 1.0
Requires:       python3dist(tox-gh-actions) >= 3.0
Provides:       python3dist(numpy-stl[tox]) = %{version}-%{release}

%description -n python3-numpy-stl+tox
Metapackage for python3-numpy-stl tox extras.

%description

%package -n     python3-numpy-stl
Summary:        Library to make reading, writing and modifying both binary and ascii STL files easy.
# oreon:reqs
Requires:       python3dist(numpy) >= 1.24
Requires:       python3dist(python-utils) >= 3.4.5
Requires:       python3dist(typing-extensions) >= 4.1
# /oreon:reqs
%description -n python3-numpy-stl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir numpy_stl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-numpy-stl usr/lib/python3*/site-packages/numpy_stl* usr/lib64/python3*/site-packages/numpy_stl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/numpy_stl* usr/lib64/python3*/site-packages/numpy_stl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-numpy-stl -f %{oreon_filedir}/python3-numpy-stl.list

%changelog

%autochangelog
