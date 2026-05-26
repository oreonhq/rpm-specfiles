# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
