%global source0_hash b8c0dc52c93604d4f2d04c6bc19bfac0a10229ee06277e1140bacc75005fe85a

%global srcname msgpack

Name:           python-%{srcname}
Version:        1.1.2
Release:        2%{?dist}
Summary:        Python MessagePack (de)serializer

License:        Apache-2.0
URL:            https://msgpack.org/
Source0:        https://github.com/msgpack/msgpack-python/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc-c++

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

# For backwards compatibility
Provides:       python3dist(%{srcname}-python) = %{version}
Provides:       python%{python3_version}dist(%{srcname}-python) = %{version}

%description -n python%{python3_pkgversion}-%{srcname}
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python %{python3_version} (de)serializer for MessagePack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-python-%{version}
# Remove as soon as setuptools is available in a later release 
sed -i "s/setuptools >= 69.5.1/setuptools/g" pyproject.toml
# There is a circular dependency with python-msgpack-ext
rm -rf test/test_timestamp.py

%generate_buildrequires
%pyproject_buildrequires -R

%build
make cython
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v test

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog
