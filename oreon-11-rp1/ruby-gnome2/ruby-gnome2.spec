%global source0_hash 73248f23f656df09a322a68c3139eb54eb6f7a4158c42cc30ee9e67fc2d4018e

%define         xulrunner_still_beta   1
#%%define         betaver                svn3690_trunk

#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
# Currently this spec file does not support libgda module.
# libgda-2 is needed, API change for libgda-3 needs investigation
# - Mamoru Tasaka

%define ruby_base_req ruby(release)

%undefine __brp_mangle_shebangs

Name:           ruby-gnome2
Version:        0.90.4
#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
Release:        27%{?dist}
Summary:        Ruby binding of libgnome/libgnomeui-2.x

# SPDX confirmed
License:        LGPL-2.1-only AND LGPL-2.1-or-later
URL:            http://ruby-gnome2.sourceforge.jp/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-all-%{version}.tar.gz
#Source0:        %{name}-all-%{version}-%{betaver}.tar.gz
Patch1:         ruby-gnome2-0.90.4-newpng.patch
# Fix for build error with gcc8 -O2 + ruby 2.5, rb_funcall argument number fix
Patch4:         ruby-libart-arglength-fix.patch
Patch6:         ruby-gnome2-rb_secure.patch
Patch14:        ruby-gnome2-implicit-int-7.patch
Patch15:        ruby-gnome2-c99.patch

BuildRequires:  make
BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libgnomeui-devel
# pkg-config.rb moved to rubygem-pkg-config, and now this is needed for BR
BuildRequires:  rubygem(pkg-config)
# The following line must actually be fixed in rubygem-pkg-config side.
# Will surely fix.
BuildRequires:  gcc
BuildRequires:  rubygems
BuildRequires:  %ruby_base_req

# Add system wide library (not ruby-gnome2 internal) to BR
BuildRequires:  rubygem-glib2-devel

Requires:       %ruby_base_req
Requires:       ruby(gnomecanvas2) = %{version}-%{release}

Provides:       ruby(gnome2) =  %{version}-%{release}

%description
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.

%package devel
Summary:        Development libraries and header files for ruby-gnome2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnome2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnome2-devel) = %{version}-%{release}

%description devel
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.
This package provides libraries and header files for ruby-gnome2

%package -n ruby-bonobo2
Summary:        Ruby binding of libbonobo-2.x
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel

Requires:       %ruby_base_req ruby(gtk2) >= %{version}

Provides:       ruby(bonobo2) = %{version}-%{release}

%description -n ruby-bonobo2
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.

%package -n ruby-bonobo2-devel
Summary:        Development libraries and header files for ruby-bonobo2
License:        LGPL-2.1-only

Requires:       ruby(bonobo2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonobo2-devel) = %{version}-%{release}

%description -n ruby-bonobo2-devel
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.
This package provides libraries and header files for ruby-bonobo2

%package -n ruby-bonoboui2
Summary:        Ruby binding of libbonoboui-2.x
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel libgnomeui-devel
BuildRequires:  rubygem-gtk2-devel

Requires:       %ruby_base_req ruby(gnome2) = %{version}-%{release}

Provides:       ruby(bonoboui2) = %{version}-%{release}

%description -n ruby-bonoboui2
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.

%package -n ruby-bonoboui2-devel
Summary:        Development libraries and header files for ruby-bonoboui2
License:        LGPL-2.1-only

Requires:       ruby(bonoboui2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonoboui2-devel) = %{version}-%{release}

%description -n ruby-bonoboui2-devel
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.
This package provides libraries and header files for ruby-bonoboui2

%package -n ruby-gconf2
Summary:        Ruby binding of GConf-2.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel GConf2-devel

Requires:       %ruby_base_req ruby(glib2) >= %{version}

Provides:       ruby(gconf2) =  %{version}-%{release}

%description -n ruby-gconf2
Ruby/GConf2 is a Ruby binding of GConf-2.x.

%package -n ruby-gconf2-devel
Summary:        Development libraries and header files for ruby-gconf2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gconf2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gconf2-devel) = %{version}-%{release}

%description -n ruby-gconf2-devel
Ruby/GConf2 is a Ruby binding of GConf-2.x.
This package provides libraries and header files for ruby-gconf2

%package -n ruby-gnomecanvas2
Summary:        Ruby binding of GnomeCanvas-2.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gtk2-devel libgnomecanvas-devel

Requires:       %ruby_base_req
Requires:       ruby(gtk2) >= %{version} 
Requires:       ruby(libart2) = %{version}-%{release}

Provides:       ruby(gnomecanvas2) =  %{version}-%{release}

%description -n ruby-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby-gnomecanvas2-devel
Summary:        Development libraries and header files for ruby-gnomecanvas2
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnomecanvas2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomecanvas2-devel) = %{version}-%{release}

