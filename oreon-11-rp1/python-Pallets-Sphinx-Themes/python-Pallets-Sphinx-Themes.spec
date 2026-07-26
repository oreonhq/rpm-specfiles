%global source0_hash 6293ced11a1d5d3de7268af1acd60428732b5a9e6051a47a596c6d9a083e60d9

%global pypi_name Pallets-Sphinx-Themes

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        %autorelease
Summary:        Sphinx themes for Pallets and related projects

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source0:        %{pypi_source pallets_sphinx_themes}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Pallets Sphinx Themes Themes for the Pallets projects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-sphinx
%description -n python3-%{pypi_name}
Pallets Sphinx Themes Themes for the Pallets projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pallets_sphinx_themes-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pallets_sphinx_themes

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CHANGES.rst

%changelog
%autochangelog
