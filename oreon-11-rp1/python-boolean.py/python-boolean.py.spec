%global source0_hash 60cbc4bad079753721d32649545505362c754e121570ada4658b852a3a318d95
%global pypi_name boolean.py

Name:           python-%{pypi_name}
Version:        5.0
Release:        %autorelease
Summary:        Define boolean algebras, and create and parse boolean expressions

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/bastikr/boolean.py
Source0:        %{pypi_source boolean_py}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist pytest}

%global _description \
"boolean.py" is a small library implementing a boolean algebra. It defines\
two base elements, TRUE and FALSE, and a Symbol class that can take on one of\
these two values. Calculations are done in terms of AND, OR and NOT - other\
compositions like XOR and NAND are not implemented but can be emulated with\
AND or and NOT. Expressions are constructed from parsed strings or in Python.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n boolean_py-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l boolean

%check
%pyproject_check_import
%pytest

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