%description -n ruby-gnomecanvas2-devel
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.
This package provides libraries and header files for ruby-gnomecanvas2

%package -n ruby-gnomevfs
Summary:        Ruby binding of GnomeVFS-2.0.x
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gnome-vfs2-devel

Requires:       %ruby_base_req
Requires:       ruby(glib2) >= %{version}

Provides:       ruby(gnomevfs) =  %{version}-%{release}

%description -n ruby-gnomevfs
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby-gnomevfs-devel
Summary:        Development libraries and header files for ruby-gnomevfs
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gnomevfs) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomevfs-devel) = %{version}-%{release}

%description -n ruby-gnomevfs-devel
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.
This package provides libraries and header files for ruby-gnomevfs

%package -n ruby-gtkglext
Summary:        Ruby binding of GtkGLExt
License:        LGPL-2.1-only AND LGPL-2.1-or-later

BuildRequires:  ruby ruby-devel gtk2-devel gtkglext-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gtk2-devel) = %{version}

Requires:       %ruby_base_req
Requires:       rubygem(ruby-opengl)
Requires:       ruby(gtk2) >= %{version}

Provides:       ruby(gtkglext) = %{version}-%{release}

%description -n ruby-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby-gtkglext-devel
Summary:        Development libraries and header files for ruby-gtkglext
License:        LGPL-2.1-only AND LGPL-2.1-or-later

Requires:       ruby(gtkglext) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtkglext-devel) = %{version}-%{release}

%description -n ruby-gtkglext-devel
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.
This package provides libraries and header files for ruby-gtkglext

%package -n ruby-libart2
Summary:        Ruby binding of Libart_lgpl
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel libart_lgpl-devel libpng-devel libjpeg-devel
#BuildRequires:  ruby(glib2-devel) = %{version}

Requires:       %ruby_base_req

Provides:       ruby(libart2) = %{version}-%{release}

%description -n ruby-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 

%package -n ruby-libart2-devel
Summary:        Development libraries and header files for ruby-libart2
License:        LGPL-2.1-only

Requires:       ruby(libart2) = %{version}-%{release}
Requires:       libart_lgpl-devel ruby-devel
Requires:       pkgconfig

Provides:       ruby(libart2-devel) = %{version}-%{release}

%description -n ruby-libart2-devel
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 
This package provides libraries and header files for ruby-libart2

%package -n ruby-libglade2
Summary:        Ruby bindings of Libglade2
License:        LGPL-2.1-only

BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libglade2-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gnome2) = %{version}

Requires:       %ruby_base_req
Requires:       ruby(gtk2) >= %{version}
Requires:       ruby(gnome2) = %{version}-%{release}

Provides:       ruby(libglade2) = %{version}-%{release}

%description -n ruby-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby-libglade2-devel
Summary:        Development libraries and header files for ruby-libglade2
License:        LGPL-2.1-only

