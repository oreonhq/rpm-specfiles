%global source0_hash a1196fdddf1e364b02ec68a05e8ff8f6914fee10fbca2e6b6735f166bb0da8d4

Name:           python-rich-rst
Version:        1.3.2
Release:        %autorelease
Summary:        A beautiful reStructuredText renderer for rich
License:        MIT
URL:            https://wasi-master.github.io/rich-rst
Source:         %{pypi_source rich_rst}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A beautiful reStructuredText renderer for rich.}

%description %_description

%package -n     python3-rich-rst
Summary:        %{summary}

%description -n python3-rich-rst %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rich_rst-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l rich_rst

%check
%pyproject_check_import
%pytest

%files -n python3-rich-rst -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
