%global source0_hash fdd1896c8de35a15eb14444d7880be81d635fcbbc4ad162d8bc3ccf5627aa8c7

%global git0 https://github.com/containers/%{name}

%{!?_modulesloaddir:%global _modulesloaddir %{_usr}/lib/modules-load.d}

Name: fuse-overlayfs
Version: 1.18
Release: %autorelease
ExclusiveArch: %{arm64} ppc64le s390x x86_64 riscv64
License: GPL-3.0-or-later
Summary: FUSE overlay+shiftfs implementation for rootless containers
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0:        https://github.com/containers/fuse-overlayfs/archive/refs/tags/v1.18.tar.gz#/fuse-overlayfs-1.18.tar.gz

BuildRequires: autoconf
BuildRequires: automake
Requires: fuse3
Requires: kmod
BuildRequires: fuse3-devel
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: make
BuildRequires: systemd-rpm-macros
Provides: bundled(gnulib) = cb634d40c7b9bbf33fa5198d2e27fdab4c0bf143

%description
%{summary}.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git %{name}-%{version}

%build
./autogen.sh
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__make}

%install
%make_install
install -d %{buildroot}%{_modulesloaddir}
echo fuse > %{buildroot}%{_modulesloaddir}/fuse-overlayfs.conf

%post
modprobe fuse > /dev/null 2>&1 || :

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_modulesloaddir}/fuse-overlayfs.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-1
- Prepare for Oreon 11 (RP1)
