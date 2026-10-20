%global debug_package %{nil}

Name: filesystem
Version: 11
Release: 1%{?dist}
Summary: Base directory layout
License: MIT
URL: https://oreonhq.com/

%description
The directories and compatibility symlinks every other package installs into.

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_infodir}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/var
mkdir -p %{buildroot}/var/tmp
mkdir -p %{buildroot}/var/log
mkdir -p %{buildroot}/var/cache
mkdir -p %{buildroot}/run
mkdir -p %{buildroot}/proc
mkdir -p %{buildroot}/sys
mkdir -p %{buildroot}/tmp
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/home
mkdir -p %{buildroot}/root
chmod 1777 %{buildroot}/tmp %{buildroot}/var/tmp
ln -s usr/bin %{buildroot}/bin
ln -s usr/bin %{buildroot}/sbin
ln -s usr/lib %{buildroot}/lib
ln -s usr/lib64 %{buildroot}/lib64

%files
%dir /usr
%dir %{_bindir}
%dir %{_sbindir}
%dir /usr/sbin
%dir /usr/lib
%dir %{_libdir}
%dir %{_libexecdir}
%dir %{_includedir}
%dir %{_datadir}
%dir %{_sysconfdir}
%dir %{_mandir}
%dir %{_infodir}
%dir /var
%dir /var/tmp
%dir /var/log
%dir /var/cache
%dir /run
%dir /proc
%dir /sys
%dir /tmp
%dir /boot
%dir /home
%dir /root
/bin
/sbin
/lib
/lib64
