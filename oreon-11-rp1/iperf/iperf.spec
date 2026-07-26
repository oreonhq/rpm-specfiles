%global source0_hash 754ab0a7e28033dbea81308ef424bc7df4d6e2fe31b60cc536b61b51fefbd8fb

#%%global alphatag rc

Name: iperf
Version: 2.2.1
Release: 4%{?alphatag:.%{alphatag}}%{?dist}
Summary: Measurement tool for TCP/UDP bandwidth performance
License: BSD-3-Clause
URL: http://sourceforge.net/projects/iperf2
Source: http://sourceforge.net/projects/iperf2/files/%{name}-%{version}%{?alphatag:-%{alphatag}}.tar.gz
BuildRequires: gcc-c++
BuildRequires: make

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, datagram loss.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?alphatag:-%{alphatag}}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install

%files
%doc AUTHORS ChangeLog COPYING README doc/*.gif doc/*.html
%{_bindir}/iperf
%{_mandir}/man*/*

%changelog
%autochangelog
