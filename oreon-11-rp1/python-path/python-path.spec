%global source0_hash 2dfcbfec8b4d960f3469c52acf133113c2a8bf12ac7b98d629fa91af87248d42

%global pypi_name path

Name:           python-path
Version:        17.1.1
Release:        2%{?dist}
Summary:        Python module wrapper for os.path

License:        MIT
URL:            https://pypi.org/pypi/path
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(more-itertools)
%generate_buildrequires
%pyproject_buildrequires

%description
path.py implements path objects as first-class entities, allowing common
operations on files to be invoked on those path objects directly.

%package    -n python3-path
Summary:        Python 3 module wrapper for os.path
%{?python_provide:%python_provide python3-path}

%description -n python3-path
path.py implements path objects as first-class entities, allowing common
operations on files to be invoked on those path objects directly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-path
%{python3_sitelib}/path
%{python3_sitelib}/path-%{version}.dist-info/

%changelog
%autochangelog
