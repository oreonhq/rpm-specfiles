%global source0_hash 620bd241acc0bbb9ec819f1ab215866871b4bbd1f73836a55f799200ee86950c

%global pypi_name aioitertools

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        %autorelease
Summary:        Itertools and builtins for AsyncIO and mixed iterables

License:        MIT
URL:            https://github.com/omnilib/aioitertools
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
