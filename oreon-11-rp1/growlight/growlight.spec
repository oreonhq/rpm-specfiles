%global source0_hash 9c8a5854ba30aa66a7b806b75f00784942f29711dbde0787a29f06583e6ec7a3

Name:          growlight
Version:       1.2.38
Release:       %autorelease
Summary:       Disk manipulation and system setup tool
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           https://nick-black.com/dankwiki/index.php/Growlight
Source0:       https://github.com/dankamongmen/%{name}/archive/v%{version}.tar.gz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:       https://nick-black.com/dankamongmen.gpg

BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: doctest-devel
BuildRequires: gcc-c++
BuildRequires: readline-devel
BuildRequires: libpciaccess-devel
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libatasmart)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(notcurses)
BuildRequires: device-mapper-devel
BuildRequires: cryptsetup-devel
BuildRequires: pandoc

%description
Growlight can manipulate both physical (NVMe, SATA, etc.) and virtual (mdadm,
device-mapper, etc.) block devices, help identify bottlenecks in a storage
topology, create and destroy filesystems, and prepare a machine for initial
boot when run in an installer context. Both full-screen and REPL readline UIs
are available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -DUSE_LIBZFS=off .
%cmake_build

%install
%cmake_install
mkdir -vp %{buildroot}%{_bindir}
mv -v %{buildroot}/usr/sbin/* %{buildroot}%{_bindir}

%files
%doc README.md
%license COPYING
%{_bindir}/growlight
%{_bindir}/growlight-readline
%{_mandir}/man8/*.8*
%{_datadir}/%{name}

%changelog
%autochangelog
