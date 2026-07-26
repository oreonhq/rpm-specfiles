%global source0_hash 816b48ff61034e8d020efa55df397f893b63a87a417441db8bfba2eec3ce4c24

%define debug 0
%define final 0

# These games are already in KDE 4.
%define donotcompilelist atlantik katomic kbattleship kblackbox kbounce kgoldrunner kjumpingcube klickety klines kmahjongg kmines knetwalk kolf konquest kpat kreversi ksame kshisen ksokoban kspaceduel ktron ktuberling kwin4 lskat

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:    kdegames3
Summary: KDE 3 Games not ported to KDE 4
Version: 3.5.10
Release: 53%{?dist}

License: GPL-2.0-only
Url:     http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegames-%{version}.tar.bz2
Patch0: kdegames-3.5.10-trademarks.patch
# fix FTBFS with the new stricter ld in F13 (#565113)
Patch2: kdegames-3.5.10-ftbfs.patch
Patch3: kde3-autoconf-version.patch
# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
Patch303: kdegames-configure-c99.patch
# fix build with autoconf 2.72
Patch304: kde3-autoconf-2.72.patch

Requires: kdelibs3 >= %{version}
# directory ownership
Requires: hicolor-icon-theme kde-filesystem

Conflicts: kdegames < 6:3.80

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: automake libtool
BuildRequires: make

%description
Games and gaming libraries for KDE which have not been ported to KDE 4 yet.
Included with this package are: kasteroids, kbackgammon,
kenolaba, kfouleggs, kpoker, ksirtet, ksmiletris, ksnakerace.

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3 >= %{version}
License: LGPLv2
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kdegames-%{version}
%patch -P0 -p1
%patch -P2 -p1 -b .ftbfs
%patch -P3 -p1 -b .autoconf2.7x

export DO_NOT_COMPILE="%{donotcompilelist}"

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1
%patch -P304 -p1
make -f admin/Makefile.common cvs

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export DO_NOT_COMPILE="%{donotcompilelist}"

%configure \
   --disable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
%if %{final}
   --enable-final \
%endif
%if %{debug} == 0
   --disable-debug \
   --disable-warnings \
%endif
   --includedir=%{_includedir}/kde \
   --disable-setgid

%make_build

%install
export DO_NOT_COMPILE="%{donotcompilelist}"
%make_install

# locales
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    # remove documentation for games we don't ship
    pushd $lang_dir
      for i in *; do
        case "%{donotcompilelist}" in
          *$i*)
            # $i is listed in %{donotcompilelist}, zap
            [ -d $i ] && rm -rf $i
          ;;
        esac
      done
      rm -rf kdegames-apidocs
    popd
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# rpmdocs
for dir in atlantik k* ; do
  case "%{donotcompilelist}" in
    *$dir*)
      # $dir is listed in %{donotcompilelist}, skip
    ;;
    *)
      for file in AUTHORS ChangeLog README TODO ; do
        test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
      done
    ;;
  esac
done

# remove libkdegames devel stuff, not used by anything and conflicts with KDE 4
rm -rf %{buildroot}%{_includedir}/kde/k* %{buildroot}%{_libdir}/libkdegames.so

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

%files -f %{name}.lang
%doc AUTHORS README
%doc rpmdocs/*
%license COPYING*
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%{_datadir}/config.kcfg/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*

%ldconfig_scriptlets libs

%files libs
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%changelog
%autochangelog
