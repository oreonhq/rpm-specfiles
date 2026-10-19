%global source0_hash acaef497b420a15761cb525562b04d880b5c7afacea02d435a5d166fd8a99a16
%global _distro_extra_cxxflags -I/usr/include/eigen3
Name:           python-ml-dtypes
Version:        0.5.4
Release:        1%{?dist}
Summary:        Implementation of several NumPy dtype extensions
License:        Apache-2.0 and MPL-2.0
URL:            https://github.com/jax-ml/ml_dtypes
Source0:        https://github.com/jax-ml/ml_dtypes/archive/v%{version}/ml_dtypes-%{version}.tar.gz
Patch:          04c4dc8b23720d9d92f3cc849ffc387d5798db84.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) >= 2.0
BuildRequires:  python3dist(setuptools) >= 80.9.0
Requires:       python3-ml-dtypes = %{version}-%{release}
# /oreon:deps
%package -n       python3-ml-dtypes+dev
Summary:        Metapackage for python3-ml-dtypes dev extras
Requires:       python3-ml-dtypes = %{version}-%{release}
Requires:       python3dist(pylint) >= 2.6.0
Provides:       python3dist(ml-dtypes[dev]) = %{version}-%{release}

%description -n python3-ml-dtypes+dev
Metapackage for python3-ml-dtypes dev extras.

%description

%package -n     python3-ml-dtypes
Summary:        Implementation of several NumPy dtype extensions
# oreon:reqs
Requires:       python3dist(numpy) >= 1.21
Requires:       python3dist(numpy) >= 1.21.2
Requires:       python3dist(numpy) >= 1.23.3
Requires:       python3dist(numpy) >= 1.26.0
Requires:       python3dist(numpy) >= 2.1.0
# /oreon:reqs
%description -n python3-ml-dtypes

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n ml_dtypes-%{version}
sed -i 's/"setuptools.*",/"setuptools >= 80.9",/g' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ml-dtypes usr/lib/python3*/site-packages/ml_dtypes* usr/lib64/python3*/site-packages/ml_dtypes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ml_dtypes* usr/lib64/python3*/site-packages/ml_dtypes* usr/bin/*

%check

%pyproject_check_import
%pytest ./ml_dtypes/tests/
%files
%files -n python3-ml-dtypes -f %{oreon_filedir}/python3-ml-dtypes.list

%changelog

%autochangelog
