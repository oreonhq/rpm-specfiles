%global source0_hash f9913226d056921ae2ee334ca950c96291f208bbccc71271a535202e08860911

%global modname colander

Name:           python-%{modname}
Version:        2.0
Release:        14%{?dist}
Summary:        Simple schema-based serialization and deserialization library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/colander
Source0:        https://github.com/Pylons/colander/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
An extensible package which can be used to:\
\
- deserialize and validate a data structure composed of strings, mappings,\
  and lists.\
- serialize an arbitrary data structure to a data structure composed of\
  strings, mappings, and lists.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}
Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files colander

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt COPYRIGHT.txt
%doc README.rst CONTRIBUTORS.txt CHANGES.rst docs

%changelog
%autochangelog
