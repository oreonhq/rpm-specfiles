%global source2_hash 0a6f979c9d88b0d72310b8462d2066a60b657a2f188a74c3cb19cac0064616ce
%global source1_hash bd65c7ac9a4d2c7bdc69409020294e7dec7664d343430ac2788d7a23e9ea3e48
%global source0_hash d064d28626fbf11318563fcd7158afb68eccbf34ddce46dddd847593114caf1f
Name:          growlight
Version:       1.2.41
Release:        1%{?dist}
Summary:        Disk manipulation and system setup tool
License:       GPL-3.0-or-later
URL:           https://nick-black.com/dankwiki/index.php/Growlight
Source0:        https://github.com/dankamongmen/%{name}/archive/v%{version}.tar.gz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:       https://nick-black.com/dankamongmen.gpg
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cryptsetup-devel
BuildRequires:  device-mapper-devel
BuildRequires:  doctest-devel
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libpciaccess-devel
BuildRequires:  pandoc
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(notcurses)
BuildRequires:  readline-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
