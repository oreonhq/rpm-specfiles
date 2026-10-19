%global source0_hash 6001893f34e68a3cfeb5d424e1f2bfef005df96a22d86f35dc770c5bccf3aa8a
Name:           dbench
Version:        4.0 
Release:        1%{?dist}
Summary:        Filesystem load benchmarking tool
License:        GPL-2.0-or-later
Source0:        http://samba.org/ftp/tridge/dbench/dbench-%{version}.tar.gz
URL:            http://samba.org/ftp/tridge/dbench/README
Patch0:         dbench-4.0-destdir.patch
Patch1:         dbench-4.0-datadir.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
%description
Dbench is a file system benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring a
lab of Windows load generators to run. It is now considered a de facto
standard for generating load on the Linux VFS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .destdir 
%patch -P1 -p1 -b .datadir

%build

./autogen.sh 
%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}/man1 INSTALLCMD='install -p'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
