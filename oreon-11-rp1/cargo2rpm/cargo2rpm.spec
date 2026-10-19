%global source0_hash 98c8e1a8a124577c9bf2785533cb058f135534761a48de9acd499ef50f3c4353
%bcond_without check
Name:           cargo2rpm
Version:        0.4.0
Release:        1%{?dist}
Summary:        Translation layer between cargo and RPM
License:        MIT
URL:            https://codeberg.org/rust2rpm/cargo2rpm
Source0:        https://codeberg.org/rust2rpm/cargo2rpm/archive/v%{version}.tar.gz
BuildArch:      noarch
%if %{with check}
%endif
Requires:       cargo
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cargo2rpm = %{version}-%{release}
# /oreon:deps
%description
cargo2rpm implements a translation layer between cargo and RPM. It
provides a CLI interface (for implementing RPM macros and generators)
and a Python API (which rust2rpm is built upon).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cargo2rpm
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%if %{with check}
%pytest
%endif
%files

%changelog

%autochangelog
