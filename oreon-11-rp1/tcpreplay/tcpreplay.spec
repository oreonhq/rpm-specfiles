%global source0_hash 14b96e3565d6e66e813000d0d510afeaecb871f2b533182c391c6ccf948c3e21
%define pcapdep libpcap-devel
%define _legacy_common_support 1
Name:           tcpreplay
Version:        4.6.1
Release:        1%{?dist}
Summary:        Replay captured network traffic
License:        GPL-3.0-only
URL:            http://tcpreplay.appneta.com/
Source0:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/tcpreplay-%{version}.tar.xz
Patch0:         tcpreplay-4.5.2-txring_h.patch
Patch1:         tcpreplay-4.5.1-configure_ac.patch
Requires:       tcpdump
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tcpdump
# /oreon:deps
%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --enable-local-libopts \
           --disable-libopts-install \
           --disable-maintainer-mode
%{__sed} -i \
         -e 's/^CFLAGS.*/CFLAGS=${RPM_OPT_FLAGS} -std=gnu99 -D_U_="__attribute__((unused))" -Wno-format-contains-nul/' \
         $(find . -name Makefile)
%{__rm} -f docs/INSTALL docs/Makefile*
%{__chmod} -x src/*.c src/common/*.c
%{__make} %{?_smp_mflags}
%install
%{__rm} -rf %{buildroot}
%{__make} %{?_smp_mflags} DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
