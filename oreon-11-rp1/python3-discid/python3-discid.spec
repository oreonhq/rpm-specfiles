%global source0_hash 1e8e004220cba22651be124335a66f6bb30f458870e3dc4b7cac5eb2629c8016
Name:    python3-discid
Version: 1.4.2
Release:        1%{?dist}
Summary:        Libdiscid Python bindings
URL:     https://github.com/metabrainz/python-discid
License: LGPL-3.0-or-later
Source0:        https://github.com/metabrainz/python-discid/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: libdiscid
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-python3-discid = %{version}-%{release}
# /oreon:deps
%description
Python-discid implements Python bindings for MusicBrainz libdiscid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python-discid-%{version}
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
