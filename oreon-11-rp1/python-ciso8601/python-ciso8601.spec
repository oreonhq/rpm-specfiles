%global source0_hash 1510481321ba3599661aec6a82ab3f1832f7f3a009179ca299be0cfa9cfd12aa

%global pypi_name ciso8601

Name:           python-%{pypi_name}
Version:        2.3.3
Release:        1%{?dist}
Summary:        Fast ISO8601 date time parser

License:        MIT
URL:            https://github.com/closeio/ciso8601
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

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

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.rst

%changelog
%autochangelog
