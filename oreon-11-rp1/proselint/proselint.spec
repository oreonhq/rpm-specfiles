%global source0_hash 2568db94db227ea3aa011f88ddb6f554707b99b2c7447666bf00d71c5d7167cb
Name:           proselint
Version:        0.16.0
Release:        1%{?dist}
Summary:        A linter for English prose
License:        BSD-3-Clause
URL:            https://github.com/amperser/proselint
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-click
Requires:       python3-six
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.8.0
BuildRequires:  python3dist(uv-build) >= 0.7.22
Requires:       python3-proselint = %{version}-%{release}
# /oreon:deps
%description
proselint's goal is to aggregate knowledge about best practices in
writing and to make that knowledge immediately accessible to all authors
in the form of a linter for prose.  It is a command-line utility that
can be integrated into existing tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
