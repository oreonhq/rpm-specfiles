%global source0_hash b108dfe898a8291d2d087b86e4171d2d5e930498f12f3a6d5a1a6b86386442dc
Name:           python-datanommer-commands
Version:        1.5.0
Release:        1%{?dist}
Summary:        Console commands for datanommer
License:        GPL-3.0-or-later
URL:            https://pypi.org/project/datanommer.commands
Source0:        https://files.pythonhosted.org/packages/source/d/datanommer_commands/datanommer_commands-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-datanommer-commands = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-datanommer-commands
Summary:        Console commands for datanommer
%description -n python3-datanommer-commands

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir datanommer_commands-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-datanommer-commands usr/lib/python3*/site-packages/datanommer_commands* usr/lib64/python3*/site-packages/datanommer_commands* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/datanommer_commands* usr/lib64/python3*/site-packages/datanommer_commands* usr/bin/*

%check

%pyproject_check_import -t
%files
%files -n python3-datanommer-commands -f %{oreon_filedir}/python3-datanommer-commands.list

%changelog

%autochangelog
