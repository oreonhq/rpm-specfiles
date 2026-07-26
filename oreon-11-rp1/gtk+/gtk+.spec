%global source0_hash 222548df9bf905c930029fa25eb5586ac0a5f290610cfb7c68183a1db81e3b50

Summary:	The GIMP ToolKit
Name:		gtk+
Epoch:		1
Version:	1.2.10
Release:	112%{?dist}
License:	LGPL-2.0-or-later
URL:		http://www.gtk.org/
Source0:	https://ftp.gnome.org/pub/gnome/sources/gtk+/1.2/gtk+-%{version}.tar.gz

Provides:	gtk1 = %{version}-%{release}
Provides:	gtk1%{?_isa} = %{version}-%{release}

Source1:	gtkrc-default
Source2:	gtk+-pofiles.tar.gz
Source3:	gtkrc.ja.utf8
Source4:	gtkrc.ko.utf8
Source5:	gtkrc.zh_CN.utf8
Source6:	gtkrc.zh_TW.utf8

# We need newer versions of config.guess and config.sub to be able to
# handle exotic new architectures (at the time this software was released)
# such as x86_64
#
# http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD
Source7:	config.guess
# http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD
Source8:	config.sub

Patch1:		gtk+-1.2.10-ahiguti.patch
Patch5:		gtk+-1.2.8-wrap-alnum.patch
# Suppress alignment warnings on ia64
Patch10:	gtk+-1.2.10-alignment.patch
# Improve exposure compression
Patch11:	gtk+-1.2.10-expose.patch
# Handle focus tracking for embedded window properly
Patch12:	gtk+-1.2.10-focus.patch
# Find gtkrc files for the current encoding better
Patch13:	gtk+-1.2.10-encoding.patch
# Don't screw up CTEXT encoding for UTF-8
Patch14:	gtk+-1.2.10-ctext.patch
# Don't warn about missing fonts for UTF-8
Patch15:	gtk+-1.2.10-utf8fontset.patch
# Accept KP_Enter as a synonym for Return everywhere
Patch16:	gtk+-1.2.10-kpenter.patch
# Allow theme switching to work properly when no windows are realized
Patch17:	gtk+-1.2.10-themeswitch.patch
# Fix crash when switching themes
Patch18:	gtk+-1.2.10-pixmapref.patch
# Fix computation of width of missing characters
Patch19:	gtk+-1.2.10-missingchar.patch
# Fix sizes of Ukrainian fontsets
Patch20:	gtk+-1.2.10-ukfont.patch
# Fix file selection delete-dir when changing directory problem
# also, fix memory corruption problem when changing directories.
Patch21:	gtk+-1.2.10-deletedir.patch
# Improve warning for missing fonts
Patch22:	gtk+-1.2.10-fontwarning.patch
# Allow themes to make scrollbar trough always repaint
Patch23:	gtk+-1.2.10-troughpaint.patch
# Fix a crash that can happen in some apps when the current
# locale is not supported by XLib.
Patch24:	gtk+-1.2.10-localecrash.patch
# Patch from CVS to fix b.g.o #56349
Patch26:	gtk+-1.2.10-dndorder.patch
# Patch from CVS to fix b.g.o #94812
Patch27:	gtk+-1.2.10-clistfocusrow.patch
# Fix GTK+ to obey X server's default bell volume
Patch28:	gtk+-1.2.10-bellvolume.patch
# Hack up the configure scripts to deal with some obscure
# breakage with ancient libtool
Patch29:	gtk+-1.2.10-libtool.patch
# Add a dependency on libgdk to libgtk (#106677)
Patch30:	gtk+-1.2.10-gtkgdkdep.patch
Patch31:	gtk+-underquoted.patch
Patch32:	gtk+-1.2.10-ppc64.patch
# do not allow for undefined symbols in shared libraries -- Rex
Patch33:	gtk+-1.2.10-no_undefined.patch
# http://bugzilla.redhat.com/222298
Patch34:	gtk+-1.2.10-multilib.patch
# Remove redundant shared library dependencies
Patch35:	gtk+-1.2.10-unused-deps.patch
# Avoid having to run autotools at build time
Patch36:	gtk+-1.2.10-autotools.patch
# Use format strings properly
Patch37:	gtk+-1.2.10-format.patch
# C99 compiler support
Patch38:	gtk+-1.2.10-c99.patch
# Fix incompatible pointer type in call to XmbTextListToTextProperty
Patch39:	gtk+-1.2.10-ptrtype.patch
# C23 compiler support
Patch40:	gtk+-1.2.10-c23.patch

BuildRequires:	coreutils
BuildRequires:	gettext
BuildRequires:	glib-devel >= 1:%{version}
BuildRequires:	glibc-common
BuildRequires:	libtool
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXt-devel
BuildRequires:	make

%description
The gtk+ package contains the GIMP ToolKit (GTK+), a library for
creating graphical user interfaces for the X Window System. GTK+ was
originally written for the GIMP (GNU Image Manipulation Program) image
processing program, but is now used by several other programs as
well.

