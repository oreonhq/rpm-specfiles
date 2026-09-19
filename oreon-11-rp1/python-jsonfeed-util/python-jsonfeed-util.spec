%global source0_hash 1aa4123307059a1a522033f00c17fa492bf7c2d0dc1eb877e518f5c30438e0fc

%bcond tests 1

Name:           python-jsonfeed-util
Version:        1.2.0
Release:        %autorelease
Summary:        Python package for parsing and generating JSON feeds

License:        MIT
URL:            https://github.com/lukasschwab/jsonfeed
# PyPI tarball is broken
Source:         %{url}/archive/%{version}/jsonfeed-%{version}.tar.gz
# Add license text
Patch:          %{url}/pull/13.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
jsonfeed is a Python package for parsing and constructing JSON Feeds. It
explicitly supports JSON Feed Version 1.1.}

%description %_description

%package -n     python3-jsonfeed-util
Summary:        %{summary}

%description -n python3-jsonfeed-util %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jsonfeed-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jsonfeed

# We don't want the tests package
rm -r %{buildroot}%{python3_sitelib}/tests

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-jsonfeed-util -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
