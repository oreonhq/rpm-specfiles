Name:           python-pathspec
Version:        1.0.4
Release:        %autorelease
Summary:        Utility library for gitignore style pattern matching of file paths

License:        MPL-2.0
URL:            https://github.com/cpburnz/python-path-specification
Source:         %{pypi_source pathspec}
# oreon url source checksums begin
%global source0_sha256 0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645
%global source0_file pathspec-1.0.4.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pathspec-1.0.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645" || { echo "oreon: Source0 SHA256 mismatch for pathspec-1.0.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
