%global source0_hash 9dbb07ea0d6a0b4fb607004be66e540df1a518c5431cc1e9ea542582abd7711f

Name:    python3-discid
Version: 1.3.0
Release: %autorelease
Summary: Libdiscid Python bindings
URL:     https://github.com/metabrainz/python-discid
License: LGPL-3.0-or-later

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: libdiscid
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

Requires: libdiscid

%description
Python-discid implements Python bindings for MusicBrainz libdiscid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-discid-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files discid

%check
%pytest

%files -f %{pyproject_files}
%license COPYING COPYING.LESSER
%doc README.rst CHANGES.rst

%changelog
%autochangelog
