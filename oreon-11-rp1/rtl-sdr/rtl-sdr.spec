%global source0_hash 851b87a62e548470c287c26669b83abb665d83bccb8d8492d07a697c7b9c4e37
%global __cmake_in_source_build 1
Name:             rtl-sdr
URL:              http://sdr.osmocom.org/trac/wiki/rtl-sdr
Version:          2.0.3
Release:        1%{?dist}
License:          GPL-2.0-or-later
Requires(pre):    glibc-common
Summary:        SDR utilities for Realtek RTL2832 based DVB-T dongles
Source0:        https://github.com/steve-m/librtlsdr/archive/refs/tags/v%{version}/librtlsdr-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libusbx-devel
# /oreon:deps
%description
This package can turn your RTL2832 based DVB-T dongle into a SDR receiver.

%package devel
Summary:          Development files for rtl-sdr
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         cmake-filesystem
%description devel
Development files for rtl-sdr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n librtlsdr-%%{git_commit}
%autosetup -p1 -n librtlsdr-%{version}
rm -f src/getopt/*
rmdir src/getopt

# Create a sysusers.d config file
cat >rtl-sdr.sysusers.conf <<EOF
g rtlsdr -
EOF

%build

%cmake -DDETACH_KERNEL_DRIVER=ON
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.a
sed -i 's/GROUP="plugdev"/GROUP="rtlsdr"/' ./rtl-sdr.rules
install -Dpm 644 ./rtl-sdr.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-rtl-sdr.rules
install -m0644 -D rtl-sdr.sysusers.conf %{buildroot}%{_sysusersdir}/rtl-sdr.conf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rtl-sdr-devel -f %{oreon_filedir}/rtl-sdr-devel.list

%changelog

%autochangelog
