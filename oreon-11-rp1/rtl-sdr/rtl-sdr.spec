%global source0_hash e108d3c6a00efcdf55877d1172be538842686c50377043319baffcfdb6b7b9cb

%global __cmake_in_source_build 1
#%%global git_commit 1261fbb285297da08f4620b18871b6d6d9ec2a7b
#%%global git_date 20230921

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

# git clone git://git.osmocom.org/gr-osmosdr
# cd %%{name}
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:             rtl-sdr
URL:              http://sdr.osmocom.org/trac/wiki/rtl-sdr
#Version:          0.6.0^%%{git_suffix}
Version:          2.0.1
Release:          7%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
BuildRequires:    gcc
BuildRequires:    cmake
BuildRequires:    libusbx-devel
#BuildRequires:    libusb1-devel
Requires(pre):    glibc-common
Summary:          SDR utilities for Realtek RTL2832 based DVB-T dongles
#Source0:          https://github.com/steve-m/librtlsdr/archive/%%{git_commit}/librtlsdr-%%{git_commit}.tar.gz
Source0:          https://github.com/steve-m/librtlsdr/archive/refs/tags/v%{version}/librtlsdr-%{version}.tar.gz
#Source0:          https://github.com/steve-m/librtlsdr/archive/%%{version}/librtlsdr-%%{version}.tar.gz
# https://osmocom.org/projects/rtl-sdr/repository/revisions/222517b506278178ab93182d79ccf7eb04d107ce

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

# remove static libs
rm -f %{buildroot}%{_libdir}/*.a

# Fix udev rules and allow access only to users in rtlsdr group
sed -i 's/GROUP="plugdev"/GROUP="rtlsdr"/' ./rtl-sdr.rules
install -Dpm 644 ./rtl-sdr.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-rtl-sdr.rules

install -m0644 -D rtl-sdr.sysusers.conf %{buildroot}%{_sysusersdir}/rtl-sdr.conf

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_bindir}/*
%{_libdir}/*.so.*
%{_prefix}/lib/udev/rules.d/10-rtl-sdr.rules
%{_sysusersdir}/rtl-sdr.conf

%files devel
%{_includedir}/*
%{_libdir}/cmake/rtlsdr
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
