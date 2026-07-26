%global source0_hash 782b366d1b649b809447191522141750ad5ab03dea4679ee8121f7099f5074fa

Name:           python-hiredis
Version:        3.3.0
Release:        %autorelease
Summary:        Python wrapper for hiredis

License:        BSD-2-Clause
URL:            https://github.com/redis/hiredis-py
Source:         %{url}/archive/v%{version}/python-hiredis-%{version}.tar.gz
# Drop vendor sources for hiredis and use the system one.
# Upstream issues (reported by OpenSUSE package mainteners):
# - https://github.com/redis/hiredis-py/issues/158
# - https://github.com/redis/hiredis-py/pull/159
# - https://github.com/redis/hiredis-py/pull/161
Patch0:         use-system-hiredis.patch
# Do not use load_module as it is deprecated from py34 and will be removed in py315
# https://github.com/redis/hiredis-py/pull/218
Patch1:         do-not-use-load_module.patch

BuildRequires: python3-devel
BuildRequires: hiredis-devel
BuildRequires: gcc
BuildRequires: python3dist(pytest)

Requires: hiredis

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Python extension that wraps protocol parsing code in hiredis.
It primarily speeds up parsing of multi bulk replies.}

%description %_description

%package -n     python3-hiredis
Summary:        %{summary}

%description -n python3-hiredis %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hiredis-py-%{version}
# Use system hiredis
rm -r vendor/hiredis

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hiredis

%check
%pyproject_check_import
%pytest --import-mode append

%files -n python3-hiredis -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
