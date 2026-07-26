%global source0_hash 87970442e2b6423fa352d5097adca6cbd2271e0ab258a2a2d8f1b51b20abcc12

%global snapshot 42ffc5f

Name:    sunxi-tools
Version: 1.4.2
Release: 24%{?snapshot:.%{snapshot}}%{?dist}
Summary: Tools to help hacking Allwinner (sunxi) based devices
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://linux-sunxi.org/Sunxi-tools

%if 0%{?snapshot:1}
# git archive --format=tar --prefix=%{name}-%{version}/ %{snapshot} | xz > %{name}-%{snapshot}.tar.xz
Source0: %{name}-%{snapshot}.tar.xz
%else
Source0: https://github.com/linux-sunxi/sunxi-tools/archive/v%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires: gcc
BuildRequires: libusbx-devel
BuildRequires: zlib-devel

%description
This package contains various tools to help hacking Allwinner (aka sunxi) based
devices and possibly it's successors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make %{?_smp_mflags} CFLAGS='%{optflags} -Iinclude -D_POSIX_C_SOURCE=200112L -std=c99'

%install
install -d %{buildroot}%{_bindir}
install sunxi-fel fel-gpio fex2bin sunxi-nand-part sunxi-fexc sunxi-pio %{buildroot}%{_bindir}
install sunxi-bootinfo %{buildroot}%{_bindir}/sunxi-bootinfo

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
