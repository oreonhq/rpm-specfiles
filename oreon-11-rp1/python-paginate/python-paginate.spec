%global source0_hash 88eaa65ea111e533542cdd4c8e9f90e5beefaabcf3d62021fb4d1113351bc9c6

%global srcname paginate

Name:           python-%{srcname}
Version:        0.5.7
Release:        %autorelease
Summary:        Divides large result sets into pages for easier browsing

License:        MIT
URL:            https://github.com/Signum/paginate
# PyPI tarball does not include tests
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This module helps dividing large lists of items into pages. The user is shown
one page at a time and can navigate to other pages.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.txt TODO

%changelog
%autochangelog
