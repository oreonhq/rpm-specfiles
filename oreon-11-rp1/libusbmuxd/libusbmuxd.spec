%global forgeurl https://github.com/libimobiledevice/libusbmuxd

Name:           libusbmuxd
Version:        2.1.0
Release:        %autorelease
Summary:        Client library USB multiplex daemon for Apple's iOS devices

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://www.libimobiledevice.org/
Source:        https://github.com/libimobiledevice/libusbmuxd/releases/download/2.1.0/libusbmuxd-2.1.0.tar.bz2
# oreon url source checksums begin
%global source0_sha256 c35bf68f8e248434957bd5b234c389b02206a06ecd9303a7fb931ed7a5636b16
%global source0_file libusbmuxd-2.1.0.tar.bz2
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel >= 2.2.0

%description
libusbmuxd is the client library used for communicating with Apple's iPod Touch,
iPhone, iPad and Apple TV devices. It allows multiple services on the device 
to be accessed simultaneously.

%package        utils
Summary:        Utilities for communicating with Apple's iOS devices
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
Utilities for Apple's iOS devices

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libusbmuxd-2.1.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c35bf68f8e248434957bd5b234c389b02206a06ecd9303a7fb931ed7a5636b16" || { echo "oreon: Source0 SHA256 mismatch for libusbmuxd-2.1.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README.md AUTHORS
%{_libdir}/libusbmuxd-2.0.so.7*

%files utils
%{_bindir}/iproxy
%{_bindir}/inetcat
%{_mandir}/man1/iproxy.1*
%{_mandir}/man1/inetcat.1*

%files devel
%{_includedir}/usbmuxd.h
%{_includedir}/usbmuxd-proto.h
%{_libdir}/%{name}-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-1
- Prepare for Oreon 11 (RP1)
