%global source0_hash fabaf3e0f18a6618d9b36560682562157f77c2b71fcffc7b432be2baed9d753d
Name:           python-safetensors
Version:        0.8.0
Release:        1%{?dist}
Summary:        ...
License:        ...
URL:            https://github.com/huggingface/safetensors
Source0:        https://files.pythonhosted.org/packages/source/s/safetensors/safetensors-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-safetensors = %{version}-%{release}
# /oreon:deps
%package -n       python3-safetensors+numpy
Summary:        Metapackage for python3-safetensors numpy extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.24.6
Provides:       python3dist(safetensors[numpy]) = %{version}-%{release}

%description -n python3-safetensors+numpy
Metapackage for python3-safetensors numpy extras.

%package -n       python3-safetensors+torch
Summary:        Metapackage for python3-safetensors torch extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(torch) >= 2.4
Provides:       python3dist(safetensors[torch]) = %{version}-%{release}

%description -n python3-safetensors+torch
Metapackage for python3-safetensors torch extras.

%package -n       python3-safetensors+tensorflow
Summary:        Metapackage for python3-safetensors tensorflow extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(tensorflow) >= 2.11.0
Provides:       python3dist(safetensors[tensorflow]) = %{version}-%{release}

%description -n python3-safetensors+tensorflow
Metapackage for python3-safetensors tensorflow extras.

%package -n       python3-safetensors+tf-nightly
Summary:        Metapackage for python3-safetensors tf-nightly extras
Requires:       python3-safetensors = %{version}-%{release}
Provides:       python3dist(safetensors[tf-nightly]) = %{version}-%{release}

%description -n python3-safetensors+tf-nightly
Metapackage for python3-safetensors tf-nightly extras.

%package -n       python3-safetensors+pinned-tf
Summary:        Metapackage for python3-safetensors pinned-tf extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(tensorflow) == 2.18.0
Provides:       python3dist(safetensors[pinned-tf]) = %{version}-%{release}

%description -n python3-safetensors+pinned-tf
Metapackage for python3-safetensors pinned-tf extras.

%package -n       python3-safetensors+jax
Summary:        Metapackage for python3-safetensors jax extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(flax) >= 0.6.3
Requires:       python3dist(jax) >= 0.3.25
Requires:       python3dist(jaxlib) >= 0.3.25
Provides:       python3dist(safetensors[jax]) = %{version}-%{release}

%description -n python3-safetensors+jax
Metapackage for python3-safetensors jax extras.

%package -n       python3-safetensors+mlx
Summary:        Metapackage for python3-safetensors mlx extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(mlx) >= 0.0.9
Provides:       python3dist(safetensors[mlx]) = %{version}-%{release}

%description -n python3-safetensors+mlx
Metapackage for python3-safetensors mlx extras.

%package -n       python3-safetensors+paddlepaddle
Summary:        Metapackage for python3-safetensors paddlepaddle extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(paddlepaddle) >= 2.4.1
Provides:       python3dist(safetensors[paddlepaddle]) = %{version}-%{release}

%description -n python3-safetensors+paddlepaddle
Metapackage for python3-safetensors paddlepaddle extras.

%package -n       python3-safetensors+convert
Summary:        Metapackage for python3-safetensors convert extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(huggingface-hub) >= 1.4
Provides:       python3dist(safetensors[convert]) = %{version}-%{release}

%description -n python3-safetensors+convert
Metapackage for python3-safetensors convert extras.

%package -n       python3-safetensors+quality
Summary:        Metapackage for python3-safetensors quality extras
Requires:       python3-safetensors = %{version}-%{release}
Provides:       python3dist(safetensors[quality]) = %{version}-%{release}

%description -n python3-safetensors+quality
Metapackage for python3-safetensors quality extras.

%package -n       python3-safetensors+testing
Summary:        Metapackage for python3-safetensors testing extras
Requires:       python3-safetensors = %{version}-%{release}
Requires:       python3dist(h5py) >= 3.7.0
Requires:       python3dist(setuptools-rust) >= 1.12.0
Requires:       python3dist(pytest) >= 9.0
Requires:       python3dist(pytest-benchmark) >= 5.2
Requires:       python3dist(hypothesis) >= 6.70.2
Requires:       python3dist(fsspec) >= 2024.6.0
Requires:       python3dist(s3fs) >= 2024.6.0
Provides:       python3dist(safetensors[testing]) = %{version}-%{release}

%description -n python3-safetensors+testing
Metapackage for python3-safetensors testing extras.

%package -n       python3-safetensors+all
Summary:        Metapackage for python3-safetensors all extras
Requires:       python3-safetensors = %{version}-%{release}
Provides:       python3dist(safetensors[all]) = %{version}-%{release}

%description -n python3-safetensors+all
Metapackage for python3-safetensors all extras.

%package -n       python3-safetensors+dev
Summary:        Metapackage for python3-safetensors dev extras
Requires:       python3-safetensors = %{version}-%{release}
Provides:       python3dist(safetensors[dev]) = %{version}-%{release}

%description -n python3-safetensors+dev
Metapackage for python3-safetensors dev extras.

%description

%package -n     python3-safetensors
Summary:        ...
%description -n python3-safetensors

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir safetensors-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-safetensors usr/lib/python3*/site-packages/safetensors* usr/lib64/python3*/site-packages/safetensors* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/safetensors* usr/lib64/python3*/site-packages/safetensors* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-safetensors -f %{oreon_filedir}/python3-safetensors.list

%changelog

%autochangelog
