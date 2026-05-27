%global source0_hash 355b4cbbed880b0381a04c46617b7656e362585d52e9cf84a67e2009b749ff11

%bcond compat_libs %[!(0%{?rhel} >= 10) || %{defined eln}]
%bcond gpm %[!(0%{?rhel} >= 10)]

Summary: Ncurses support utilities
Name: ncurses
Version: 6.6
Release: 1%{?dist}
License: MIT-open-group
URL: https://invisible-island.net/ncurses/ncurses.html
Source0: https://invisible-mirror.net/archives/ncurses/ncurses-%{version}.tar.gz
Source1: https://invisible-mirror.net/archives/ncurses/ncurses-%{version}.tar.gz.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc

Patch8: ncurses-config.patch
Patch9: ncurses-libs.patch
Patch11: ncurses-urxvt.patch
BuildRequires: gcc gcc-c++ gnupg2 make pkgconfig
%{?with_gpm:BuildRequires: gpm-devel}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains support utilities, including a terminfo compiler
tic, a decompiler infocmp, clear, tput, tset, and a termcap conversion
tool captoinfo.

%package libs
Summary: Ncurses libraries
Requires: %{name}-base = %{version}-%{release}

%description libs
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains the ncurses libraries.

%if %{with compat_libs}
%package compat-libs
Summary: Ncurses compatibility libraries
Requires: %{name}-base = %{version}-%{release}

%description compat-libs
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains the ABI version 5 of the ncurses libraries for
compatibility.
%endif

%package c++-libs
Summary: Ncurses C++ bindings
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description c++-libs
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

This package contains C++ bindings of the ncurses ABI version 6 libraries.

%package base
Summary: Descriptions of common terminals
BuildArch: noarch

%description base
This package contains descriptions of common terminals. Other terminal
descriptions are included in the ncurses-term package.

%package term
Summary: Terminal descriptions
Requires: %{name}-base = %{version}-%{release}
BuildArch: noarch

%description term
This package contains additional terminal descriptions not found in
the ncurses-base package.

%package devel
Summary: Development files for the ncurses library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-c++-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The header files and libraries for developing applications that use
the ncurses terminal handling library.

Install the ncurses-devel package if you want to develop applications
which will use ncurses.

%package static
Summary: Static libraries for the ncurses library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The ncurses-static package includes static libraries of the ncurses library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}

%setup -q -n %{name}-%{version}

%patch -P8 -p1 -b .config
%patch -P9 -p1 -b .libs
%patch -P11 -p1 -b .urxvt

%build
common_options="\
    --enable-colorfgbg \
    --enable-hard-tabs \
    --enable-overwrite \
    --enable-pc-files \
    --enable-xmc-glitch \
    --disable-root-access \
    --disable-setuid-environ \
    --disable-stripping \
    --disable-wattr-macros \
    --with-cxx-shared \
    --with-ospeed=unsigned \
    --with-pkg-config-libdir=%{_libdir}/pkgconfig \
    --with-shared \
    --with-terminfo-dirs=%{_sysconfdir}/terminfo:%{_datadir}/terminfo \
    --with-termlib=tinfo \
    --with-ticlib=tic \
    --with-xterm-kbs=DEL \
%{!?with_gpm:--without-gpm} \
    --without-ada"
abi5_options="--with-chtype=long"

for abi in %{?with_compat_libs:5} 6; do
    for char in narrowc widec; do
        mkdir $char$abi
        pushd $char$abi
        ln -s ../configure .

        [ $abi = 6 -a $char = widec ] && progs=yes || progs=no

        %configure $(
            echo $common_options --with-abi-version=$abi
            [ $abi = 5 ] && echo $abi5_options
            [ $char = widec ] && echo --enable-widec || echo --disable-widec
            [ $progs = yes ] || echo --without-progs
        )

        %make_build libs
        [ $progs = yes ] && %make_build -C progs

        popd
    done
done

%install
%if %{with compat_libs}
make -C narrowc5 DESTDIR=$RPM_BUILD_ROOT install.libs
rm ${RPM_BUILD_ROOT}%{_libdir}/lib{tic,tinfo}.so.5*
make -C widec5 DESTDIR=$RPM_BUILD_ROOT install.libs
%endif
make -C narrowc6 DESTDIR=$RPM_BUILD_ROOT install.libs
rm ${RPM_BUILD_ROOT}%{_libdir}/lib{tic,tinfo}.so.6*
make -C widec6 DESTDIR=$RPM_BUILD_ROOT install.{libs,progs,data,includes,man}

chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/lib*.so.*.*
chmod 644 ${RPM_BUILD_ROOT}%{_libdir}/lib*.a

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/terminfo

baseterms=

# prepare -base and -term file lists
for termname in \
    alacritty ansi dumb foot\* linux vt100 vt100-nav vt102 vt220 vt52 \
    Eterm\* aterm bterm cons25 cygwin eterm\* gnome gnome-256color hurd jfbterm \
    kitty konsole konsole-256color mach\* mlterm mrxvt nsterm putty{,-256color} pcansi \
    rxvt{,-\*} screen{,5,-\*color,.[^mlp]\*,.linux,.mlterm\*,.putty{,-256color},.mrxvt} \
    st{,-\*color} sun teraterm teraterm2.3 tmux{,-\*} vte vte-256color vwmterm \
    wsvt25\* xfce xterm xterm-\*
do
    for i in $RPM_BUILD_ROOT%{_datadir}/terminfo/?/$termname; do
        for t in $(find $RPM_BUILD_ROOT%{_datadir}/terminfo -samefile $i); do
            baseterms="$baseterms $(basename $t)"
        done
    done
done 2> /dev/null
for t in $baseterms; do
    echo "%dir %{_datadir}/terminfo/${t::1}"
    echo %{_datadir}/terminfo/${t::1}/$t
done 2> /dev/null | sort -u > terms.base
find $RPM_BUILD_ROOT%{_datadir}/terminfo \! -type d | \
    sed "s|^$RPM_BUILD_ROOT||" | while read t
do
    echo "%dir $(dirname $t)"
    echo $t
done 2> /dev/null | sort -u | comm -2 -3 - terms.base > terms.term

# can't replace directory with symlink (rpm bug), symlink all headers
mkdir $RPM_BUILD_ROOT%{_includedir}/ncurses{,w}
for l in $RPM_BUILD_ROOT%{_includedir}/*.h; do
    ln -s ../$(basename $l) $RPM_BUILD_ROOT%{_includedir}/ncurses
    ln -s ../$(basename $l) $RPM_BUILD_ROOT%{_includedir}/ncursesw
done

# don't require -ltinfo when linking with --no-add-needed
for l in $RPM_BUILD_ROOT%{_libdir}/libncurses{,w}.so; do
    soname=$(basename $(readlink $l))
    rm -f $l
    echo "INPUT($soname -ltinfo)" > $l
done

rm -f $RPM_BUILD_ROOT%{_libdir}/libcurses{,w}.so
echo "INPUT(-lncurses)" > $RPM_BUILD_ROOT%{_libdir}/libcurses.so
echo "INPUT(-lncursesw)" > $RPM_BUILD_ROOT%{_libdir}/libcursesw.so

echo "INPUT(-ltinfo)" > $RPM_BUILD_ROOT%{_libdir}/libtermcap.so

rm -f $RPM_BUILD_ROOT%{_bindir}/ncurses*5-config
rm -f $RPM_BUILD_ROOT{%{_libdir},/usr/lib}/terminfo
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*_g.pc

xz NEWS

%ldconfig_scriptlets libs

%ldconfig_scriptlets c++-libs

%if %{with compat_libs}
%ldconfig_scriptlets compat-libs
%endif

%files
%doc ANNOUNCE AUTHORS NEWS.xz README TO-DO
%{_bindir}/[cirt]*
%{_mandir}/man1/[cirt]*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files libs
%exclude %{_libdir}/libncurses++*.so.6*
%{_libdir}/lib*.so.6*

%if %{with compat_libs}
%files compat-libs
%{_libdir}/lib*.so.5*
%endif

%files c++-libs
%{_libdir}/libncurses++*.so.6*

%files base -f terms.base
%license COPYING
%doc README
%dir %{_sysconfdir}/terminfo
%{_datadir}/tabset
%dir %{_datadir}/terminfo

%files term -f terms.term

%files devel
%doc doc/html/hackguide.html
%doc doc/html/ncurses-intro.html
%doc c++/README*
%doc misc/ncurses.supp
%{_bindir}/ncurses*-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/ncurses
%dir %{_includedir}/ncursesw
%{_includedir}/ncurses/*.h
%{_includedir}/ncursesw/*.h
%{_includedir}/*.h
%{_mandir}/man1/ncurses*-config*
%{_mandir}/man3/*

%files static
%{_libdir}/lib*.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6-1
- Prepare for Oreon 11 (RP1)
