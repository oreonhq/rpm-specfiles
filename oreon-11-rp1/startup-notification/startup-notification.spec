# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3c391f7e930c583095045cd2d10eb73a64f085c7fde9d260f2652c7cb3cfbe4a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:    startup-notification
Version: 0.12
Release: 33%{?dist}
Summary: Library for tracking application startup

License: LGPL-2.0-or-later AND MIT
URL:     https://www.freedesktop.org/wiki/Software/startup-notification/
Source0: http://www.freedesktop.org/software/startup-notification/releases/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: make
BuildRequires: pkgconfig(xcb-event)

%description
This package contains libstartup-notification which implements a
startup notification protocol. Using this protocol a desktop
environment can track the launch of an application and provide
feedback such as a busy cursor, among other features.

%package devel
Summary: Development portions of startup-notification
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel

%description devel
Header files and static libraries for libstartup-notification.

%prep
%oreon_verify_sources
%autosetup
mkdir examples
cp -p test/*.c test/*.h examples

%build
%configure --disable-static
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%doc doc/startup-notification.txt
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_libdir}/libstartup-notification-1.so.0{,.*}

%files devel
%doc examples 
%{_libdir}/libstartup-notification-1.so
%{_libdir}/pkgconfig/libstartup-notification-1.0.pc
%{_includedir}/startup-notification-1.0/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12-33
- Prepare for Oreon 11 (RP1)
