%global source0_hash c63b2cd392523539b11d18e646d4f9df3ca2505240d16c8391fc424c8569b407

# Disable automatic .la file removal
%global __brp_remove_la_files %nil
%global configure ./configure~

Name:    kdewebdev
Summary: Web development applications 
Epoch:   6
Version: 3.5.10
Release: 61%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url:     http://kdewebdev.org/ 

Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Source1: http://download.sourceforge.net/quanta/css.tar.bz2
Source2: http://download.sourceforge.net/quanta/html.tar.bz2
Source3: http://download.sourceforge.net/quanta/php_manual_en_20030401.tar.bz2
Source4: http://download.sourceforge.net/quanta/javascript.tar.bz2
Source5: hi48-app-kxsldbg.png

Patch0: javascript.patch
Patch1: kdewebdev-3.5.4-kxsldbg-icons.patch
# fixes crash in kimagemapeditor when using freehand tool
Patch3: kdewebdev-3.5.10-fix-freehand-crash.patch
# fixes using a temporary as a lvalue in KafkaPart (FTBFS with g++ 4.6, probably
# silently did the wrong thing before)
Patch4: kdewebdev-3.5.10-gcc46.patch
# docbParseFile is dropped in libxml2-2.9 amd later
Patch6: kdewebdev-3.5.10-docbParseFile.patch

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# autoconf 2.7x
Patch304: kde3-autoconf-version.patch
# automake-1.16.5
Patch305: kdewebdev-3.5.10-automake-1.16.5.patch
Patch306: kdewebdev-3.5.10-libxml-ftbfs.patch
Patch307: kdewebdev-configure-c99.patch
# ftbfs, include cstdlib
Patch308: kdewebdev-3.5.10-include-cstdlib.patch
Patch309: kdewebdev-3.5.10-ftbfs.patch
Patch310: kdewebdev-3.5.10-xslt-api.patch

BuildRequires: gcc gcc-c++
BuildRequires: automake libtool
BuildRequires: desktop-file-utils
BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: perl-interpreter
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# should be optional but no hint support anymore
#Requires: gnupg
Requires: tidy

Provides: kdewebdev3 = %{version}-%{release}

Obsoletes: quanta < %{epoch}:%{version}-%{release}
Provides:  quanta = %{epoch}:%{version}-%{release}

%define kommander_ver 1.2.2
#Obsoletes: kommander < %{kommander_ver}-%{release}
Provides:  kommander = %{kommander_ver}-%{release}

%description
%{summary}, including:
* kfilereplace: batch search and replace tool
* kimagemapeditor: HTML image map editor
* klinkstatus: link checker
* kommander: visual dialog building tool
* kxsldbg: xslt Debugger
* quanta+: web development

%package devel
Summary: Header files and documentation for %{name} 
Provides: kdewebdev3-devel = %{version}-%{release}
Requires: kdelibs3-devel
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: quanta-devel < %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3%{?_isa} >= %{version}
# helps multilib upgrades
#Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:  %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 2 -a 3 -a 4
%patch -P0 -p0 -b .javascript
%patch -P1 -p1 -b .kxsldbg-icons
%patch -P3 -p1 -b .fix-freehand-crash
%patch -P4 -p1 -b .gcc46
%patch -P6 -p1 -b .docbParseFile

install -m644 -p %{SOURCE5} kxsldbg/

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .autoconf-2.7x
%patch -P305 -p1 -b .automake-1.16.5
%patch -P306 -p1 -b .ftbfs
%patch -P307 -p1 -b .configure-c99
%patch -P308 -p1 -b .ftbfs
%patch -P309 -p1 -b .ftbfs
%patch -P310 -p1 -b .xslt-api-change

make -f admin/Makefile.common cvs

%build
unset QTDIR && . /etc/profile.d/qt.sh

export CXXFLAGS="%{optflags} -std=gnu++98 -fpermissive -D FORCE_DEBUGGER"

%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

## package separately?  Why doesn't upstream include this? -- Rex
# install docs
for i in css html javascript ; do
   pushd $i
   ./install.sh <<EOF
%{buildroot}%{_datadir}/apps/quanta/doc
EOF
   popd
   rm -rf $i
done
cp -a php php.docrc %{buildroot}%{_datadir}/apps/quanta/doc/

# make symlinks relative
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd

# rpmdocs
for dir in k* quanta; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

%post
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun
if [ $1 -eq 0 ] ; then
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
fi

%posttrans
for f in crystalsvg locolor ; do
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%doc rpmdocs/*
%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/applications/kde/*
%{_datadir}/applnk/.hidden/*
%{_datadir}/apps/*
%doc %{_datadir}/apps/quanta/doc
%{_datadir}/config.kcfg/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_docdir}/HTML/en/*

%files libs
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%{_libdir}/lib*.so
%{_includedir}/kde/*

%changelog
%autochangelog
