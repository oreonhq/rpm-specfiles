%global source0_hash 45a321c83f64267d82907492c55199fccabda45bc872dd23bf1efd08edac1b0b

Name:           python-pyls-spyder
Version:        0.4.0
Release:        %autorelease
Summary:        Spyder extensions for the python-language-server (pyls)

# SPDX
License:        MIT
URL:            https://github.com/spyder-ide/pyls-spyder
Source:         %{pypi_source pyls-spyder}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%package -n     python3-pyls-spyder
Summary:        %{summary}

%description -n python3-pyls-spyder %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyls-spyder-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyls_spyder

%check
# Upstream provides no tests
%pyproject_check_import

%files -n python3-pyls-spyder -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
