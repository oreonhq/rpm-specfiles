%global source0_hash 42c1f2dc2ee9fa898c620e011f226de0d90ab4cd2640560199d7f919589a591b

Name:           python-mkdocs-d2-plugin
Version:        1.6.0
Release:        %autorelease
Summary:        D2 plugin for MkDocs

License:        MIT
URL:            https://github.com/landmaj/mkdocs-d2-plugin
Source:         %{pypi_source mkdocs_d2_plugin}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a plugin for embedding D2 diagrams in MkDocs.}

%description %_description

%package -n     python3-mkdocs-d2-plugin
Summary:        %{summary}
Requires:       d2

%description -n python3-mkdocs-d2-plugin %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs_d2_plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l d2

%check
%pyproject_check_import

%files -n python3-mkdocs-d2-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
