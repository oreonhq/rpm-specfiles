%global source0_hash 4c787696faa5c21b228310ae8dceccf51359bb757595fb5282a4a089ec0df034
%define kdessconfigdir %{_datadir}/applnk/System/ScreenSavers
Name:           qstars
Version:        0.4
Release:        40%{?dist}
Summary:        A screensaver simulating planets and asteroids in space
License:        GPL-2.0-or-later AND HPND
URL:            http://qt.osdn.org.ua/qstars.html
Source0:        http://qt.osdn.org.ua/%{name}-%{version}.tar.gz
Source1:        %{name}.setup
Source2:        %{name}.conf
Patch0:         %{name}-0.4-desktop.patch
Patch1:         qstars-0.4-format-security.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt3-devel
# /oreon:deps
%description
A screensaver which simulates planets, asteroids and ships in a moving
starfield.

%package            xscreensaver
Summary:            XScreenSaver support for %{name}
Requires:           %{name} = %{version}-%{release}
Requires(post):     xscreensaver-base
Requires(postun):   xscreensaver-base
%description        xscreensaver
A screensaver which simulates planets, asteroids and ships in a moving
starfield. This package contains the files needed to use the hack with
xscreensaver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .orig
%patch -P1 -p1 -b .format

# Set installation in project file
sed -i 's|/local/|/|' %{name}.pro

%build

qmake
make clean
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d
install -p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d/
install -p -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -m0755 %{SOURCE1} %{buildroot}%{_bindir}/
cp -a ships galaxies planets asteroids %{buildroot}%{_datadir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post xscreensaver

if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi
%postun xscreensaver

if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi
%files -f %{oreon_filedir}/main.list
%files -n qstars-xscreensaver -f %{oreon_filedir}/qstars-xscreensaver.list

%changelog

%autochangelog
