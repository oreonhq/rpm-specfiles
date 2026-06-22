%global source0_hash 028d46ee4b025ad9ab4d79924113816f825f62b17b87c9e1d0d8ce144a4a0e31
%global upname bottleneck

%bcond_with docs

Name:           python-Bottleneck
Version:        1.6.0
Release:        1%{?dist}
Summary:        Collection of fast NumPy array functions written in Cython
License:        BSD-2-Clause
URL:            https://pypi.org/project/Bottleneck/
Source0:        https://files.pythonhosted.org/packages/14/d8/6d641573e210768816023a64966d66463f2ce9fc9945fa03290c8a18f87c/bottleneck-%{version}.tar.gz
Patch0001:      0001-Fix-doc-build-with-Sphinx-6.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

ExcludeArch:    %{ix86}

%description
%{name} is a collection of fast NumPy array functions written in Cython.

%package -n python3-Bottleneck
Summary:        Collection of fast NumPy array functions written in Cython

%description -n python3-Bottleneck
python3-Bottleneck is a collection of fast NumPy array functions written in Cython.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{upname}-%{version} -p1
sed -i /contributors/d doc/source/conf.py

%generate_buildrequires
%if %{with docs}
%pyproject_buildrequires -x doc
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l bottleneck

%if %{with docs}
export PYTHONPATH="%{buildroot}%{python3_sitearch}"
export READTHEDOCS=1
sphinx-build -b html doc/source doc/html
rm -rf doc/html/{.buildinfo,.doctrees,.nojekyll}
%endif

%check
cd build/lib.linux-*
%pytest bottleneck
cd -

%files -n python3-Bottleneck -f %{pyproject_files}
%doc README* RELEASE*

%changelog
%autochangelog
