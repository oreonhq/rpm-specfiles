%global source0_hash 4be0cc459b9f3d9f24726f0f448ac67ff8d4c87a7010453dca817b556bd0b841

%global pypi_name listparser

Name:           python-%{pypi_name}
Version:        0.18
Release:        29%{?dist}
Summary:        Parse OPML, FOAF, and iGoogle subscription lists

License:        LGPL-3.0-or-later
URL:            https://github.com/kurtmckee/listparser
Source0:        %pypi_source
BuildArch:      noarch
Patch0:         2to3.patch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

%description
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n python-%{pypi_name}-doc
Summary:        listparser documentation
%description -n python-%{pypi_name}-doc
Documentation for listparser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p0
chmod 644 COPYING
chmod 644 COPYING.LESSER
chmod 644 README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

#%check
#%{__python3} lptest.py test

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%license COPYING COPYING.LESSER
%doc html

%changelog
%autochangelog
