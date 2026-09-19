%global source0_hash 402544cc9e179489441054f09c807804e115ea246907de87c0355fb4f5a31268

%global pypi_name XStatic

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        %autorelease
Summary:        XStatic base package with minimal support code

License:        MIT
URL:            https://github.com/xstatic-py/xstatic
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
The goal of XStatic family of packages is to provide static
file packages with minimal overhead - without selling you some 
dependencies you don't want.

XStatic has some minimal support code for working with the
XStatic-* packages.

%package -n python3-%{pypi_name}
Summary:       XStatic base package with minimal support code

%description -n python3-%{pypi_name}

The goal of XStatic family of packages is to provide static
file packages with minimal overhead - without selling you some
dependencies you don't want.

XStatic has some minimal support code for working with the
XStatic-* packages.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xstatic
mkdir -p %{buildroot}%{python3_sitelib}/xstatic/pkg

%check
%pyproject_check_import xstatic

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/XStatic-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
