%global source0_hash 5e12eb3aefe9050068af7df2c663edabc977ef34c9e7ba7b9d2c43e0ad47d8df
Name: lmdbxx
Version: 1.0.0
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Summary:        C++ wrapper for the LMDB embedded B+ tree database library
URL: https://github.com/hoytech/%{name}
Source0:        https://github.com/hoytech/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lmdbxx-devel -f %{oreon_filedir}/lmdbxx-devel.list

%changelog

%autochangelog
