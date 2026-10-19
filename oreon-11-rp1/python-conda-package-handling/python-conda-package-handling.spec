%global source0_hash 84ea1d53df6a01b8985382a7b64e8e0231881777d84761fd3a9df01704999177
Name:           python-conda-package-handling
Version:        2.6.0
Release:        1%{?dist}
Summary:        Create and extract conda packages of various formats.
License:        ...
URL:            https://conda.github.io/conda-package-handling/
Source0:        https://files.pythonhosted.org/packages/source/c/conda_package_handling/conda_package_handling-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-conda-package-handling = %{version}-%{release}
# /oreon:deps
%package -n       python3-conda-package-handling+test
Summary:        Metapackage for python3-conda-package-handling test extras
Requires:       python3-conda-package-handling = %{version}-%{release}
Provides:       python3dist(conda-package-handling[test]) = %{version}-%{release}

%description -n python3-conda-package-handling+test
Metapackage for python3-conda-package-handling test extras.

%package -n       python3-conda-package-handling+docs
Summary:        Metapackage for python3-conda-package-handling docs extras
Requires:       python3-conda-package-handling = %{version}-%{release}
Requires:       python3dist(mdit-py-plugins) >= 0.3.0
Provides:       python3dist(conda-package-handling[docs]) = %{version}-%{release}

%description -n python3-conda-package-handling+docs
Metapackage for python3-conda-package-handling docs extras.

%description

%package -n     python3-conda-package-handling
Summary:        Create and extract conda packages of various formats.
# oreon:reqs
Requires:       python3dist(backports.zstd) >= 1.1.0
Requires:       python3dist(conda-package-streaming) >= 0.13.0
# /oreon:reqs
%description -n python3-conda-package-handling

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir conda_package_handling-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-conda-package-handling usr/lib/python3*/site-packages/conda_package_handling* usr/lib64/python3*/site-packages/conda_package_handling* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/conda_package_handling* usr/lib64/python3*/site-packages/conda_package_handling* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-conda-package-handling -f %{oreon_filedir}/python3-conda-package-handling.list

%changelog

%autochangelog