%package	devel
Summary:	Development tools for GTK+ (GIMP ToolKit) applications
Provides:	gtk1-devel = %{version}-%{release}
Provides:	gtk1-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	glib-devel%{?_isa}
Requires:	libX11-devel%{?_isa}
Requires:	libXext-devel%{?_isa}
Requires:	libXi-devel%{?_isa}
Requires:	libXt-devel%{?_isa}

%description devel
Libraries, header files and documentation for developing GTK+ 
(GIMP ToolKit) applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 2

%patch -P  1 -p1 -b .ahiguti
%patch -P  5 -p1 -b .alnum
%patch -P 10 -p1 -b .alignment
%patch -P 11 -p1 -b .expose
%patch -P 12 -p1 -b .focus
%patch -P 13 -p1 -b .encoding
%patch -P 14 -p1 -b .ctext
%patch -P 15 -p1 -b .utf8fontset
%patch -P 16 -p1 -b .kpenter
%patch -P 17 -p1 -b .themeswitch
%patch -P 18 -p1 -b .pixmapref
%patch -P 19 -p1 -b .missingchar
%patch -P 20 -p1 -b .ukfont
%patch -P 21 -p1 -b .deletedir
%patch -P 22 -p1 -b .fontwarning
%patch -P 23 -p0 -b .troughpaint
%patch -P 24 -p1 -b .localecrash
%patch -P 26 -p0 -b .dndorder
%patch -P 27 -p0 -b .clistfocusrow
%patch -P 28 -p1 -b .bellvolume
%patch -P 29 -p1 -b .libtool
%patch -P 30 -p1 -b .gtkgdkdep
%patch -P 31 -p1 -b .underquoted
%patch -P 32 -p1 -b .ppc64
%patch -P 33 -p1 -b .no_undefined
%patch -P 34 -p1 -b .multilib
%patch -P 35 -p1 -b .unused-deps
%patch -P 36 -p0 -b .autotools
%patch -P 37 -p0 -b .format
%patch -P 38 -p1 -b .c99
%patch -P 39 -p1 -b .ptrtype
%patch -P 40 -p0 -b .c23

# The original config.{guess,sub} do not work on x86_64, aarch64 etc.
#
cp -p %{SOURCE7} %{SOURCE8} .
chmod -c +x config.{guess,sub}

# Recode docs as UTF-8
for doc in ChangeLog examples/calendar/calendar.c; do
	iconv -f iso-8859-1 -t utf-8 < ${doc} > ${doc}.utf8
	mv ${doc}.utf8 ${doc}
done

%build
LIBTOOL=/usr/bin/libtool \
%configure \
	--disable-static \
	--with-xinput=xfree \
	--with-native-locale

%{make_build} LIBTOOL=/usr/bin/libtool

%install
%{make_install} LIBTOOL=/usr/bin/libtool

#
# Make cleaned-up versions of examples and tutorial for installation
#
./mkinstalldirs tmpdocs/tutorial
install -p -m0644 docs/html/gtk_tut.html docs/html/gtk_tut-[0-9]*.html docs/html/*.gif tmpdocs/tutorial
for dir in examples/*; do
	if [ -d $dir ]; then
		./mkinstalldirs tmpdocs/$dir
		for file in $dir/* ; do
			case $file in
			*pre1.2.7)
				;;
			*)
				install -p -m0644 $file tmpdocs/$dir
				;;
			esac
		done
	fi
done

install -p -m644 -D %{SOURCE1} %{buildroot}/etc/gtk/gtkrc

# Install some extra gtkrc files to improve functioning of GTK+
# in UTF-8 locales for Chinese, Japanese, Korean.
for i in %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}; do
	install -p -m0644 $i %{buildroot}/etc/gtk/
done

# We don't ship the info files
rm -rvf %{buildroot}%{_infodir}

# .la fies... die die die.
rm -rvf %{buildroot}%{_libdir}/lib*.la
# despite use of --disable-static, delete static libs that get built anyway
rm -rvf %{buildroot}%{_libdir}/lib*.a

%find_lang %{name}

%check
make check LIBTOOL=/usr/bin/libtool

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 27)
# ldconfig scriptlets replaced by RPM File Triggers from Fedora 28
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libgdk-1.2.so.*
%{_libdir}/libgtk-1.2.so.*
%{_datadir}/themes/Default/
%dir %{_sysconfdir}/gtk/
%config(noreplace) %{_sysconfdir}/gtk/gtkrc*

%files devel
%doc tmpdocs/tutorial/
%doc tmpdocs/examples/
%{_bindir}/gtk-config
%{_includedir}/gtk-1.2/
%{_libdir}/libgdk.so
%{_libdir}/libgtk.so
%{_libdir}/pkgconfig/gdk.pc
%{_libdir}/pkgconfig/gtk+.pc
%{_datadir}/aclocal/gtk.m4
%{_mandir}/man1/gtk-config.1*

%changelog
%autochangelog
