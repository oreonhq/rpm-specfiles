%global source0_hash b2599426dee4a81bfe6aa40d5fb0a22ae5ff842a0a7f9df59f013bfbcd369f72
Name:           python-conda-package-streaming
Version:        0.13.0
Release:        1%{?dist}
Summary:        An efficient library to read from new and old format .conda and .tar.bz2 conda packages.
License:        ...
URL:            https://conda.github.io/conda-package-streaming/
Source0:        https://files.pythonhosted.org/packages/source/c/conda_package_streaming/conda_package_streaming-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-conda-package-streaming = %{version}-%{release}
# /oreon:deps
%package -n       python3-conda-package-streaming+test
Summary:        Metapackage for python3-conda-package-streaming test extras
Requires:       python3-conda-package-streaming = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Requires:       python3dist(conda-package-handling) >= 2
Provides:       python3dist(conda-package-streaming[test]) = %{version}-%{release}

%description -n python3-conda-package-streaming+test
Metapackage for python3-conda-package-streaming test extras.

%package -n       python3-conda-package-streaming+docs
Summary:        Metapackage for python3-conda-package-streaming docs extras
Requires:       python3-conda-package-streaming = %{version}-%{release}
Requires:       python3dist(mdit-py-plugins) >= 0.3.0
Provides:       python3dist(conda-package-streaming[docs]) = %{version}-%{release}

%description -n python3-conda-package-streaming+docs
Metapackage for python3-conda-package-streaming docs extras.

%description

%package -n     python3-conda-package-streaming
Summary:        An efficient library to read from new and old format .conda and .tar.bz2 conda packages.
%description -n python3-conda-package-streaming

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir conda_package_streaming-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-conda-package-streaming usr/lib/python3*/site-packages/conda_package_streaming* usr/lib64/python3*/site-packages/conda_package_streaming* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/conda_package_streaming* usr/lib64/python3*/site-packages/conda_package_streaming* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-conda-package-streaming -f %{oreon_filedir}/python3-conda-package-streaming.list

%changelog

%autochangelog
