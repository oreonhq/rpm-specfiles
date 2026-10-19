%global source0_hash 72a8c13001dd512acff9b85594dd29a435947072e20abefe85c29468a3967121
%global _hardened_build 1
Name:		fprobe-ulog
Version:	1.2
Release:        1%{?dist}
Summary:        NetFlow probe
License:	GPLv2
URL:		https://github.com/opoplawski/fprobe-ulog
Source0:        https://github.com/opoplawski/fprobe-ulog/releases/download/v%{version}/fprobe-ulog-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libnetfilter_log-devel
BuildRequires:  make
# /oreon:deps
%description
fprobe-ulog - libipulog-based tool that collect network traffic data and emit
it as NetFlow flows towards the specified collector.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%{__make} %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT/%{_sbindir}/fprobe-ulog $RPM_BUILD_ROOT/%{_bindir}/fprobe-ulog
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
