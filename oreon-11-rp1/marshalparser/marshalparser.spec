# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 4c1e5a4330047c7640d86c324ef458cf4f2a1e3756f38f3e510f88389d2a6f0e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           marshalparser
Version:        0.5.0
Release:        %autorelease
Summary:        Parser for Python internal Marshal format

# SPDX
License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        https://github.com/fedora-python/marshalparser/archive/v0.5.0/marshalparser-0.5.0.tar.gz
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
%oreon_verify_sources
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
