Name:           libestr
Version:        0.1.11
Release:        13%{?dist}
Summary:        String handling essentials library

License:        LGPL-2.1-or-later
URL:            http://libestr.adiscon.com/
Source0:        http://libestr.adiscon.com/files/download/libestr-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 46632b2785ff4a231dcf241eeb0dcb5fc0c7d4da8ee49cf5687722cdbe8b2024
%global source0_file libestr-0.1.11.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf automake libtool
%description
This package compiles the string handling essentials library
used by the Rsyslog daemon.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The package contains libraries and header files for
developing applications that use libestr.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libestr-0.1.11.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "46632b2785ff4a231dcf241eeb0dcb5fc0c7d4da8ee49cf5687722cdbe8b2024" || { echo "oreon: Source0 SHA256 mismatch for libestr-0.1.11.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static --with-pic
V=1 make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libestr.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libestr.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.11-13
- Import
