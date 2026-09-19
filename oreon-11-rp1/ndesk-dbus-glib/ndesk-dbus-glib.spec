%global source0_hash 0a6d5fe7be55b6301615d71b89507b712f287b4ba498b798301333ffabe06769

%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac
%endif

%define			debug_package %{nil}

Name:			ndesk-dbus-glib
URL:			http://www.ndesk.org/DBusSharp
License:		MIT
Version:		0.4.1
Release:		44%{?dist}
Summary:		Provides glib mainloop integration for ndesk-dbus
Source0:		http://www.ndesk.org/archive/dbus-sharp/ndesk-dbus-glib-%{version}.tar.gz

BuildRequires: make
BuildRequires:	mono-devel
## This EVR is necessary due to the WaitForIOCompletion API added in the Sugar
## datastore patch.
BuildRequires:	ndesk-dbus-devel >= 0.6.1a-7

# Mono only available on these:
ExclusiveArch:	%{mono_arches}

%description
ndesk-dbus-glib provides glib mainloop integration for ndesk-dbus

%package devel
Summary:		Development files for ndesk-dbus-glib
Requires:		ndesk-dbus-glib = %{version}
Requires:		ndesk-dbus-devel
Requires:		pkgconfig

%description devel
Development files for ndesk-dbus-glib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_monogacdir}/NDesk.DBus.GLib/
%{_monodir}/ndesk-dbus-glib-1.0/

%files devel
%{_libdir}/pkgconfig/ndesk-dbus-glib-1.0.pc

%changelog
%autochangelog
