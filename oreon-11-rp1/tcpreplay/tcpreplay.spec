%global source0_hash 2df15bc6d49f96a77617d137049f998193bbae95c1a31b04ca02856a24cbf384

# EL4 doesn't have libpcap-devel
%if 0%{?rhel} && 0%{?rhel} < 5
%define pcapdep libpcap
%else
%define pcapdep libpcap-devel
%endif

# GCC 10 uses -fno-common by default, turn it off for now
%define _legacy_common_support 1

Name:           tcpreplay
Version:        4.5.2
Release:        2%{?dist}
Summary:        Replay captured network traffic

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://tcpreplay.appneta.com/
Source:         https://github.com/appneta/tcpreplay/releases/download/v%{version}/tcpreplay-%{version}.tar.xz
Patch0:         tcpreplay-4.5.2-txring_h.patch
Patch1:         tcpreplay-4.5.1-configure_ac.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  %{pcapdep} >= 0.8.0, tcpdump
%if ! 0%{?rhel}
BuildRequires:  libdnet-devel
%endif
Requires:       tcpdump

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vif
%configure --enable-local-libopts \
           --disable-libopts-install \
           --disable-maintainer-mode

# make sure we use proper CFLAGS
%{__sed} -i \
         -e 's/^CFLAGS.*/CFLAGS=${RPM_OPT_FLAGS} -std=gnu99 -D_U_="__attribute__((unused))" -Wno-format-contains-nul/' \
         $(find . -name Makefile)

# remove unneeded docs
%{__rm} -f docs/INSTALL docs/Makefile*

# fix wrong permissions
%{__chmod} -x src/*.c src/common/*.c

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%doc docs/*
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
