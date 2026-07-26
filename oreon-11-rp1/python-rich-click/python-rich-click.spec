%global source0_hash fd98c0ab9ddc1cf9c0b7463f68daf28b4d0033a74214ceb02f761b3ff2af3136

Name:           python-rich-click
Version:        1.8.9
Release:        %autorelease
Summary:        Format click help output nicely with rich

License:        MIT
URL:            https://github.com/ewels/rich-click
Source:         %{pypi_source rich_click}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
rich-click is a shim around Click that renders help output nicely using Rich.
The intention of rich-click is to provide attractive help output from Click,
formatted with Rich, with minimal customization required.}

%description %_description

%package -n     python3-rich-click
Summary:        %{summary}

%description -n python3-rich-click %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rich_click-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l rich_click

%check
%pyproject_check_import
# Revisit running upstream tests when
# https://github.com/ewels/rich-click/pull/247 is merged

%files -n python3-rich-click -f %{pyproject_files}
%_bindir/rich-click
%doc README.md

%changelog
%autochangelog
