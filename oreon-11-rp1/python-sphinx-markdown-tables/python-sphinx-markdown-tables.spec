%global source0_hash 6bc6d3d400eaccfeebd288446bc08dd83083367c58b85d40fe6c12d77ef592f1

%global srcname sphinx-markdown-tables

Name:           python-%{srcname}
Version:        0.0.17
Release:        14%{?dist}
Summary:        Sphinx extension for rendering markdown tables
License:        GPL-3.0-only

URL:            https://github.com/ryanfox/%{srcname}
Source0:        %{pypi_source %srcname}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A Sphinx extension for rendering tables written in markdown.

%package -n python3-%{srcname}
Summary:        Sphinx extension for rendering markdown tables

%description -n python3-%{srcname}
A Sphinx extension for rendering tables written in markdown.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
# Fix exec perms on LICENSE
chmod -x LICENSE

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_markdown_tables

# Drop incorrectly installed LICENSE
rm -f %{buildroot}%{_prefix}/LICENSE

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
