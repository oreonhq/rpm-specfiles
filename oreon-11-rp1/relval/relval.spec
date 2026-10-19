%global source0_hash 74c7c8ddbc28e4fa119a482bead5eed024e46d27144d2a4e3c6002e159248e0e
%global srcname relval
Name:           relval
Version:        2.7.7
Release:        1%{?dist}
Summary:        Tool for interacting with Fedora QA wiki pages
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/quality/relval
Source0:        https://forge.fedoraproject.org/quality/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-relval = %{version}-%{release}
# /oreon:deps
%description
Relval can perform various tasks related to Fedora QA by interacting with the
Fedora wiki. It lets you:

* Create wiki pages for Fedora release validation test events
* Generate statistics on release validation testing
* Report release validation test results using a console interface

See https://fedoraproject.org/wiki/QA/SOP_Release_Validation_Test_Event for
more information on the process relval helps with.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# setuptools-scm is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%tox
%files

%changelog

%autochangelog
