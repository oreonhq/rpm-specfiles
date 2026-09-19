%global source0_hash e94004fa9aa6a7250ac4db6180e96f9c147db617c0d8e7fc8c9e2c42924e990c

Name:           tango-icon-theme
Version:        0.8.90
Release:        33%{?dist}
Summary:        Icon theme from Tango Project
Summary(de):    Symbolthema vom Tango Projekt
Summary(es):    Iconos del Proyecto Tango
Summary(pl):    Ikony Projektu Tango

License:        CC0-1.0
URL:            http://tango.freedesktop.org/Tango_Desktop_Project

Source0:        http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
#VCS: git:git://anongit.freedesktop.org/tango/tango-icon-theme
Patch0:         tango-icon-theme-0.8.90-transparency.patch

# https://bugs.freedesktop.org/show_bug.cgi?id=45803
Patch1:         tango-icon-theme-0.8.90-rsvg-convert.patch
Patch2:         tango-icon-theme-0.8.90-rsvg-convert-configure.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  icon-naming-utils >= 0.8.90
BuildRequires:  ImageMagick-devel >= 5.5.7
BuildRequires:  intltool
BuildRequires:  librsvg2-devel >= 2.35.2
BuildRequires:  librsvg2-tools
BuildRequires:  make
BuildRequires:  pkgconfig >= 0.19

%description
Contains icons from Tango Project.

%description -l de
Enthält Symbole vom Tango Projekt.

%description -l es
Contiene iconos del Proyecto Tango.

%description -l pl
Zawiera ikony Projektu Tango.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .transparency
%patch -P1 -p1
%patch -P2 -p1

%build
%configure --enable-png-creation
make

chmod +x svg2png.sh

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL='install -p'

%post
touch --no-create %{_datadir}/icons/Tango &>/dev/null || :

%postun
touch --no-create %{_datadir}/icons/Tango &>/dev/null || :
gtk-update-icon-cache -q %{_datadir}/icons/Tango &>/dev/null || :

%posttrans
gtk-update-icon-cache -q %{_datadir}/icons/Tango &>/dev/null || :

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/icons/Tango

%changelog
%autochangelog
