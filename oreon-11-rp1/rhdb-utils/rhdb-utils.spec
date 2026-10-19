%global source0_hash 9ed1a30f719a5215ad5807c9094b987becc3ea6680979c20b874155c226075d7
%global tarballname REL_16_0
Summary:        Miscellaneous utilities for PostgreSQL - Red Hat Edition
Name: rhdb-utils
Version: 16.0
Release:        1%{?dist}
URL: https://github.com/df7cb/pg_filedump
License: GPL-2.0-or-later
Source0:        https://github.com/df7cb/pg_filedump/archive/refs/tags/%{tarballname}.tar.gz
Requires(pre): postgresql-server
Provides: pg_filedump = %{version}-%{release}
# oreon:deps
BuildRequires:  clang
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  postgresql-server-devel
BuildRequires:  postgresql-static
# /oreon:deps
%description
This package contains miscellaneous, non-graphical tools originally
developed for PostgreSQL - Red Hat Edition.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pg_filedump-%{tarballname} -p1

%build

make %{?_smp_mflags} PG_CONFIG=%_bindir/pg_server_config
%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -p -m 755 pg_filedump ${RPM_BUILD_ROOT}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
