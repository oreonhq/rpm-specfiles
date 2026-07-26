%global source0_hash 8a1fd3bf9f38e8c7bb2b2864c090f986b60cec2281ecf1bba462d120fb327d00

Name:           pekwm
Version:        0.1.17
Release:        32%{?dist}
Summary:        A small and flexible window manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.pekwm.org/
Source0:        http://www.pekwm.org/projects/pekwm/files/%{name}-%{version}.tar.bz2

Patch0:         %{name}-0.1.15-menu.patch
Patch1:		%{name}-0.1.15-gcc10.patch

BuildRequires: make
BuildRequires:  libX11-devel libpng-devel libXrandr-devel
BuildRequires:  libXft-devel libXext-devel libXinerama-devel
BuildRequires:  libXpm-devel libjpeg-devel libICE-devel libSM-devel
BuildRequires: 	gcc-c++

%description
Pekwm is a window manager that once up on a time was based on the aewm++ window
manager, but it has evolved enough that it no longer resembles aewm++ at all.
It has a much expanded feature-set, including window grouping (similar to ion,
pwm, or fluxbox), autoproperties, xinerama, keygrabber that supports keychains,
and much more.

* Lightweight and Unobtrusive, a window manager shouldn't be noticed.
* Very configurable, we all work and think in different ways.
* Automatic properties, for all the lazy people, make things appear as they
should when starting applications.
* Chainable Keygrabber, usability for everyone. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Exclude/replace menu apps that are not in Fedora or are not free software
%patch -P0 -p0 -b .orig
%patch -P1 -p1 -b .gcc10

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Create desktop file
mkdir -p %{buildroot}%{_datadir}/xsessions/
cat << EOF > %{buildroot}%{_datadir}/xsessions/%{name}.desktop
[Desktop Entry]
Name=PekWM
Comment=Very small and fast window manger
Exec=pekwm
TryExec=pekwm
Type=XSession
EOF

# Delete makefiles from contrib folder
find contrib/Makefile* -type f | xargs rm -rf || true
find contrib/lobo/Makefile* -type f | xargs rm -rf || true

# Rearrange the contents of contrib folder
mv contrib/lobo/* contrib/
rm -rf contrib/lobo

# Fix permissions to include scripts in %%doc
find contrib/pekwm_autoprop.pl -type f | xargs chmod 0644 || true
find contrib/pekwm_menu_config.pl -type f | xargs chmod 0644 || true

%files
%doc AUTHORS ChangeLog ChangeLog.aewm++ ChangeLog.until-0.1.6 LICENSE NEWS README contrib/
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/autoproperties
%config(noreplace) %{_sysconfdir}/%{name}/autoproperties_typerules
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/config_system
%config(noreplace) %{_sysconfdir}/%{name}/keys
%config(noreplace) %{_sysconfdir}/%{name}/menu
%config(noreplace) %{_sysconfdir}/%{name}/mouse
%config(noreplace) %{_sysconfdir}/%{name}/mouse_click
%config(noreplace) %{_sysconfdir}/%{name}/mouse_sloppy
%config(noreplace) %{_sysconfdir}/%{name}/mouse_system
%config(noreplace) %{_sysconfdir}/%{name}/vars
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/start
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.*
%{_datadir}/xsessions/%{name}.desktop

%changelog
%autochangelog
