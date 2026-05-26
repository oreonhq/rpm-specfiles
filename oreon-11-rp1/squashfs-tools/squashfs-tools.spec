# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 91c49f9a1ed972ad00688a38222119e2baf49ba74cf5fda05729a79d7d59d335
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: squashfs-tools
Version: 4.7.4
Summary: Utility for the creation of squashfs filesystems
%global forgeurl https://github.com/plougher/%{name}
%global tag %{version}
%forgemeta
URL:	 %{forgeurl}
Source:  %{forgesource}
Release: 1%{dist}
License: GPL-2.0-or-later

BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: lzo-devel
BuildRequires: libattr-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
BuildRequires: help2man

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%oreon_verify_sources
%forgesetup

%build
%set_build_flags
pushd squashfs-tools
CFLAGS="%optflags" XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1 LZ4_SUPPORT=1 ZSTD_SUPPORT=1 make %{?_smp_mflags}

%install
pushd squashfs-tools
make INSTALL_PREFIX=%{buildroot}/usr INSTALL_DIR=%{buildroot}%{_sbindir} INSTALL_MANPAGES_DIR=%{buildroot}%{_mandir}/man1 install

%check
[[ $(squashfs-tools/mksquashfs -version) =~ "%{version}" ]]

%files
%doc ACKNOWLEDGEMENTS README* CHANGES COPYING

%{_mandir}/man1/mksquashfs.1.gz
%{_mandir}/man1/unsquashfs.1.gz
%{_mandir}/man1/sqfstar.1.gz
%{_mandir}/man1/sqfscat.1.gz

%{_sbindir}/mksquashfs
%{_sbindir}/unsquashfs
%{_sbindir}/sqfstar
%{_sbindir}/sqfscat

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.7.4-1
- Prepare for Oreon 11 (RP1)
