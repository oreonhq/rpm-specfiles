%global source0_hash 525597aca0a06486798be925b6f04146bb595643248690f45807b6fa3a0ded5d
Summary:        Screen lock and screen saver
Name: xlockmore
Version: 5.89
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://sillycycle.com/xlockmore.html
Source0:        http://sillycycle.com/xlock/xlockmore-%{version}.tar.xz
Patch0: xlockmore-ignore-void.patch
Requires: gnome-icon-theme-legacy
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  motif-devel
BuildRequires:  pam-devel
# /oreon:deps
%description
Locks the local X display until a password is entered.

%package motif
Summary: Motif based frontend for xlockmore
Requires: %{name} = %{version}-%{release}
%description motif
Motif based frontend for xlockmore.

%package gtk
Summary: GTK based frontend for xlockmore
Requires: %{name} = %{version}-%{release}
%description gtk
GTK based frontend for xlockmore.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p 1

%{__sed} -i -e "s,/lib,/%{_lib},g;s,-Wno-format,,g;" configure

# See README for X(M)LOCKLDFLAGS explanation
%{__sed} -i "/^XLOCKLDFLAGS$/d" configure
%{__sed} -i "/^XMLOCKLDFLAGS$/d" configure

%build

%configure --with-crypt --enable-pam --enable-syslog --disable-setuid --disable-mb
sed -i 's/^CC =.*/\0 -std=c17/' xglock/Makefile
sed -i 's/@XLOCKLDFLAGS@//' modes/Makefile
sed -i 's/@XMLOCKLDFLAGS@//' xmlock/Makefile
%{__make} %{?_smp_mflags}
%install
%{__install} -D -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -D -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -D -m0755 xglock/xglock %{buildroot}%{_bindir}/xglock
%{__install} -p -D -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -p -D -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -p -D -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock
%{__chmod} 644 README
%{__chmod} 644 docs/Revisions
%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/xlock << EOF
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
EOF
%{__mkdir_p} %{buildroot}%{_datadir}/applications
cat >> %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Xlock
Comment=Screen Saver
Encoding=UTF-8
Icon=gnome-lockscreen
Exec=xlock
Terminal=false
Type=Application
EOF
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category X-Fedora \
	--add-category Application \
	--add-category Graphics \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xlockmore-motif -f %{oreon_filedir}/xlockmore-motif.list
%files -n xlockmore-gtk -f %{oreon_filedir}/xlockmore-gtk.list

%changelog

%autochangelog
