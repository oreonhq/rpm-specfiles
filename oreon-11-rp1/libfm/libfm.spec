%global source0_hash 601277a977053275f50ee696721e505501dd029fbd7f10b4262eb9c1f2b0373d

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=567257

# Upstream git:
# git://pcmanfm.git.sourceforge.net/gitroot/pcmanfm/libfm
# add bootstrap, need to build menu-cache in epel7
%global         use_release  0
%global         use_gitbare  1

%if 0%{?use_gitbare} < 1
# force
%global         use_release  1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20251217
%global		gittartime		2335
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20251214
%global		git_rev		7e575d13fcf0532fc181fc26391ad6fd7717ed66
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%else
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%endif

%endif

%global		main_version	1.4.1

%global         bootstrap   0
%global         build_doc   1

%undefine        _changelog_trimtime

Name:           libfm
Version:        %{main_version}%{git_ver_rpm}
Release:        2%{?dist}
Summary:        GIO-based library for file manager-like programs

# src/actions/	GPL-2.0-or-later
# src/base/	LGPL-2.1-or-later
# src/demo/	GPL-2.0-or-later
# src/extra/	LGPL-2.1-or-later
# src/fm-gtk.{c,h}	GPL-2.0-or-later
# src/gtk-compat.c	GPL-2.0-or-later
# src/*.c		(rest) LGPL-2.1-or-later
# src/gio/		GPL-2.0-or-later
# src/gtk/exo/	LGPL-2.1-or-later AND GPL-2.0-or-later
# src/gtk/		GPL-2.0-or-later AND LGPL-2.1-or-later
# src/job/		LGPL-2.1-or-later
# src/modules/	GPL-2.0-or-later
# src/tests/	GPL-2.0-or-later
# src/tools/	GPL-2.0-or-later
# src/udisks/	GPL-2.0-or-later

# SPDX confirmed
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://pcmanfm.sourceforge.net/
%if 0%{?use_release} >= 1
Source0:        http://downloads.sourceforge.net/pcmanfm/%{name}-%{mainver}%{?prever}.tar.xz
Source1:        https://raw.githubusercontent.com/lxde/libfm/master/autogen.sh
%endif
%if 0%{?use_gitbare} >= 1
Source0:        libfm-%{gittardate}T%{gittartime}.tar.gz
%endif
Source10:       create-libfm-git-bare-tarball.sh

# Make fm_config_load_from_key_file don't replace string key value
# when subsequent config file does not contain such key but previous key had
# (related to bug 2011471)
Patch1:         libfm-1.3.2-0001-fm_config_load_from_key_file-don-t-replace-string-va.patch
# http://sourceforge.net/p/pcmanfm/feature-requests/385/
#Patch1000:      http://sourceforge.net/p/pcmanfm/feature-requests/_discuss/thread/0a50a386/597e/attachment/libfm-1.2.3-moduledir-gtkspecific-v02.patch
Patch1000:      libfm-1.3.0.2-moduledir-gtkspecific-v03.patch

BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.26.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.27.0
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libexif)

%if ! 0%{?bootstrap}
BuildRequires:  pkgconfig(libmenu-cache) >= 0.3.2
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

BuildRequires:  gtk-doc
BuildRequires:  libxslt
BuildRequires:  %{_bindir}/valac

# Patch1000 needs the below anyway
BuildRequires:  automake
BuildRequires:  libtool

# Anyway use git
BuildRequires:  git

%if 0%{?build_doc} < 1
Obsoletes:      %{name}-devel-docs < 0.1.15
%endif

%description
LibFM is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnails support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package contains the generic non-gui functions of libfm.

%package        gtk
Summary:        File manager-related GTK+ widgets of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gvfs

%description    gtk
libfm is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnail support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package provides useful file manager-related GTK+ 3 widgets.

%package        gtk2
Summary:        File manager-related GTK+ widgets of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gvfs

%description    gtk2
libfm is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnail support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package provides useful file manager-related GTK+ 2 widgets.

%package        gtk-utils
Summary:        GTK+ related utility package for %{name}
Requires:       %{name}-gtk%{?isa} = %{version}-%{release}
Obsoletes:      lxshortcut < 0.1.3
Provides:       lxshortcut = %{version}-%{release}
Provides:       lxshortcut%{?_isa} = %{version}-%{release}

