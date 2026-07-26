%global source0_hash f271300c10423150562a290ed2a67910db804c7f11fbfd3e3f67016c039af8fa

Name: xsc
Version:  1.6
Release:  23%{?dist}
Summary: A clone of the old vector graphics video game Star Castle

License: GPL-2.0-or-later
URL: http://www.panix.com/~mbh/projects.html
Source0: http://www.panix.com/~mbh/xsc/xsc-%{version}.tar.gz
Source1: xsc.desktop
Source2: xsc.png
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: desktop-file-utils, libX11-devel
Requires: hicolor-icon-theme

%description
The object is to blast a hole in the rings and destroy the enemy ship.
The only problem is that it tracks your every move and as soon as you 
knock a hole in all three rings, and they all line up, it lets loose  
with the big nasty green fireballs.  Avoid them.  Avoid the little green
buzzers, too.  Shoot 'em if you want.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --x-includes="" --x-libraries=""
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 xsc %{buildroot}%{_bindir}/xsc

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install           \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%{_bindir}/xsc
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_datadir}/applications/xsc.desktop
%{_datadir}/icons/hicolor/32x32/apps/xsc.png

%changelog
%autochangelog
