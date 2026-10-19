%global source0_hash baa5a9aa1726b97240e16fef8856395cd42440aee410bf479479249f9cce6076
Name:           dvblast
Version:        3.5
Release:        1%{?dist}
Summary:        Simple and powerful streaming application
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/projects/dvblast.html
Source0:        https://downloads.videolan.org/pub/videolan/dvblast/%{version}/dvblast-%{version}.tar.bz2
# oreon:deps
BuildRequires:  bitstream-devel
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  make
# /oreon:deps
%description
DVBlast is a simple and powerful streaming application based on the
linux-dvb API. It opens a DVB device, tunes it, places PID filters,
configures a CAM module, and demultiplexes the packets to several RTP
outputs. It supports the new S2API of linux-dvb (compile option).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Prepare dvbiscovery
sed -i -e 's|/usr/local|/usr|' extra/dvbiscovery/dvbiscovery.sh
install -pm 0644 extra/dvbiscovery/README README.dvbiscovery

%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build V=1
%install
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_datadir}/%{name}/dvbiscovery
install -pm 0644 extra/dvbiscovery/*.conf \
  %{buildroot}%{_datadir}/%{name}/dvbiscovery
install -pm 0755 extra/dvbiscovery/dvbiscovery.sh %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
