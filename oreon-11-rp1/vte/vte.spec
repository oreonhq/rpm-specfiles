%global source0_hash 86cf0b81aa023fa93ed415653d51c96767f20b2d7334c893caba71e42654b0ae

%define glib2_version 2.26.0
%define pango_version 1.22.0
%define gtk2_version 2.20.0

Name: vte
Version: 0.28.2
Release: 46%{?dist}
Summary: A terminal emulator
License: LGPL-2.0-or-later
#VCS: git:git://git.gnome.org/vte
URL: http://developer.gnome.org/vte/
Source: http://download.gnome.org/sources/vte/0.28/%{name}-%{version}.tar.xz
# https://bugzilla.gnome.org/show_bug.cgi?id=663779
Patch0: vte-alt-meta-confusion.patch
# Python bindings bugfix
# https://bugzilla.redhat.com/show_bug.cgi?id=556200
Patch1: vte-python-bugfixes.patch
# limit arguments to avoid DOS
# http://git.gnome.org/browse/vte/patch/?id=feeee4b5832b17641e505b7083e0d299fdae318e
Patch2: vte-0.28.2-limit-arguments.patch
#
# aarch64 support
Patch3: http://ausil.fedorapeople.org/aarch64/vte/vte-aarch64.patch
# Fix control home/control end codes
# https://bugzilla.redhat.com/show_bug.cgi?id=1114074
Patch4: vte-0.28.2-control.patch
# Fix mc paste
# https://bugzilla.redhat.com/show_bug.cgi?id=1114301
Patch5: vte-0.28.2-paste-fix.diff
# Backport introspection fixes
# https://bugzilla.redhat.com/show_bug.cgi?id=1256535
Patch6: vte-0.28.2-introspection-fixes.patch
# Backport "cat bigfile" speedup
# https://bugzilla.gnome.org/show_bug.cgi?id=721944
Patch7: vte-0.28.2-performance.patch
# Backport shift-mouse grab "hang" fix
# https://bugzilla.gnome.org/show_bug.cgi?id=683730
Patch8: vte-0.28.2-683730.patch
# Backport extended xterm/urxvt mouse tracking support
# https://bugzilla.gnome.org/show_bug.cgi?id=681329
Patch9: vte-0.28.2-mouse-tracking.patch
Patch10: pointer-types.patch

BuildRequires: make
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: ncurses-devel
BuildRequires: gettext
BuildRequires: libXt-devel
BuildRequires: intltool
# Work around broken perl / perl-Carp
BuildRequires: perl-Carp
BuildRequires: gobject-introspection-devel

# systemd creates the utmp group
Requires: systemd

%description
VTE is a terminal emulator widget for use with GTK+ 2.0.

%package devel
Summary: Files needed for developing applications which use vte
Requires: %{name} = %{version}-%{release}
Requires: gtk2-devel
Requires: ncurses-devel
Requires: pkgconfig

%description devel
The vte-devel package includes the header files and developer docs
for the vte package.

Install vte-devel if you want to develop programs which will use
vte.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p2
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p0

%build
%configure \
        --enable-shared \
        --enable-static \
        --enable-introspection \
        --with-gtk=2.0 \
        --libexecdir=%{_libdir}/%{name} \
        --without-glX \
        --disable-gtk-doc \
        --disable-python
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove the .a and .la file.
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.a
rm $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.la

# Remove static python modules and la files, which are probably useless to Python anyway.
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/*.a

%find_lang vte-0.0

%files -f vte-0.0.lang
%doc COPYING HACKING NEWS README
%doc src/iso2022.txt
%doc doc/utmpwtmp.txt doc/boxes.txt doc/openi18n/UTF-8.txt doc/openi18n/wrap.txt
%{_libdir}/*.so.*
%dir %{_libdir}/vte
%attr(2711,root,utmp) %{_libdir}/vte/gnome-pty-helper
%{_datadir}/%{name}
%{_libdir}/girepository-1.0

#rpmlint gives:
#vte.x86_64: W: private-shared-object-provides /usr/lib64/python2.7/site-packages/gtk-2.0/vtemodule.so vtemodule.so()(64bit)
# This is not used by anything except possibly third party scripts, so we're leaving it in place.

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_bindir}/%{name}
%{_datadir}/gir-1.0
%doc %{_datadir}/gtk-doc/html/vte-0.0

%changelog
%autochangelog
