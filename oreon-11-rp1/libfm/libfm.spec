%global source1_hash 358f60c1f471bec9c5275395466e3f9fc16d7e655c85b42cdca31cb05f9b0d3c
%global source0_hash 1b4c9cd5cd4cbcce8ad15f364e62dfc2de1d3f663dfd9931a35ebd190fbbdbbc
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global         use_release  0
%global         use_gitbare  1
%if 0%{?use_gitbare} < 1
%global         use_release  1
%endif
%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%if 0%{?use_gitbare}
%global		gittardate		20251015
%global		gittartime		1400
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
%{!?bootstrap:%global bootstrap 0}
%global         build_doc   1
%undefine        _changelog_trimtime
Name:           libfm
Version:        %{main_version}%{git_ver_rpm}
Release:        1%{?dist}
Summary:        GIO-based library for file manager-like programs
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://pcmanfm.sourceforge.net/
%if 0%{?use_release} >= 1
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
Source1:        https://raw.githubusercontent.com/lxde/libfm/master/autogen.sh
%endif
%if 0%{?use_gitbare} >= 1
%endif
Source10:       create-libfm-git-bare-tarball.sh
Patch1:         libfm-1.3.2-0001-fm_config_load_from_key_file-don-t-replace-string-va.patch
Patch1000:      libfm-1.3.0.2-moduledir-gtkspecific-v03.patch
%if ! 0%{?bootstrap}
%endif
%if 0%{?build_doc} < 1
Obsoletes:      %{name}-devel-docs < 0.1.15
%endif
# oreon:deps
BuildRequires:  //bin/valac
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(pango)
# /oreon:deps
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
./configure %{?bootstrap:--with-extra-only}
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
	    --disable-silent-rules \
	    --disable-static
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
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

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

if [ -d %{_includedir}/libfm ] ; then
  rm -rf %{_includedir}/libfm
fi
%if 0%{?bootstrap}
%files -f %{oreon_filedir}/main.list
%files -n libfm-gtk -f %{oreon_filedir}/libfm-gtk.list
%files -n libfm-gtk2 -f %{oreon_filedir}/libfm-gtk2.list
%files -n libfm-gtk-utils -f %{oreon_filedir}/libfm-gtk-utils.list
%files -n libfm-devel -f %{oreon_filedir}/libfm-devel.list
%files -n libfm-gtk-devel-common -f %{oreon_filedir}/libfm-gtk-devel-common.list
%files -n libfm-gtk-devel -f %{oreon_filedir}/libfm-gtk-devel.list
%files -n libfm-gtk2-devel -f %{oreon_filedir}/libfm-gtk2-devel.list
%files -n libfm-devel-docs -f %{oreon_filedir}/libfm-devel-docs.list

%changelog

%autochangelog
%endif