Requires:       ruby(libglade2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(libglade2-devel) = %{version}-%{release}

%description -n ruby-libglade2-devel
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This package provides libraries and header files for ruby-libglade2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-all-%{version}
#%%setup -q -n %{name}-all-%{version}-%{betaver}

# Remove diretories no longer going to build
rm -rf \
	atk \
	gdk_pixbuf2 \
	gio2 \
	glib2 \
	gtk2 \
	gtkhtml2 \
	panel-applet \
	pango \
	poppler \
	rsvg2 \
	vte \
	goocanvas \
	gstreamer \
	gnomeprint \
	gnomeprintui \
	gtkmozembed \
	gtksourceview \
	gtksourceview2 \
	%{nil}
sed -i extconf.rb \
	-e 's|^priorlibs.*$|priorlibs\t= []|'

%patch -P1 -p1 -b .newpng
%patch -P4 -p1 -b .rb25
%patch -P6 -p1
%patch -P14 -p1
%patch -P15 -p1

# Fix /usr/local
grep -rl /usr/local/bin . | grep -v ChangeLog | \
	xargs -r sed -i -e 's|/usr/local/bin|/usr/bin|g'

# Keep timestamps as much as possible
find . -type f -name depend | xargs sed -i -e 's|-m 0644 -v|-m 0644 -p -v|'

# Fix the attributes of some files
# suppress lots of messages..
set +x
find . -name \*.rb -or -name \*.c | while read f ; do
        chmod 0644 $f
done
set -x

sed -i.config \
	-e 's|\([( \+]\)Config:|\1RbConfig:|g' \
	extconf.rb run-test.rb

# ruby 3 build fix
sed -i.ruby3 \
	gtkglext/src/rbgtkglext.c \
	-e 's|EXTERN|RUBY_EXTERN|'

# ruby 3.2 build fix
grep -rl rb_cData . | xargs sed -i.ruby32 -e 's|rb_cData|rb_cObject|'

# cleanup
# find . -type d -path '*/sample/*.svn' | sort -r | xargs rm -rf

# Kill tainted feature, fix -Werror=implicit-funciton-declaration
sed -i gnomevfs/src/gnomevfs-file.c \
	-e 's|rb_tainted_str_new|rb_str_new|'

%build
export CFLAGS="$RPM_OPT_FLAGS -Werror=implicit-function-declaration"
ruby extconf.rb --vendor

make %{?_smp_mflags} -k

%install
mkdir -p $RPM_BUILD_ROOT%{ruby_vendorarchdir}
mkdir -p $RPM_BUILD_ROOT%{ruby_vendorlibdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

export pkgconfigdir=$RPM_BUILD_ROOT%{_libdir}/pkgconfig
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" \
    ruby=ruby \
    %{nil}

# Handle manually
# ????
install -cpm 0755 */src/*.so \
    $RPM_BUILD_ROOT%{ruby_vendorarchdir}
install -cpm 0755 libglade/bin/ruby-glade-create-template \
    $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT/bin

%files
%doc gnome/README gnome/ChangeLog gnome/COPYING.LIB gnome/sample
%doc AUTHORS NEWS
%{ruby_vendorlibdir}/gnome2.rb
%{ruby_vendorarchdir}/gnome2.so

%files devel
%{_libdir}/pkgconfig/ruby-gnome2.pc

%files -n ruby-bonobo2
%doc bonobo/ChangeLog bonobo/COPYING.LIB bonobo/README
%{ruby_vendorlibdir}/bonobo2.rb
%{ruby_vendorarchdir}/bonobo2.so

%files -n ruby-bonobo2-devel
%{_libdir}/pkgconfig/ruby-bonobo2.pc

%files -n ruby-bonoboui2
%doc bonoboui/ChangeLog bonoboui/COPYING.LIB bonoboui/README
%{ruby_vendorlibdir}/bonoboui2.rb
%{ruby_vendorarchdir}/bonoboui2.so

%files -n ruby-bonoboui2-devel
%{_libdir}/pkgconfig/ruby-bonoboui2.pc

%files -n ruby-gconf2
%doc gconf/ChangeLog gconf/COPYING.LIB gconf/README gconf/sample
%{ruby_vendorlibdir}/gconf2.rb
%{ruby_vendorarchdir}/gconf2.so

%files -n ruby-gconf2-devel
%{_libdir}/pkgconfig/ruby-gconf2.pc

%files -n ruby-gnomecanvas2
%doc gnomecanvas/ChangeLog gnomecanvas/COPYING.LIB gnomecanvas/README gnomecanvas/sample
%{ruby_vendorlibdir}/gnomecanvas2.rb
%{ruby_vendorarchdir}/gnomecanvas2.so

%files -n ruby-gnomecanvas2-devel
%{_libdir}/pkgconfig/ruby-gnomecanvas2.pc

%files -n ruby-gnomevfs
%doc gnomevfs/ChangeLog gnomevfs/COPYING.LIB gnomevfs/README
%{ruby_vendorlibdir}/gnomevfs.rb
%{ruby_vendorarchdir}/gnomevfs.so

%files -n ruby-gnomevfs-devel
%{_libdir}/pkgconfig/ruby-gnomevfs.pc

%files -n ruby-gtkglext
%doc gtkglext/ChangeLog COPYING.LIB gtkglext/README gtkglext/README.rbogl gtkglext/sample
%{ruby_vendorlibdir}/gtkglext.rb
%{ruby_vendorarchdir}/gtkglext.so

%files -n ruby-gtkglext-devel
%{_libdir}/pkgconfig/ruby-gtkglext.pc

%files -n ruby-libart2
%doc libart/ChangeLog libart/COPYING.LIB libart/README libart/sample
%{ruby_vendorlibdir}/libart2.rb
%{ruby_vendorarchdir}/libart2.so

%files -n ruby-libart2-devel
%{ruby_vendorarchdir}/rbart.h
%{_libdir}/pkgconfig/ruby-libart2.pc

%files -n ruby-libglade2
%doc libglade/ChangeLog libglade/COPYING.LIB libglade/README libglade/sample
%{_bindir}/ruby-glade-create-template
#%%{ruby_vendorlibdir}/libglade2.rb
%attr(755, root, root) %{ruby_vendorlibdir}/libglade2.rb
%{ruby_vendorarchdir}/libglade2.so

%files -n ruby-libglade2-devel
%{_libdir}/pkgconfig/ruby-libglade2.pc

%changelog
%autochangelog
