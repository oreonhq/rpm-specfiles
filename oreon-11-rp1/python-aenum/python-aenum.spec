%global source0_hash 4c7a5fb76a04ad8dc0c82b13c4cd858b755c69d16c2060a248bf3380a4d1067e

%global pypi_name aenum

Name:           python-%{pypi_name}
Version:        3.1.16
Release:        3%{?dist}
Summary:        Advanced Enumerations, NamedTuples and NamedConstants for Python

License:        BSD-3-Clause
URL:            https://pypi.org/project/aenum/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aenum includes a Python stdlib Enum-compatible data type, as well as a
metaclass-based NamedTuple implementation and a NamedConstant class.

An Enum is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the
enumeration itself can be iterated over. Support exists for unique values,
multiple values, auto-numbering, and suspension of aliasing, plus the ability
to have values automatically bound to attributes.

A NamedTuple is a class-based, fixed-length tuple with a name for each
possible position accessible using attribute-access notation as well as
the standard index notation.

A NamedConstant is a class whose members cannot be rebound; it lacks all other
Enum capabilities, however.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm %{pypi_name}/_py2.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# https://github.com/ethanfurman/aenum/issues/7
sed -i -e 's/from \. /from aenum /g' -e 's/from \./from aenum\./g' %{pypi_name}/test.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} %{pypi_name}/test.py

%files -n python3-%{pypi_name}
%doc README.md aenum/doc aenum/CHANGES
%license aenum/LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
