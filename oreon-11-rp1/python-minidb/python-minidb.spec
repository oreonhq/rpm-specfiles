%global source0_hash f177870a9f44ff834aa7986ebb9451445a5afa8e756ab400c16ea1d746441aaf

%global pypi_name minidb

Name:           python-%{pypi_name}
Version:        2.0.8
Release:        %autorelease
Summary:        Simple python object store

License:        ISC
URL:            https://github.com/thp/minidb
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

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
%pytest -v test

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
