%global source0_hash 22d926ebed3421c90d40a997555b8a3ad9b49469b0edd7183b0770c8d6e25d8b
Name:           python-h5io
Version:        0.2.5
Release:        1%{?dist}
Summary:        Read and write simple Python objects using HDF5
License:        BSD-3-Clause
URL:            https://github.com/h5io/h5io
Source0:        https://github.com/h5io/h5io/archive/h5io-%{version}/h5io-h5io-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format. It is a higher-level package than
h5py.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-h5io = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-h5io
Summary:        Read and write simple Python objects using HDF5
Recommends:     python%{python3_version}dist(scipy)
%description -n python3-h5io %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n h5io-h5io-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--cov[^[:blank:]"=]*(=[^[:blank:]"]*)?//g' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-h5io usr/lib/python3*/site-packages/h5io* usr/lib64/python3*/site-packages/h5io* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/h5io* usr/lib64/python3*/site-packages/h5io* usr/bin/*

%check

%if v"0%{?python3_version}" >= v"3.13"
k="${k-}${k+ and }not test_state_with_pathlib"
%endif
%pytest -k "${k-}" -v
%files
%files -n python3-h5io -f %{oreon_filedir}/python3-h5io.list

%changelog

%autochangelog
