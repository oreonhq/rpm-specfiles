%global source0_hash 6b094264c8d235178daf6249fb1e25561d35cdef8820097ff7aa582eb0a3be6d

%bcond tests 1

Name:           python-tcx2gpx
Version:        0.1.6
Release:        %autorelease
Summary:        Convert Garmin TPX to GPX

License:        GPL-3.0-only
URL:            https://gitlab.com/nshephard/tcx2gpx
Source:         %{pypi_source tcx2gpx}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This module converts the Garmin tcx GPS file format to the more commonly used
gpx file format. Both formats are a form of XML but there are some fields in
the former that are not present in the later. It uses two packages to do the
grunt work tcxparser and gpxpy.}

%description %_description

%package -n python3-tcx2gpx
Summary:        %{summary}

%description -n python3-tcx2gpx %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tcx2gpx-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem tool.pytest.ini_options.addopts \
    '^--cov.*'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tcx2gpx

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-tcx2gpx -f %{pyproject_files}
%doc README.md
%{_bindir}/tcx2gpx

%changelog
%autochangelog
