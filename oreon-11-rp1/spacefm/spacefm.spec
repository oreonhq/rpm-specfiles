%global source0_hash fedea9fcad776e0af4b8d90c5a1c86684a9c96ef1cdd4e959530ce93bdebe7c9

Name:		spacefm
Version:	1.0.6
Release:	23%{?dist}
Summary:	Multi-panel tabbed file and desktop manager

# overall		GPL-3.0-or-later
# src/exo/		LGPL-3.0-or-later
# src/libmd5-rfc/md5.c	Zlib
# src/ptk/		LGPL-3.0-or-later
# SPDX confirmed
License:	GPL-3.0-or-later AND LGPL-3.0-or-later AND Zlib
URL:		http://ignorantguru.github.io/spacefm/
Source0:	https://github.com/IgnorantGuru/spacefm/archive/%{version}/%{name}-%{version}.tar.gz
# Force x11 as gdk backend (bug 1438277)
Patch0:	spacefm-1.0.5-force-x11-backend.patch
# Patch for major(), minor() with glibc 2.28
Patch1:	spacefm-1.0.6-major-glibc228.patch
# Patch to compile with gcc10 -fno-common
Patch2:	spacefm-1.0.6-gcc10-fno-common.patch
# Support C99, use pointer type correctly
Patch3:	spacefm-1.0.6-c99-type-cast.patch
# Avoid C23 bool keyword usage
Patch4:	spacefm-1.0.6-c23-bool-keyword.patch
# Support C23 strict function prototype
Patch5:	spacefm-1.0.6-c23-function-proto.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libudev) >= 143

%description
SpaceFM is a multi-panel tabbed file manager with built-in VFS, udev-based
device manager, customizable menu system, and bash integration.

%package	Faenza
Summary:	Faenza theme files for spacefm
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	Faenza
This package contains Faenza theme files for spacefm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .x11
%patch -P1 -p1 -b .glibc228
%patch -P2 -p1 -b .gcc10
%patch -P3 -p1 -b .c99
%patch -P4 -p1 -b .bool
%patch -P5 -p1 -b .c23
find . -name \*.c -print0 | xargs --null chmod 0644

%build
%configure \
	--with-gtk3 \
	--disable-video-thumbnails \
	%{nil}
%make_build

%install
%make_install

# Create skeleton configuration file and directory (ref: src/settings.c)
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

# Distro does not require this
rm -f %{buildroot}%{_bindir}/spacefm-installer

# save this
rm -rf tmpdocdir
mv %{buildroot}%{_docdir}/%{name} tmpdocdir

%find_lang %{name}

%check
for f in %{buildroot}%{_datadir}/applications/*desktop
do
	desktop-file-validate $f
done

%post	Faenza
touch --no-create %{_datadir}/icons/Faenza &>/dev/null || :

%postun	Faenza
if [ $1 -eq 0 ] ; then
	touch --no-create %{_datadir}/icons/Faenza &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/Faenza &>/dev/null || :
fi

%posttrans	Faenza
gtk-update-icon-cache %{_datadir}/icons/Faenza &>/dev/null || :

%files	-f %{name}.lang
%doc	AUTHORS
%license	COPYING*
%doc	ChangeLog
%doc	README

%dir	%{_sysconfdir}/%{name}
%config(noreplace)	%{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-auth
%{_datadir}/applications/%{name}*desktop
# ref: src/settings.c
%doc	tmpdocdir/%{name}-manual-en.html
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/mime/packages/%{name}-mime.xml
%dir	%{_datadir}/%{name}
%{_datadir}/%{name}/ui/

%files	Faenza
%{_datadir}/icons/Faenza/apps/*/%{name}*

%changelog
%autochangelog
