%global source0_hash 61dbf97b1fde441bd03a5409874571e229898b67fb3080400837b8f4cee46659

%global pypi_name sphinx-typlog-theme
%global srcname sphinx_typlog_theme

%global _description %{expand:
A sphinx theme sponsored by Typlog, created by Hsiaoming Yang.}

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %autorelease
Summary:        A Sphinx theme sponsored by Typlog

License:        BSD-3-Clause
URL:            https://github.com/typlog/sphinx-typlog-theme
Source:         %{pypi_source}

# Contributed upstream: https://github.com/typlog/sphinx-typlog-theme/pull/26
Patch:          Ensure-compatibility-with-Sphinx-7.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(sphinx)

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
