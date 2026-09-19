%global source0_hash 5e12eb3aefe9050068af7df2c663edabc977ef34c9e7ba7b9d2c43e0ad47d8df

Name: lmdbxx
Version: 1.0.0
Release: 12%{?dist}

License: LicenseRef-Fedora-Public-Domain
Summary: C++ wrapper for the LMDB embedded B+ tree database library
URL: https://github.com/hoytech/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: make

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Requires: lmdb-devel
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files devel
%doc README.md FUNCTIONS.rst AUTHORS CREDITS VERSION
%license UNLICENSE
%{_includedir}/lmdb++.h

%changelog
%autochangelog
