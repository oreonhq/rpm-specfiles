Name:           low-memory-monitor
Version:        2.1
Release:        14%{?dist}
Summary:        Monitors low-memory conditions

License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/hadess/low-memory-monitor
Source0:        https://gitlab.freedesktop.org/hadess/low-memory-monitor/uploads/9c201566253ed52a9054f514f9904e48/low-memory-monitor-2.1.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  gtk-doc
BuildRequires:  systemd

%description
The Low Memory Monitor is an early boot daemon that will monitor memory
pressure information coming from the kernel, and, first, send a signal
to user-space applications when memory is running low, and then activate
the kernel's OOM killer when memory is running really low.

%package doc
Summary:        Documentation for %{name}
License:        GFDL-1.1-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc

This package contains the documentation for %{name}.

%prep
%autosetup


%build
%meson -Dgtk_doc=true -Dtrigger_kernel_oom=false
%meson_build


%install
%meson_install


%post
%systemd_post low-memory-monitor.service

%preun
%systemd_preun low-memory-monitor.service

%postun
%systemd_postun_with_restart low-memory-monitor.service

%triggerun -- low-memory-monitor < 2.0-6

# This is for upgrades from previous versions before low-memory-monitor became part
# of the system daemons.
systemctl --no-reload preset low-memory-monitor.service &>/dev/null || :

%files
%license COPYING
%doc NEWS README.md
%{_unitdir}/low-memory-monitor.service
%{_libexecdir}/low-memory-monitor
%{_datadir}/dbus-1/system.d/org.freedesktop.LowMemoryMonitor.conf

%files doc
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-14
- Prepare for Oreon 11 (RP1)
