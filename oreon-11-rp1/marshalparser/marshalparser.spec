Name:           marshalparser
Version:        0.5.0
Release:        %autorelease
Summary:        Parser for Python internal Marshal format

# SPDX
License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        https://github.com/fedora-python/marshalparser/archive/v0.5.0/marshalparser-0.5.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 4c1e5a4330047c7640d86c324ef458cf4f2a1e3756f38f3e510f88389d2a6f0e
%global source0_file marshalparser-0.5.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests on various pyc files
# We intentionally skip those on RHEL to avoid pulling other Pythons into next RHEL.
# When a new Python is added into RHEL, the new version should be explicitly added.
%if %{undefined rhel}
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3.6
BuildRequires:  python3.9
BuildRequires:  python3.10
BuildRequires:  python3.11
BuildRequires:  python3.12
BuildRequires:  python3.13
BuildRequires:  python3.14
BuildRequires:  python3.15
%endif

%generate_buildrequires
%pyproject_buildrequires -x test

%description
Parser for Python internal Marshal format which can fix pyc files
reproducibility.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/marshalparser-0.5.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4c1e5a4330047c7640d86c324ef458cf4f2a1e3756f38f3e510f88389d2a6f0e" || { echo "oreon: Source0 SHA256 mismatch for marshalparser-0.5.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%pytest %{?!rhel:-n auto}

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-1
- Prepare for Oreon 11 (RP1)
