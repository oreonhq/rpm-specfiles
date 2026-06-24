%global source0_hash none

%global pypi_name xmltodict

Name:               python-xmltodict
Version:            0.14.2
Release:            6%{?dist}
Summary:            Python to transform XML to JSON

License:            MIT
URL:                https://github.com/martinblech/xmltodict
Source0:            %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:          noarch

%description
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

%package -n python3-%{pypi_name}
Summary:            %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
xmltodict is a Python module that makes working with XML feel like you are
working with JSON. It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

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

%check
%pytest -v

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

