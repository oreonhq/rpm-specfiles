%global source0_hash 4265789ec59555a1f383ea2d75da085f78ee4cf1cd7c44a2b38662de02dd316f

Name:           libu2f-host
Version:        1.1.10
Release:        20%{?dist}
Summary:        Yubico Universal 2nd Factor (U2F) Host C Library

License:        GPLv3 and LGPLv2
URL:            http://developers.yubico.com/%{name}/
Source0:        http://developers.yubico.com/%{name}/releases/%{name}-%{version}.tar.xz

# https://github.com/Yubico/libu2f-host/pull/146
Patch0001:      libu2f-host-1.1.10_add_support_for_upcoming_json_c_0_14_0.patch

BuildRequires:  gcc
BuildRequires:  json-c-devel hidapi-devel
BuildRequires: make

# Bundled gnulib https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib)

# People using libu2f-host are actually using Yubikeys and
# will want them to be set up properly by udev
Requires:       u2f-hidraw-policy

%description
libu2f-host provides a C library that implements the host-side of the
U2F protocol. There are APIs to talk to a U2F device and perform the U2F
Register and U2F Authenticate operations.

%package -n u2f-host
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Command-line tool for U2F devices
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n u2f-host
u2f-host provides a command line tool that implements the host-side of the
U2F protocol.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed to develop applications that
use libu2f-host.

%global _hardened_build 1

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
LD_LIBRARY_PATH="$(pwd)/u2f-host/.libs" make check

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING.LGPLv2
%doc README AUTHORS NEWS THANKS ChangeLog doc/*
%{_libdir}/*.so.*

%files -n u2f-host
%license COPYING
%{_bindir}/u2f-host
%{_mandir}/man1/u2f-host.1*

%files devel
%doc %{_datadir}/gtk-doc
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*

%changelog
%autochangelog
