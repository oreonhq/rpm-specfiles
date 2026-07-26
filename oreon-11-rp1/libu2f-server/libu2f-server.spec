%global source0_hash a618f59051209d6d70c24cf42d64c9b67bd7dd5946b6dbd2c649181d7e8f1f6e

Name:		libu2f-server
Version:	1.0.1
Release:	34%{?dist}
Summary:	Yubico Universal 2nd Factor (U2F) Server C Library

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://developers.yubico.com/%{name}
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.xz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.xz.sig
Source2:	gpgkey-01F3D14D.gpg

# Picked from upstream
# https://github.com/Yubico/libu2f-server/commit/5d74f88b278ca1df6c69d7328be2a8035ca7976c
Patch0:		%{name}-1.0.1_fix_memory_errors.patch
# https://github.com/Yubico/libu2f-server/commit/72997944d5ee7f165fe04f1ac451d115e97d75e9
Patch1:		%{name}-1.0.1_check_result_json_object.patch
# https://github.com/Yubico/libu2f-server/pull/31
Patch2:		%{name}-1.0.1_fix_refcount_json_object.patch
# https://github.com/Yubico/libu2f-server/pull/42
Patch3:		%{name}-1.0.1_add_support_for_upcoming_json_c_0_14_0.patch

#BuildRequires:	json-c-devel openssl-devel check-devel gnupg2 systemd
BuildRequires:  gcc
BuildRequires:	json-c-devel openssl-devel check-devel systemd
BuildRequires: make

# Bundled gnulib https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(gnulib)

%description
This is a C library that implements the server-side of the U2F protocol. More
precisely, it provides an API for generating the JSON blobs required by U2F
devices to perform the U2F Registration and U2F Authentication operations, and
functionality for verifying the cryptographic operations.

%package -n u2f-server
Summary:	Server-side command-line tool for U2F devices
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n u2f-server
u2f-server provides a command line tool that implements the server-side of the
U2F protocol.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed to develop applications that
use libu2f-server.

%global _hardened_build 1

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# disable signature verficiation due to gpgv2 bug
# https://bugzilla.redhat.com/show_bug.cgi?id=1292687
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p 1

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
LD_LIBRARY_PATH="$(pwd)/u2f-server/.libs" make check

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc README AUTHORS NEWS THANKS
%{_libdir}/*.so.*

%files -n u2f-server
%{_bindir}/u2f-server
%{_mandir}/man1/u2f-server.1*

%files devel
%doc %{_datadir}/gtk-doc/html/u2f-server
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*

%changelog
%autochangelog
