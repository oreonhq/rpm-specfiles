# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-pathspec
Version:        1.0.4
Release:        %autorelease
Summary:        Utility library for gitignore style pattern matching of file paths

License:        MPL-2.0
URL:            https://github.com/cpburnz/python-path-specification
Source:         %{pypi_source pathspec}

BuildArch:      noarch
BuildRequires:  python3-devel

# Tests require pytest which requires python-iniconfig, which in turn
# requires python-hatchling, requiring python-pathspec
# Conditionalize to make new Python bootstrap possible
%bcond tests 1

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.


%package -n     python3-pathspec
Summary:        %{summary}

%description -n python3-pathspec
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.


%prep
%oreon_verify_sources
%autosetup -n pathspec-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pathspec


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-pathspec -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-1
- Prepare for Oreon 11 (RP1)
