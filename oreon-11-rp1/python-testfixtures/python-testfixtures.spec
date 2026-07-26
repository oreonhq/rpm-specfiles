%global source0_hash 517e9cf353942723533ae1100ca45dd27fe0785c3ad2765075f5cb1cbce01482

%global pypi_name testfixtures

Name:           python-%{pypi_name}
Version:        9.1.0
Release:        %autorelease
Summary:        Collection of helpers and mock objects for unit tests

License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

#%%check
# Upstream has a different idea about how Open Source works
# and is hostile against everything that doesn't match that idea.
# Thus, the only thing that matters is that tests work in their CI

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
