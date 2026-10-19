%global source0_hash 24beb74e7b96c5c6368cd3c198c03271d9c6c1f6f8c9a4df232b499f5c042835
%global date 20250709
%global commit 2ecffa6df3f0fd5b0bd23d2361178d2613f3786b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           packetdrill
Version:        2.0~%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Quick, precise tests for entire TCP/UDP/IPv4/IPv6 network stacks
License:        GPL-2.0-only
URL:            https://github.com/google/packetdrill
Source0:        https://github.com/google/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         %{url}/pull/56.patch
Patch2:         %{url}/pull/93.patch
Recommends:     %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  emacs
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  sed
BuildRequires:  vim-filesystem
# /oreon:deps
%description
The packetdrill scripting tool enables quick, precise tests for entire
TCP/UDP/IPv4/IPv6 network stacks, from the system call layer down to the NIC
hardware. packetdrill currently works on Linux, FreeBSD, OpenBSD, and NetBSD.
It can test network stack behavior over physical NICs on a LAN, or on a single
machine using a tun virtual network device.

%package        data
Summary:        Data files for %{name}
Requires:       bash
Requires:       coreutils
Requires:       emacs-filesystem
Requires:       iproute
Requires:       procps-ng
Requires:       python3
Requires:       vim-filesystem
Suggests:       emacs
Suggests:       vim
BuildArch:      noarch
%description    data
This package contains a test runner, test scripts, and editor configs for
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

# Fix paths in the test runner
sed -i gtests/net/packetdrill/run_all.py \
    -e 's:bin_path = .*:bin_path = "%{_bindir}/%{name}":' \
    -e 's:nswrap_path = .*:nswrap_path = "%{_datadir}/%{name}/in_netns.sh":'

%build

pushd gtests/net/%{name}
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%{_emacs_bytecompile} contrib/%{name}.el
%install
install -Dpm0755 -t %{buildroot}%{_bindir} \
%if 0%{?el8}
  gtests/net/%{name}/%{name}
%else
  gtests/net/%{name}/%{_vpath_builddir}/%{name}
%endif
install -Dpm0755 -t %{buildroot}%{_datadir}/%{name} \
  gtests/net/%{name}/{in_netns.sh,run_all.py}
cp -PR gtests/net/{common,tcp}/ %{buildroot}%{_datadir}/%{name}/
install -Dpm0644 -t %{buildroot}%{_emacs_sitelispdir} \
  gtests/net/%{name}/contrib/%{name}.{el,elc}
install -Dpm0644 -t %{buildroot}%{vimfiles_root}/syntax \
  gtests/net/%{name}/contrib/%{name}.vim
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for t in packet_parser_test packet_to_string_test; do
%if 0%{?el8}
  ./gtests/net/%{name}/${t}
%else
  ./gtests/net/%{name}/%{_vpath_builddir}/${t}
%endif
done
%files -f %{oreon_filedir}/main.list
%files -n packetdrill-data -f %{oreon_filedir}/packetdrill-data.list

%changelog

%autochangelog
