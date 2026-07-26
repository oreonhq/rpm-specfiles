%global source0_hash ba6ff0ed3e0acf645db9088262b8e0aac224f7950f99f5633f334c2fb6574c18

%global pypi_name pyconify

# Tests require network, so make sure network is enabled
%bcond tests 0

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        %{autorelease}
Summary:        Iconify for Python - universal icon framework

%global forgeurl https://github.com/pyapp-kit/pyconify
%global tag v%{version}
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For hatch-vcs
BuildRequires:  git-core
%if %{with tests}
# Test dependencies
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
Python wrapper for the Iconify API.

Iconify is a versatile icon framework that includes 100+ icon sets with
more than 100,000 icons from FontAwesome, Material Design Icons,
DashIcons, Feather Icons, EmojiOne, Noto Emoji and many other open
source icon sets.

Search for icons at: https://icon-sets.iconify.design}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git

# Make sure this is the last step in prep
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%if %{with tests}
# All tests require network for testing the Iconify API.
# So, we rely on upstreams testing and occasional network enabled builds.
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
