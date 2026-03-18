Name:           usbredir
Version:        0.15.0
Release:        3%{?dist}
Summary:        USB network redirection protocol libraries
License:        LGPL-2.1-or-later
URL:            https://www.spice-space.org/usbredir.html
Source0:        http://spice-space.org/download/%{name}/%{name}-%{version}.tar.xz
Source1:        http://spice-space.org/download/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        victortoso-E37A484F.keyring
BuildRequires:  gnupg2
BuildRequires:  gcc g++
BuildRequires:  glib2-devel
BuildRequires:  libusb1-devel >= 1.0.9
BuildRequires:  git-core
BuildRequires:  meson

%description
The usbredir libraries allow USB devices to be used on remote and/or virtual
hosts over TCP.  The following libraries are provided:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the USB host side of a usbredir connection.
All that an application wishing to implement a USB host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        usbredir utility tools
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Includes usbredirect that uses libusbredirhost to export an USB device for use
in another (virtual) machine

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am


%build
%meson \
    -Dgit_werror=disabled \
    -Dtools=enabled \
    -Dfuzzing=disabled

%meson_build


%install
%meson_install


%ldconfig_scriptlets


%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB
%{_libdir}/libusbredir*.so.*

%files devel
%doc docs/usb-redirection-protocol.md docs/multi-thread.md ChangeLog.md TODO
%{_includedir}/usbredir*.h
%{_libdir}/libusbredir*.so
%{_libdir}/pkgconfig/libusbredir*.pc

%files tools
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/usbredirect
%{_mandir}/man1/usbredirect.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.0-3
- Prepare for Oreon 11 (RP1)
