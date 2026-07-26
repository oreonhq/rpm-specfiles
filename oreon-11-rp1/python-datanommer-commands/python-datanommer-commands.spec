%global source0_hash b108dfe898a8291d2d087b86e4171d2d5e930498f12f3a6d5a1a6b86386442dc

Name:           python-datanommer-commands
Version:        1.5.0
Release:        1%{?dist}
Summary:        Console commands for datanommer

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/datanommer.commands
Source:         %{pypi_source datanommer_commands}

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-postgresql)

%global _description %{expand:
Console commands for datanommer. }

%description %_description

%package -n python3-datanommer-commands
Summary:        %{summary}

%description -n python3-datanommer-commands %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n datanommer_commands-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L datanommer

# The tests suites requires the messaging schema that are currently not packaged
# in Fedora. We can try to make the %%pytest macro running later when they are available.
%check
%pyproject_check_import -t

%files -n python3-datanommer-commands -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/datanommer-create-db
%{_bindir}/datanommer-dump
%{_bindir}/datanommer-extract-users
%{_bindir}/datanommer-latest
%{_bindir}/datanommer-stats
%{_bindir}/datanommer-refresh-view

%changelog
%autochangelog