%description    gtk-utils
This package contains some GTK+ related utility files for
%{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        gtk-devel-common
Summary:        Common Development files for %{name}-gtk
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:		noarch

%description    gtk-devel-common
The %{name}-gtk-devel package contains common header files for
developing applications that use %{name}-gtk.

%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk-devel-common = %{version}-%{release}

%description    gtk-devel
The %{name}-gtk-devel package contains libraries files for
developing applications that use %{name}-gtk.

%package        gtk2-devel
Summary:        Development files for %{name}-gtk2
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk-devel-common = %{version}-%{release}

%description    gtk2-devel
The %{name}-gtk2-devel package contains libraries files for
developing applications that use %{name}-gtk2.

%package        devel-docs
Summary:        Development documation for %{name}

%description    devel-docs
This package containg development documentation files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release} >= 1
%setup -q -n %{name}-%{main_version}%{?prever}
cp -a %{SOURCE1} .
#%%patch0 -p1 -b .orig
git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

%if !%{use_gitcommit_as_rel}
git checkout -b fedora-%{version} %{version}
%endif

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "libfm Fedora maintainer"
git config user.email "libfm-maintainer@fedoraproject.org"

%if 0%{?use_release} >= 1
# Once call autogen.sh to make git status clean
sh autogen.sh
git add .
git commit -m "Init tree" -q
%endif

%if 0%{?use_gitbare} >= 1
git checkout -b %{main_version}-fedora %{git_rev}
cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done
%endif

cat %PATCH1  | git am
%patch -P1000 -p1 -Z
git commit -m "Use gtk version specific module directory" -a

# Need reporting upstream
# ref: https://github.com/lxde/libfm/commit/1af95bd8f26cab6848a74b7e02b53c6c79fb53a5
sed -i Makefile.am \
	-e '\@docs/reference/libfm/libfm-sections.txt@d'
git commit -m "Remove files entry to be regenerated" -a || true

# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
sh autogen.sh
git commit -m "save modified files" -a || true

# treak rpath
sed -i.libdir_syssearch \
  -e '/sys_lib_dlsearch_path_spec/s|/usr/lib |/usr/lib /usr/lib64 /lib /lib64 |' \
  configure
git commit -m "Tweak library search path spec not to inject rpath" -a || true

# Ignore po/ directory make check error
sed -i.error po/Makefile.in.in \
	-e '\@check@,\@fi@s|exit 1|exit 0|'
git commit -m "ignore po/ directory make check error" -a || true

# Tell vala to regenerate C source
find . -name \*.vala | xargs touch

%build
%if 0%{?use_gitbare} >= 1
cd libfm
%endif

%if 0%{?use_gitbare} >= 1
# Workaround
# Once generate files anyway
./configure
make dist
rm -f config.status
%endif

for ver in \
	2 \
	3 \
	%{nil}
do
	rm -rf _BUILDDIR_gtk${ver}
	mkdir _BUILDDIR_gtk${ver}
	pushd _BUILDDIR_gtk${ver}
	ln -sf ../configure

	%configure \
	    --srcdir=$(pwd)/.. \
%if 0%{?bootstrap}
	    --with-extra-only \
%endif
	    --enable-gtk-doc \
	    --enable-udisks \
	    --with-gtk=${ver} \
%if 0
	    --enable-demo \
%endif
	    --disable-silent-rules \
	    --disable-static

	# To show translation status
	make -C po -j1 GMSGFMT="msgfmt --statistics"
	make %{?_smp_mflags} -k

	make install DESTDIR=$(pwd)/../INSTDIR-gtk${ver} INSTALL="install -p"
	popd
done

%install
TOPDIR=$(pwd)

%if 0%{?use_gitbare} >= 1
cd libfm
%endif

