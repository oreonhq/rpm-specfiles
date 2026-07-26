%global source0_hash 46e7565e2e14926ad6c05e4f1b8beb83f65b13db4c2711a56befdc8e1b42f687

%global srcname dirhash

Name:           python-%{srcname}
Version:        0.5.0
Release:        7%{?dist}
Summary:        Python module and CLI for hashing of file system directories

License:        MIT
URL:            https://github.com/andhus/dirhash-python
Source0:        https://github.com/andhus/dirhash-python/archive/v%{version}/%{srcname}-python-%{version}.tar.gz

# Needed to run tests outside of a venv - Not submitted upstream
Patch0:         %{srcname}-python-0.5.0-cli-test.patch

BuildArch:      noarch

%global _description %{expand:
A lightweight python module and CLI for computing the hash of any directory
based on its files' structure and content.

- Supports all hashing algorithms of Python's built-in hashlib module.
- Glob/wildcard (".gitignore style") path matching for expressive filtering
  of files to include/exclude.
- Multiprocessing for up to 6x speed-up

The hash is computed according to the Dirhash Standard, which is designed to
allow for consistent and collision resistant generation/verification of
directory hashes across implementations.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-python-%{version}

# Loosen pinned versioneer requirement
sed -i 's|versioneer==[0-9.]*|versioneer|g' pyproject.toml

# Drop shebangs from module
sed -i '1{s|^#!\(/usr\)\?/bin/\(env \)\?python\d\?$||}' src/dirhash/{cli.py,__init__.py}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%tox

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{srcname}

%changelog
%autochangelog
