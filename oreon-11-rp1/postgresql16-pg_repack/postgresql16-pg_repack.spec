%global source0_hash 4516cad42251ed3ad53ff619733004db47d5755acac83f75924cd94d1c4fb681
%{!?postgresql_default:%global postgresql_default 0}
%global majorname pg_repack
%global pgversion 16
Name:           postgresql%{pgversion}-%{majorname}
Version:        1.5.2
Release:        1%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks
License:        BSD-3-Clause
URL:            http://reorg.github.io/%{majorname}/
Source0:        https://github.com/reorg/%{majorname}/archive/refs/tags/ver_%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %?postgresql_default
%global pkgname %{majorname}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  postgresql16-server
BuildRequires:  postgresql16-server-devel
BuildRequires:  postgresql16-static
BuildRequires:  python3-docutils
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%package -n %{pkgname}
Summary: Reorganize tables in PostgreSQL databases without any locks
%else
%global pkgname %name
%endif
BuildRequires: make
BuildRequires:  gcc, openssl-devel, lz4-devel, libzstd-devel
BuildRequires:  postgresql16-server-devel
BuildRequires:  postgresql16-server
BuildRequires:  postgresql16-static
BuildRequires:  readline-devel, zlib-devel
BuildRequires:  python3-docutils
Requires(pre):  postgresql16-server
%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: postgresql-%{majorname} = %precise_version
Provides: %name = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{majorname}-any
Conflicts: %{majorname}-any
%description
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.

%if %?postgresql_default
%description -n %{pkgname}
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -n %{majorname}-ver_%{version} -q

%build

make %{?_smp_mflags}
cd doc
make
%install
%make_install
%oreon_autofiles main
%if %?postgresql_default
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-3
- Import
%endif
