%global source0_hash 3fb843ea671c89b909fd145fa09fd2276af3312e58cbab29ed1c93b462108c34
Summary:        The GIMP ToolKit
Name:		gtk+
Epoch:		1
Version:	1.2.10
Release:        1%{?dist}
License:	LGPL-2.0-or-later
URL:		http://www.gtk.org/
Source0:        https://ftp.gnome.org/pub/gnome/sources/gtk+/1.2/gtk+-%{version}.tar.gz
Provides:	gtk1 = %{version}-%{release}
Provides:	gtk1%{?_isa} = %{version}-%{release}
Source1:	gtkrc-default
Source2:	gtk+-pofiles.tar.gz
Source3:	gtkrc.ja.utf8
Source4:	gtkrc.ko.utf8
Source5:	gtkrc.zh_CN.utf8
Source6:	gtkrc.zh_TW.utf8
Source7:	config.guess
Source8:	config.sub
Patch1:		gtk+-1.2.10-ahiguti.patch
Patch5:		gtk+-1.2.8-wrap-alnum.patch
Patch10:	gtk+-1.2.10-alignment.patch
Patch11:	gtk+-1.2.10-expose.patch
Patch12:	gtk+-1.2.10-focus.patch
Patch13:	gtk+-1.2.10-encoding.patch
Patch14:	gtk+-1.2.10-ctext.patch
Patch15:	gtk+-1.2.10-utf8fontset.patch
Patch16:	gtk+-1.2.10-kpenter.patch
Patch17:	gtk+-1.2.10-themeswitch.patch
Patch18:	gtk+-1.2.10-pixmapref.patch
Patch19:	gtk+-1.2.10-missingchar.patch
Patch20:	gtk+-1.2.10-ukfont.patch
Patch21:	gtk+-1.2.10-deletedir.patch
Patch22:	gtk+-1.2.10-fontwarning.patch
Patch23:	gtk+-1.2.10-troughpaint.patch
Patch24:	gtk+-1.2.10-localecrash.patch
Patch26:	gtk+-1.2.10-dndorder.patch
Patch27:	gtk+-1.2.10-clistfocusrow.patch
Patch28:	gtk+-1.2.10-bellvolume.patch
Patch29:	gtk+-1.2.10-libtool.patch
Patch30:	gtk+-1.2.10-gtkgdkdep.patch
Patch31:	gtk+-underquoted.patch
Patch32:	gtk+-1.2.10-ppc64.patch
Patch33:	gtk+-1.2.10-no_undefined.patch
Patch34:	gtk+-1.2.10-multilib.patch
Patch35:	gtk+-1.2.10-unused-deps.patch
Patch36:	gtk+-1.2.10-autotools.patch
Patch37:	gtk+-1.2.10-format.patch
Patch38:	gtk+-1.2.10-c99.patch
Patch39:	gtk+-1.2.10-ptrtype.patch
Patch40:	gtk+-1.2.10-c23.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gettext
BuildRequires:  glib-devel
BuildRequires:  glibc-common
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
for i in %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}; do
	install -p -m0644 $i %{buildroot}/etc/gtk/
done
rm -rvf %{buildroot}%{_infodir}
rm -rvf %{buildroot}%{_libdir}/lib*.la
rm -rvf %{buildroot}%{_libdir}/lib*.a
%find_lang %{name}
%oreon_autofiles main

%check

make check LIBTOOL=/usr/bin/libtool
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
