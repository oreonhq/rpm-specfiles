%global source0_hash fc2350405956774f5993a0486d87245822d8aef71a0421af944cb91e8adf5422
%global forgeurl https://github.com/HewlettPackard/netperf
%global commit 3bc455b23f901dae377ca0a558e1e32aa56b31c4
%forgemeta
Name:           netperf
Version:        2.7.0
Release:        1%{?dist}
Summary:        Benchmark to measure the performance of many different types of networking
License:        MIT AND BSD-3-Clause AND BSD-4-Clause
URL:            https://hewlettpackard.github.io/netperf
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        netserver.service
Patch1:         %{forgeurl}/pull/63.patch
Patch2:         netperf-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo-tex
# /oreon:deps
%description
Netperf is a benchmark that can be used to measure the performance of many
different types of networking. It provides tests for both unidirectional
throughput, and end-to-end latency.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# remove prebuilt documentation
rm doc/netperf.{html,pdf}

%build

./autogen.sh
export CFLAGS="%{optflags} -fcommon -std=c99"
%configure \
  --enable-burst \
  --enable-dccp \
  --enable-demo \
  --enable-dirty \
  --enable-histogram \
  --enable-intervals \
  --enable-omni \
  --enable-sctp \
  --enable-unixdomain
%make_build
%make_build -C doc netperf.html netperf.pdf
%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} %SOURCE1
rm %{buildroot}%{_infodir}/dir
rm doc/examples/Makefile*
chmod -x doc/examples/*
%oreon_autofiles main

%post

%systemd_post netserver.service
%preun

%systemd_preun netserver.service
%postun

%systemd_postun_with_restart netserver.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
