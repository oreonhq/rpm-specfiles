%global source0_hash 0cc2c5d31f64fff48b7834ab11e44dfb438e23f41b6e7ead198e2098686133e7

%global srcname scantree

Name:           python-%{srcname}
Version:        0.0.4
Release:        7%{?dist}
Summary:        Flexible recursive directory iterator

License:        MIT
URL:            https://github.com/andhus/%{srcname}
Source0:        https://github.com/andhus/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Recursive directory iterator supporting:
- flexible filtering including wildcard path matching
- in memory representation of file-tree (for repeated access)
- efficient access to directory entry properties (posix.DirEntry interface)
  extended with real path and path relative to the recursion root directory
- detection and handling of cyclic symlinks

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
Recursive directory iterator supporting:
- flexible filtering including wildcard path matching
- in memory representation of file-tree (for repeated access)
- efficient access to directory entry properties (posix.DirEntry interface)
  extended with real path and path relative to the recursion root directory
- detection and handling of cyclic symlinks

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
