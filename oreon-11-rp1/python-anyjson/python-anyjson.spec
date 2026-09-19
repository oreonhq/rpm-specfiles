%global source0_hash 37812d863c9ad3e35c0734c42e0bf0320ce8c3bed82cd20ad54cb34d158157ba

%global pypi_name anyjson
%global sum Wraps the best available JSON implementation

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/anyjson
Source0:	%{pypi_source}

# Fix Python 3 compatibility
Patch0:         anyjson-python3.patch
# Include cjson, raise priority of cjson and drop the 'deprecation'
# warning (it's about as alive as half the others), drop jsonlib,
# jsonlib2 and django.utils.simplejson (which all appear to be dead
# as doornails)
Patch1:         python-anyjson-update-order.patch
Patch2:         do-not-use-2to3.patch
Patch3:         use-pytest.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-six

%description
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%package -n python3-%{pypi_name}
Summary:        %{sum}

%description -n python3-%{pypi_name}
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v
 
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG README
%license LICENSE

%changelog
%autochangelog
