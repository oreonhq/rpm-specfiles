%global source0_hash 6b8214fb1fa08fa89012d8c85d671a61be37ad33373065daf7ae17bd703bd0ad

%global upstream_name callaudiod

Summary:        Library for audio routing during voice calls
Name:           libcallaudio
Version:        0.1.99
Release:        1%{?dist}
License:        LGPL-3.0-or-later
URL:            https://gitlab.com/mobian1/callaudiod
Source0:        https://gitlab.com/mobian1/callaudiod/-/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)

%description
libcallaudio is a small library used by callaudiod, a daemon for dealing
with audio routing during phone calls, to switch audio profiles, route
output to the speaker or headset, and mute the microphone from a D-Bus
interface. This package ships only the client library used by consumers
such as plasma-dialer; the callaudiod daemon itself is not packaged here.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkgconfig file for building against libcallaudio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{upstream_name}-%{version}

%build
%meson -Dgtk_doc=false
%meson_build

%install
%meson_install
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libexecdir}/callaudiod
rm -rf %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_datadir}/dbus-1/system-services
rm -rf %{buildroot}%{_sysconfdir}/dbus-1/system.d
rm -rf %{buildroot}%{_datadir}/dbus-1/system.d

%files
%license COPYING
%doc README.md
%{_libdir}/libcallaudio-0.1.so.0*

%files devel
%dir %{_includedir}/libcallaudio-0.1/
%{_includedir}/libcallaudio-0.1/*.h
%{_libdir}/libcallaudio-0.1.so
%{_libdir}/pkgconfig/libcallaudio-0.1.pc

%changelog
%autochangelog
