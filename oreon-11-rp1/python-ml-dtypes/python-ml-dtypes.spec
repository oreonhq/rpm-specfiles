%global source0_hash acaef497b420a15761cb525562b04d880b5c7afacea02d435a5d166fd8a99a16

%global _distro_extra_cxxflags -I/usr/include/eigen3

Name:           python-ml-dtypes
Version:        0.5.4
Release:        %autorelease
Summary:        Implementation of several NumPy dtype extensions

License:        Apache-2.0 and MPL-2.0
URL:            https://github.com/jax-ml/ml_dtypes
#Pypi sources without test
Source0:        %{url}/archive/v%{version}/ml_dtypes-%{version}.tar.gz
# Fix pytest testArange_float8_e4m3b11fnuz because of numpy version
Patch:          04c4dc8b23720d9d92f3cc849ffc387d5798db84.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(absl-py)
BuildRequires:  python3dist(pytest)
BuildRequires:  eigen3-devel
BuildRequires:  eigen3-static
BuildRequires:  g++


%global _description %{expand:
ml_dtypes is a stand-alone implementation of several NumPy dtype extensions
used in machine learning libraries, including: bfloat16, 8-bit floating point
representations, Microscaling (MX) sub-byte floating point representations,
and Narrow integer encodings.}


%description %_description

%package -n     python3-ml-dtypes
Summary:        %{summary}

%description -n python3-ml-dtypes %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n ml_dtypes-%{version}
sed -i 's/"setuptools.*",/"setuptools >= 80.9",/g' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ml_dtypes


%check
%pyproject_check_import
%pytest ./ml_dtypes/tests/


%files -n python3-ml-dtypes -f %{pyproject_files}


%changelog
%autochangelog
