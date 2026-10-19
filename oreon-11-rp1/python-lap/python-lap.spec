%global source0_hash 9eff7169e3ca452995af0493cc20d35452c4bfd06122c36c06457119ffbd411b
%global common_description %{expand:
This package provides the 'lap' Python library, a Linear Assignment Problem
solver using the Jonker-Volgenant algorithm. It is required by applications
like Beets for efficient tag matching.
}
Name:           python-lap
Version:        0.5.13
Release:        1%{?dist}
Summary:        Linear Assignment Problem solver for Python
License:        BSD-2-Clause
URL:            https://pypi.org/project/lap/
Source0:        https://files.pythonhosted.org/packages/source/l/lap/lap-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29.32
BuildRequires:  python3dist(numpy) >= 1.21.6
BuildRequires:  python3dist(setuptools) >= 67.8.0
Requires:       python3-lap = %{version}-%{release}
# /oreon:deps
%description %common_description

%package -n python3-lap
Summary:        Linear Assignment Problem solver for Python
%description -n python3-lap %common_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lap-%{version}
%oreon_prep
%install
%pyproject_install
rm -rvf '%{buildroot}%{python3_sitearch}/lap/tests'
sed -r -i '/.*\/lap\/tests(\/|$)/d' %{pyproject_files}
sed -r -i '/lap\.tests(\.|$)/d' %{_pyproject_modules}
%oreon_autofiles python3-lap usr/lib/python3*/site-packages/lap* usr/lib64/python3*/site-packages/lap* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lap* usr/lib64/python3*/site-packages/lap* usr/bin/*

%build

%pyproject_wheel
%check

mkdir _empty
cd _empty
ln -s ../lap/tests
%pyproject_check_import
%pytest
%files
%files -n python3-lap -f %{oreon_filedir}/python3-lap.list

%changelog

%autochangelog
