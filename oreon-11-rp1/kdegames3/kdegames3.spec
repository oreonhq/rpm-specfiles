%global source0_hash 816b48ff61034e8d020efa55df397f893b63a87a417441db8bfba2eec3ce4c24
%define debug 0
%define final 0
%define donotcompilelist atlantik katomic kbattleship kblackbox kbounce kgoldrunner kjumpingcube klickety klines kmahjongg kmines knetwalk kolf konquest kpat kreversi ksame kshisen ksokoban kspaceduel ktron ktuberling kwin4 lskat
%global __brp_remove_la_files %nil
Name:    kdegames3
Summary:        KDE 3 Games not ported to KDE 4
Version: 3.5.10
Release:        1%{?dist}
License: GPL-2.0-only
Url:     http://www.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegames-%{version}.tar.bz2
Patch0: kdegames-3.5.10-trademarks.patch
Patch2: kdegames-3.5.10-ftbfs.patch
Patch3: kde3-autoconf-version.patch
Patch300: kde3-acinclude.patch
Patch301: kde3-automake-version.patch
Patch302: kde3-automake-add-missing.patch
Patch303: kdegames-configure-c99.patch
Patch304: kde3-autoconf-2.72.patch
Requires: kdelibs3 >= %{version}
Requires: hicolor-icon-theme kde-filesystem
Conflicts: kdegames < 6:3.80
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  kdelibs3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    pushd $lang_dir
      for i in *; do
        case "%{donotcompilelist}" in
          *$i*)
            [ -d $i ] && rm -rf $i
          ;;
        esac
      done
      rm -rf kdegames-apidocs
    popd
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi
for dir in atlantik k* ; do
  case "%{donotcompilelist}" in
    *$dir*)
    ;;
    *)
      for file in AUTHORS ChangeLog README TODO ; do
        test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
      done
    ;;
  esac
done
rm -rf %{buildroot}%{_includedir}/kde/k* %{buildroot}%{_libdir}/libkdegames.so
export QA_RPATHS=0x0001
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kdegames3-libs -f %{oreon_filedir}/kdegames3-libs.list

%changelog

%autochangelog
