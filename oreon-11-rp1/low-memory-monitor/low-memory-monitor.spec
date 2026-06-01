%global source0_hash ec45a8c83ad92f101e161bca63f9278e86429bca21e352c6b22da4f427fd4850

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n low-memory-monitor-2.1


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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-14
- Import
