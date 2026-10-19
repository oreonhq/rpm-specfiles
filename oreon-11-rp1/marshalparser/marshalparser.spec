%global source0_hash 4c1e5a4330047c7640d86c324ef458cf4f2a1e3756f38f3e510f88389d2a6f0e
Name:           marshalparser
Version:        0.5.0
Release:        1%{?dist}
Summary:        Parser for Python internal Marshal format
License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        https://github.com/fedora-python/marshalparser/archive/refs/tags/v0.5.0.tar.gz#/marshalparser-0.5.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-marshalparser = %{version}-%{release}
# /oreon:deps
%description
Parser for Python internal Marshal format which can fix pyc files
reproducibility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest %{?!rhel:-n auto}
%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-1
- Prepare for Oreon 11 (RP1)
