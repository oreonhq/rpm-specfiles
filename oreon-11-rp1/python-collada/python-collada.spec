%global source0_hash 8194abcd4f1d2d1dd50f452f278c9b34a3e45b551ce9efe76ceb21f0c66c40e1

%global srcname pycollada

Name:           python-collada
Version:        0.9.2
Release:        5%{?dist}
Summary:        A python module for creating, editing and loading COLLADA

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pycollada/pycollada
Source0:        https://github.com/pycollada/pycollada/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# unit test requirements
BuildRequires:  python3-dateutil
BuildRequires:  python3-lxml
BuildRequires:  python3-six
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest

%description
pycollada is a python module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.

%package -n python%{python3_pkgversion}-collada
Summary:        A python 3 module for creating, editing and loading COLLADA
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-numpy
%{?python_provide: %python_provide python%{python3_pkgversion}-collada}

%description -n python%{python3_pkgversion}-collada
pycollada is a python 3 module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

 
%check
%pyproject_check_import

%pytest

%files -n python%{python3_pkgversion}-collada -f %{pyproject_files}
%doc AUTHORS.md CHANGELOG.rst README.markdown

%changelog
%autochangelog
