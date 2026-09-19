%global source0_hash 14f207f8a94ada57cadd20e4ef82fd63ab3b17fff6ef1a5ed85dfeea3b759825

Name:           arptools
Summary:        Collection of libnet and libpcap based ARP utilities
License:        GPL-2.0-or-later

%global git_commit_full 2cf523f6fe6760da1eb3f97963f1975f96f6f106
%global git_commit %(c="%{git_commit_full}"; echo "${c:0:7}")
%global git_date 20230218

Version:        1.0.2
Release:        29.%{git_date}git%{git_commit}%{?dist}

URL:            https://github.com/burghardt/arptools
Source0:        %{URL}/archive/%{git_commit_full}/%{name}-%{git_commit_full}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel

%description
ARP Tools is collection of libnet and libpcap based ARP utilities.
It currently contains ARP Discover (arpdiscover), an Ethernet scanner based on
ARP protocol; ARP Flood (arpflood), an ARP request flooder; and ARP Poison
(arppoison), for poisoning switches' MAC address tables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{git_commit_full}

%build
chmod +x autogen.sh # yes, really
NOCONFIGURE="yes" ./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README.md TODO
%license COPYING
%{_sbindir}/arpdiscover
%{_sbindir}/arpflood
%{_sbindir}/arppoison

%changelog
%autochangelog