# GTK3
cp -a INSTDIR-gtk3/* $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libfm-gtk.pc

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%if ! 0%{?bootstrap}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
( 
cd $TOPDIR
%find_lang %{name}
)
%endif

echo '%%defattr(-,root,root,-)' > $TOPDIR/base-header.files
echo '%%defattr(-,root,root,-)' > $TOPDIR/gtk-header.files

for f in $RPM_BUILD_ROOT%_includedir/%name-1.0/*.h
do
  bf=$(basename $f)
  for dir in actions base job extra .
  do
    if [ -f src/$dir/$bf ]
    then
	echo %_includedir/%name-1.0/$bf >> $TOPDIR/base-header.files
    fi
  done
  for dir in gtk
  do
    if [ -f src/$dir/$bf ]
    then
	echo %_includedir/%name-1.0/$bf >> $TOPDIR/gtk-header.files
    fi
  done
done

# GTK2
%if ! 0%{?bootstrap}
pushd INSTDIR-gtk2

find . -name '*.la' -exec rm -f {} ';'
rm -f .%{_libdir}/pkgconfig/libfm-gtk3.pc

diff -urNp .%{_includedir}/%{name}-1.0 $RPM_BUILD_ROOT%{_includedir}/%name-1.0
diff -urNp .%{_datadir}/%{name} $RPM_BUILD_ROOT/%{_datadir}/%{name}

cp -a ./%{_libdir}/libfm-gtk* $RPM_BUILD_ROOT%{_libdir}
cp -a ./%{_libdir}/pkgconfig/libfm-gtk.pc \
	$RPM_BUILD_ROOT%{_libdir}/pkgconfig/
cp -a ./%{_libdir}/libfm/modules/gtk/ \
	$RPM_BUILD_ROOT%{_libdir}/libfm/modules/
popd
%endif

/usr/lib/rpm/check-rpaths

%check
%if 0%{?use_gitbare} >= 1
cd libfm
%endif

for ver in \
	2 \
	3 \
	%{nil}
do
	pushd _BUILDDIR_gtk${ver}
	make check
	popd
done

%pre devel
# Directory -> symlink
if [ -d %{_includedir}/libfm ] ; then
  rm -rf %{_includedir}/libfm
fi

%if 0%{?bootstrap}
%files
%else
%files -f %{name}.lang
%endif
# FIXME: Add ChangeLog if not empty
%doc AUTHORS
%license COPYING
%doc NEWS
%doc README

%if ! 0%{?bootstrap}
%dir %{_sysconfdir}/xdg/libfm/
%config(noreplace) %{_sysconfdir}/xdg/libfm/libfm.conf

%{_datadir}/%{name}/
%{_libdir}/%{name}.so.4*

%dir %{_libdir}/libfm
%dir %{_libdir}/libfm/modules
%{_libdir}/libfm/modules/vfs-*.so
%{_datadir}/mime/packages/libfm.xml
%endif

%{_libdir}/%{name}-extra.so.4*

%if ! 0%{?bootstrap}
%files gtk
%{_libdir}/%{name}-gtk3.so.4*
%{_libdir}/libfm/modules/gtk3/

%files gtk-utils
%{_mandir}/man1/libfm-pref-apps.1.*
%{_mandir}/man1/lxshortcut.1.*

%{_bindir}/libfm-pref-apps
%{_bindir}/lxshortcut
%{_datadir}/applications/libfm-pref-apps.desktop
%{_datadir}/applications/lxshortcut.desktop
%endif

%files devel -f base-header.files
%doc TODO
%{_includedir}/libfm
%dir %{_includedir}/libfm-1.0/

%if ! 0%{?bootstrap}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libfm.pc
%endif
%{_libdir}/%{name}-extra.so
%{_libdir}/pkgconfig/libfm-extra.pc

%if ! 0%{?bootstrap}
%files gtk-devel-common -f gtk-header.files
%{_includedir}/libfm-1.0/fm-gtk.h

%files gtk-devel
%{_libdir}/%{name}-gtk3.so
%{_libdir}/pkgconfig/libfm-gtk3.pc

%files gtk2
%{_libdir}/%{name}-gtk.so.4*
%{_libdir}/libfm/modules/gtk/

%files gtk2-devel
%{_libdir}/%{name}-gtk.so
%{_libdir}/pkgconfig/libfm-gtk.pc

%if 0%{?build_doc}
%files devel-docs
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%endif
%endif

%changelog
%autochangelog
