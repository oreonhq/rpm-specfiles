%global source0_hash 85009b68167b3c3d96ed49a74d58df3b95f4f0678f3c73ee5f25bdf5c3d4d93a

Name: xgrav
Version:  1.2.0
Release:  39%{?dist}
Summary: A simple physics simulation for a large number of particles

License: GPL-2.0-or-later
URL: http://aass.oru.se/~mbl/xgrav/
Source0: http://www.aass.oru.se/~mbl/xgrav/xgrav-%{version}.tgz
Source1: xgrav.desktop
#Created from screenshot of example1.g run.
Source2: xgrav.png
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils, SDL-devel, flex, zlib-devel
Requires: hicolor-icon-theme

%description
X-Grav simulates the effect of gravity, collisions, heat dissipation and
a simple chemical reaction. The simulation is in no way meant to be 
realistic but rather a toy with which you can create stars, planets 
and even simple solar systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn xgrav

chmod -x COPYING

%build

make LINUX_CFLAGS="-c $RPM_OPT_FLAGS `pkg-config --cflags sdl` \
-DWITH_ROOTWINDOW" LINUX_LDFLAGS="$RPM_OPT_FLAGS `pkg-config \
--libs sdl` -lGL `pkg-config --libs x11` -lm"

%install
mkdir -p  %{buildroot}%{_bindir}
install -p -m 755 xgrav %{buildroot}%{_bindir}/xgrav

mkdir -p  %{buildroot}%{_datadir}/xgrav
install -p -m 644 example* %{buildroot}%{_datadir}/xgrav

sed 's;/usr/share;%_datadir;' %{SOURCE1} > xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc COPYING documentation.html README README.html TODO VERSION
%{_bindir}/xgrav
%{_datadir}/xgrav
%{_datadir}/applications/xgrav.desktop
%{_datadir}/icons/hicolor/32x32/apps/xgrav.png

%changelog
%autochangelog
