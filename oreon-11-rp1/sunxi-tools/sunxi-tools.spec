%global source0_hash 87970442e2b6423fa352d5097adca6cbd2271e0ab258a2a2d8f1b51b20abcc12
%global snapshot 42ffc5f
Name:    sunxi-tools
Version: 1.4.2
Release:        1%{?dist}
Summary:        Tools to help hacking Allwinner (sunxi) based devices
License: GPL-2.0-or-later
URL:     http://linux-sunxi.org/Sunxi-tools
%if 0%{?snapshot:1}
Source0:        %{name}-%{snapshot}.tar.xz
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
This package contains various tools to help hacking Allwinner (aka sunxi) based
devices and possibly it's successors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make %{?_smp_mflags} CFLAGS='%{optflags} -Iinclude -D_POSIX_C_SOURCE=200112L -std=c99'
%install
install -d %{buildroot}%{_bindir}
install sunxi-fel fel-gpio fex2bin sunxi-nand-part sunxi-fexc sunxi-pio %{buildroot}%{_bindir}
install sunxi-bootinfo %{buildroot}%{_bindir}/sunxi-bootinfo
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
