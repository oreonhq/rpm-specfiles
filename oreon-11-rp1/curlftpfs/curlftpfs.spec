%global source0_hash 4eb44739c7078ba0edde177bdd266c4cfb7c621075f47f64c85a06b12b3c6958

Name: curlftpfs
Version: 0.9.2
Release: 43%{?dist}
Summary: CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and libcurl
URL: http://curlftpfs.sourceforge.net/
# Code does not specify a version of the license.
License: GPL-1.0-or-later
Requires: fuse
Source: http://downloads.sourceforge.net/curlftpfs/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: curl-devel >= 7.15.2 fuse-devel glib2-devel
BuildRequires: make
# https://bugzilla.redhat.com/show_bug.cgi?id=831417
Patch1: curlftpfs-0.9.2-offset_64_another.patch
# https://code.google.com/p/curlftpfs/issues/detail?id=6 (bz#962015)
Patch2: curlftpfs-0.9.2-create-fix.patch
# Aarch64 support, Fedora-specific. bz#925209
Patch3: curlftpfs-0.9.2-aarch64.patch

# Fix memleaks 2 patches (one upstream report: https://code.google.com/p/curlftpfs/issues/detail?id=10)
Patch4: curlftpfs-0.9.2-memleak#591298.patch
Patch5: curlftpfs-0.9.2-memleak-cached#591299.patch
Patch6: curlftpfs-c99.patch

%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. It features SSL support, connecting through tunneling HTTP
proxies, and automatically reconnecting if the server times out.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .offset
%patch -P2 -p1 -b .create-fix
%patch -P3 -p1 -b .aarch64
%patch -P4 -p1 -b .memleak
%patch -P5 -p1 -b .memleak-cached
%patch -P6 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/curlftpfs
%{_mandir}/*/curlftpfs.*
%doc README
%doc COPYING

%changelog
%autochangelog
