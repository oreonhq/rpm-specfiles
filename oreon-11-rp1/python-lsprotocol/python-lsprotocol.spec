%global source0_hash e879da2b9301e82cfc3e60d805630487ac2f7ab17492f4f5ba5aaba94fe56c29

Name:           python-lsprotocol
Version:        2025.0.0
Release:        %autorelease
Summary:        Python implementation of the Language Server Protocol

License:        MIT
URL:            https://pypi.org/project/lsprotocol/
Source:         %{pypi_source lsprotocol}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
lsprotocol is a python implementation of object types used in the Language
Server Protocol (LSP).}

%description %_description

%package -n     python3-lsprotocol
Summary:        %{summary}

%description -n python3-lsprotocol %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lsprotocol-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lsprotocol

%check
%pyproject_check_import

%files -n python3-lsprotocol -f %{pyproject_files}

%changelog
%autochangelog
