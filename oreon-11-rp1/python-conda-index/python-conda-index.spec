%global source0_hash 7756eb19785335e1b4f85f0d40e76c16a225e52f5fccb12fdc6db285c324120f
Name:           python-conda-index
Version:        0.13.0
Release:        1%{?dist}
Summary:        ...
License:        ...
URL:            https://github.com/conda/conda-index
Source0:        https://files.pythonhosted.org/packages/source/c/conda_index/conda_index-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.2.0
BuildRequires:  python3dist(hatchling) >= 1.12.2
Requires:       python3-conda-index = %{version}-%{release}
# /oreon:deps
%package -n       python3-conda-index+docs
Summary:        Metapackage for python3-conda-index docs extras
Requires:       python3-conda-index = %{version}-%{release}
Requires:       python3dist(mdit-py-plugins) >= 0.3.0
Provides:       python3dist(conda-index[docs]) = %{version}-%{release}

%description -n python3-conda-index+docs
Metapackage for python3-conda-index docs extras.

%package -n       python3-conda-index+psql
Summary:        Metapackage for python3-conda-index psql extras
Requires:       python3-conda-index = %{version}-%{release}
Provides:       python3dist(conda-index[psql]) = %{version}-%{release}

%description -n python3-conda-index+psql
Metapackage for python3-conda-index psql extras.

%package -n       python3-conda-index+test
Summary:        Metapackage for python3-conda-index test extras
Requires:       python3-conda-index = %{version}-%{release}
Requires:       python3dist(conda-package-handling) >= 1.9.0
Requires:       python3dist(pytest) >= 7
Provides:       python3dist(conda-index[test]) = %{version}-%{release}

%description -n python3-conda-index+test
Metapackage for python3-conda-index test extras.

%description

%package -n     python3-conda-index
Summary:        ...
# oreon:reqs
Requires:       python3dist(backports.zstd) >= 1.3.0
Requires:       python3dist(conda-package-streaming) >= 0.12.0
Requires:       python3dist(msgpack) >= 1.1.1
# /oreon:reqs
%description -n python3-conda-index

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir conda_index-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-conda-index usr/lib/python3*/site-packages/conda_index* usr/lib64/python3*/site-packages/conda_index* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/conda_index* usr/lib64/python3*/site-packages/conda_index* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-conda-index -f %{oreon_filedir}/python3-conda-index.list

%changelog

%autochangelog
