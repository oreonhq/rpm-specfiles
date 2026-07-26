%global source0_hash 9abb95545d99a5f4c761fe042a4bdfdcadc635f3498792a17bd62ad7b2c4aafd

Name:           python-pbs-installer
Version:        2026.1.27
Release:        %autorelease

Summary:        Installer for Python Build Standalone

License:        MIT
URL:            https://pypi.org/project/pbs-installer/
Source:         %{pypi_source pbs_installer}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An installer for @indygreg's python-build-standalone (https://github.com/astral-sh/python-build-standalone).}

%description %_description

%package -n     python3-pbs-installer
Summary:        %{summary}

%description -n python3-pbs-installer %_description

%pyproject_extras_subpkg -n python3-pbs-installer all,download,install

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pbs_installer-%{version}

%generate_buildrequires
%pyproject_buildrequires -x all,download,install

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pbs_installer

%check
%pyproject_check_import

%files -n python3-pbs-installer -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pbs-install

%changelog
%autochangelog
