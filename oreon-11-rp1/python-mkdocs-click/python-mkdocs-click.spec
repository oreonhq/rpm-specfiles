%global source0_hash 6050917628d4740517541422b607404d044117bc31b770c4f9e9e1939a50c908

Name:           python-mkdocs-click
Version:        0.9.0
Release:        %autorelease
Summary:        MkDocs extension to generate documentation for Click CLIs

License:        Apache-2.0
URL:            https://pypi.org/project/mkdocs-click/
Source:         %{pypi_source mkdocs_click}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides an MkDocs extension to generate documentation for Click
command line applications.}

%description %_description

%package -n     python3-mkdocs-click
Summary:        %{summary}

%description -n python3-mkdocs-click %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs_click-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_click

%check
%pytest

%files -n python3-mkdocs-click -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
