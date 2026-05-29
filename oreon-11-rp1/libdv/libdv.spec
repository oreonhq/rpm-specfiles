%global source0_hash a305734033a9c25541a59e8dd1c254409953269ea7c710c39e540bd8853389ba

Name:           libdv
Version:        1.0.0
Release:        46%{?dist}
Summary:        Software decoder for DV format video
License:        LGPL-2.0-or-later
URL:            http://libdv.sourceforge.net/
Source0:        http://downloads.sourceforge.net/libdv/libdv-1.0.0.tar.gz

Patch1:         %{name}-no-exec-stack.patch
Patch2:         %{name}-pic.patch
Patch3:         %{name}-gtk2.patch
Patch4:         %{name}-dso-linking.patch
Patch5:         %{name}-gcc14.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(glib-2.0) >= 2.1.0
BuildRequires:  pkgconfig(gtk+-x11-2.0) >= 2.1.0
BuildRequires:  libtool
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  SDL-devel

%description
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the IEEE
1394 (a.k.a. FireWire or i.Link) interface. libdv was developed according to the
official standards for DV video: IEC 61834 and SMPTE 314M.

%package tools
Summary:        Basic tools to manipulate Digital Video streams
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains some basic programs to display and encode digital video
streams. This programs uses the Quasar DV codec (libdv), a software codec for DV
video, the encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (a.k.a. FireWire or i.Link) interface.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 

%build
autoreconf -vif
%configure --with-pic --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%{?ldconfig_scriptlets}

%files
%doc ChangeLog
%license COPYING COPYRIGHT
%{_libdir}/%{name}.so.4
%{_libdir}/%{name}.so.4.0.3

%files tools
%doc README.* AUTHORS
%{_bindir}/dubdv
%{_bindir}/dvconnect
%{_bindir}/encodedv
%{_bindir}/playdv
%{_mandir}/man1/dubdv.1*
%{_mandir}/man1/dvconnect.1*
%{_mandir}/man1/encodedv.1*
%{_mandir}/man1/playdv.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-46
- Prepare for Oreon 11 (RP1)
