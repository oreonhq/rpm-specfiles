%global source0_hash 436f93b1141be0abe593710947307d8f91129a5353c3a8c3c29e2ba0355e171e

%global _hardened_build 1

Summary:       Network traffic recorder
Name:          tcpflow
Version:       1.6.1
Release:       14%{?dist}
License:       GPL-1.0-or-later
URL:           https://github.com/simsong/tcpflow
Source0:       http://digitalcorpora.org/downloads/tcpflow/tcpflow-%{version}.tar.gz
Patch0:        tcpflow-1.6.1-format.patch
Patch1:        tcpflow-1.6.1-uint.patch
BuildRequires: make
BuildRequires: boost-devel
#BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
%description
tcpflow is a program that captures data transmitted as part of TCP
connections (flows), and stores the data in a way that is convenient
for protocol analysis or debugging. A program like 'tcpdump' shows a
summary of packets seen on the wire, but usually doesn't store the
data that's actually being transmitted. In contrast, tcpflow
reconstructs the actual data streams and stores each flow in a
separate file for later analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CPPFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%check
make check || :

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/tcpflow
%{_mandir}/man1/tcpflow.1*

%changelog
%autochangelog
