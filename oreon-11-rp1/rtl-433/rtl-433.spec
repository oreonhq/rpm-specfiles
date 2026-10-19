%global source0_hash d95ae2263425d39644402eeff36821c03409930ed65014af99ed5178c95c9371
%global commit_date     20260106
%global commit_long     8d92cdd60def611865fb2cf2c4b3c7cdb4faf587
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})
Name: rtl-433
Version: 25.12
Release:        1%{?dist}
Summary:        Generic radio data receiver
License: GPL-2.0-only
Url: https://github.com/merbanan/rtl_433
Source0:        https://github.com/merbanan/rtl_433/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libusb1-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  sed
# /oreon:deps
%description
rtl_433 (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.

For more documentation and related projects see the https://triq.org/ site.

%package devel
Summary:    Development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n rtl_433-%{commit_long}

# Fix python shebang in examples
sed -ri 's\^#!/usr/bin/env python3?$\#!%{python3}\' examples/*.py

%build

%cmake \
        %{?fedora:-DCMAKE_POLICY_VERSION_MINIMUM=3.5}
%cmake_build
%install
%cmake_install
install -Dm 644 %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.example.conf %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf
for C in \
    'pulse_detect squelch' \
    'pulse_detect magest' \
    'samples_to_read 0' \
    'analyze_pulses false' \
    'device        0' \
    'pulse_detect autolevel' \
    'report_meta level' \
    'report_meta noise' \
    'report_meta stats' \
    'report_meta time:usec' \
    'report_meta protocol' \
    'signal_grabber none' \
    'output json' \
    'convert si' \
    'stop_after_successful_events false' \
;do
    sed -i 's\^'"$C"'$\'#"$C"'\' %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n rtl-433-devel -f %{oreon_filedir}/rtl-433-devel.list

%changelog

%autochangelog
