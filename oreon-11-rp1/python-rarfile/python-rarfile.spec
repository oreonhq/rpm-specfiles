%global source0_hash dcf487b64541c07a47888d51fd199a96aae320e735a8ed923d698c4e6062f39f

%global pypi_name rarfile

Name:           python-%{pypi_name}
Version:        4.2
Release:        %autorelease
Summary:        RAR archive reader for Python

License:        ISC
URL:            https://github.com/markokr/rarfile
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Buildarch:      noarch

%description
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{pypi_name}
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}*.dist-info
%{python3_sitelib}/__pycache__/%{pypi_name}*

%changelog
%autochangelog
