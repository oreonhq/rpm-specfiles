%global source0_hash 036855660225cb3817a190fc00e6764ce7836051bacb48d35e26444b8c1729d9
%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}
Summary:        MinGW library for handling page faults in user mode
Name:    mingw-libsigsegv
Version: 2.15
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     http://libsigsegv.sourceforge.net/
Source0:        http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
Patch100: libsigsegv-2.6-mystack.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
# /oreon:deps
%description
MinGW library for handling memory faults and stack overflows in user mode.

%package -n mingw32-libsigsegv
Summary:        MinGW library for handling page faults in user mode
%description -n mingw32-libsigsegv
MinGW library for handling memory faults and stack overflows in user mode.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libsigsegv-%{version}

%patch -P100 -p1 -b .mystack
autoreconf --install --force

%build

%{mingw32_configure} --disable-static --enable-shared
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libsigsegv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libsigsegv -f %{oreon_filedir}/mingw32-libsigsegv.list

%changelog

%autochangelog
