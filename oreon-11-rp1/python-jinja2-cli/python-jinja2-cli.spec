%global source0_hash 089f1201ed1a812cb558f15b09c74aec1885ae00bf206512e79d55cebb2858fc

%global pypi_name jinja2-cli
%global _docdir_fmt %{name}

%global sum CLI interface to Jinja2
%global desc A CLI interface to Jinja2 which supports data in ini, json, querystring, yaml, \
yml and toml formats.

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        %sum

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/mattrobenolt/jinja2-cli/archive/0.8.2/jinja2-cli-0.8.2.tar.gz

# Drop python-toml dependency
# Cherry-picked from: https://github.com/mattrobenolt/jinja2-cli/pull/138
Patch:          138.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-jinja2

%description
%desc

%package -n     python3-%{pypi_name}
Summary:        %sum
BuildArch:      noarch
Requires:       python3-jinja2
Requires:       python3-PyYAML

%description -n python3-%{pypi_name}
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pypi_name}-%{version}
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jinja2cli

# Remove tests from install (not good folder)
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%pyproject_check_import

# Copy test template
py.test-%{python3_version}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jinja2

%changelog
%autochangelog
