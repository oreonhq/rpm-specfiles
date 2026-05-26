# Turn the tests off when bootstrapping Python, because pytest requires pluggy
%bcond tests 1

Name:           python-pluggy
Version:        1.6.0
Release:        5%{?dist}
Summary:        The plugin manager stripped of pytest specific details

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source:         %{pypi_source pluggy}
# oreon url source checksums begin
%global source0_sha256 7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3
%global source0_file pluggy-1.6.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
# the [testing] extra includes benchmarking dependencies
BuildRequires:  python3-pytest
%endif

%global _description\
The plugin manager stripped of pytest specific details.

%description %_description


%package -n python3-pluggy
Summary:  %summary

%description -n python3-pluggy %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pluggy-1.6.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3" || { echo "oreon: Source0 SHA256 mismatch for pluggy-1.6.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n pluggy-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pluggy


%if %{with tests}
%check
%pytest
%endif


%files -n python3-pluggy -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-5
- Prepare for Oreon 11 (RP1)
