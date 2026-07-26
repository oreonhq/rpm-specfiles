%global source0_hash e41d0c6f12575c152efb9478e34313aac4b18e4f8378bbd3e65bed0d65e7e713

%global         pypi_name cli_helpers

Summary:        Python helpers for common CLI tasks
Name:           python-cli-helpers
Version:        2.10.1
Release:        1%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dbcli/cli_helpers
Source0:        https://github.com/dbcli/cli_helpers/archive/v%{version}/cli_helpers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-configobj
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-tabulate
BuildRequires:  python3-terminaltables
BuildRequires:  python3-wcwidth
%global _description\
CLI Helpers is a Python package that makes it easy to perform common\
tasks when building command-line apps. Its a helper library for\
command-line interfaces.
%description %_description

%package -n     python3-cli-helpers
Summary:        %{summary}
Requires:       python3-configobj >= 5.0.5
Requires:       python3-pygments >= 1.6
Requires:       python3-tabulate >= 0.8.2
Requires:       python3-terminaltables >= 3.0.0
Requires:       python3-wcwidth
%description -n python3-cli-helpers %_description

%pyproject_extras_subpkg -n python3-cli-helpers styles

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

PYTHONPATH=build/lib/ py.test-3

%files -n python3-cli-helpers -f %{pyproject_files}
%doc AUTHORS CHANGELOG README.rst

%changelog
%autochangelog
