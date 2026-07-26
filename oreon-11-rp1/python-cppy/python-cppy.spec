%global source0_hash 55b5307c11874f242ea135396f398cb67a5bbde4fab3e3c3294ea5fce43a6d68

%global srcname cppy

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        C++ headers for C extension development

License:        BSD-3-Clause
URL:            https://github.com/nucleic/cppy
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.

%package -n python-%{srcname}-doc
Summary:        cppy documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for cppy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
