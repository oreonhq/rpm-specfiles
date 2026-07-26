%global source0_hash e7cb6a7e6214e3ee88ae3ec2e796a689bca41dc0555806b44ea2689a31fd828e

Name:           python-patch-manager
Version:        0.0.6
Release:        %autorelease
Summary:        Patman patch manager

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/patman.html
Source:         %{pypi_source patch-manager}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

BuildRequires:  python3dist(pygit2)
BuildRequires:  python3dist(requests)

%global _description %{expand:
This package provides a tool intended to automate patch creation and make it a
less error-prone process. It is useful for U-Boot and Linux work so far, since
they use the checkpatch.pl script.}

%description %_description

%package -n     python3-patch-manager
Summary:        %{summary}

Requires:       python3dist(pygit2)
Requires:       python3dist(requests)

%description -n python3-patch-manager %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n patch-manager-%{version}

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/patman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files patman

%check
%pyproject_check_import -e patman.setup

%files -n python3-patch-manager -f %{pyproject_files}
%doc README.rst
%{_bindir}/patman

%changelog
%autochangelog
