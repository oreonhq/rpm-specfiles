%global source0_hash none

# Define before mingw-binutils is build
%bcond_with bootstrap

%global debug_package %{nil}

# Place RPM macros in %%{_rpmconfigdir}/macros.d if it exists (RPM 4.11+)
# Otherwise, use %%{_sysconfdir}/rpm
# https://lists.fedoraproject.org/pipermail/devel/2014-January/195026.html
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           mingw-filesystem
Version:        151
Release:        1%{?dist}
Summary:        MinGW cross compiler base filesystem and environment

License:        GPL-2.0-or-later
URL:            http://fedoraproject.org/wiki/MinGW
BuildArch:      noarch

Source0:        COPYING
Source1:        macros.mingw
Source2:        macros.mingw32
Source3:        macros.mingw64
Source4:        macros.ucrt64
Source5:        mingw32.sh
Source6:        mingw64.sh
Source7:        ucrt64.sh
Source8:        mingw-find-debuginfo.sh
Source9:        mingw.req
Source10:       mingw.prov
Source11:       mingw-scripts.sh
Source12:       mingw-rpmlint.config
Source13:       toolchain-mingw32.cmake
Source14:       toolchain-mingw64.cmake
Source15:       toolchain-ucrt64.cmake
Source16:       mingw-find-lang.sh
Source17:       mingw32.attr
Source18:       mingw64.attr
Source19:       ucrt64.attr
Source20:       toolchain-mingw32.meson
Source21:       toolchain-mingw64.meson
Source22:       toolchain-ucrt64.meson
Source23:       pkgconf-personality-mingw32
Source24:       pkgconf-personality-mingw64
Source25:       pkgconf-personality-ucrt64
Source26:       mingw32-hostlib.conf
Source27:       mingw64-hostlib.conf

# Taken from the Fedora filesystem package
Source101:      https://fedorahosted.org/filesystem/browser/lang-exceptions
Source102:      iso_639.sed
Source103:      iso_3166.sed

BuildRequires:  make
BuildRequires:  iso-codes
BuildRequires:  pkgconf


%description
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%package base
Summary:        Generic files which are needed for {mingw32,mingw64,ucrt64}-filesystem

# We need this for cmake macros
Requires:       cmake-rpm-macros
Requires:       redhat-rpm-config
# Obsolete the packages from the test repo
Obsoletes:      cross-filesystem < 67-2
Obsoletes:      cross-filesystem-scripts < 67-2
Obsoletes:      mingw-filesystem < 75-2
Obsoletes:      mingw-filesystem-scripts < 75-2
# For using pkgconf with MinGW
Requires:       pkgconf

%description base
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%package -n mingw32-filesystem
Summary:        MinGW cross compiler base filesystem and environment for the win32 target
Requires:       %{name}-base = %{version}-%{release}
# Replace mingw32-pkg-config
Conflicts:      mingw32-pkg-config < 0.28-17
Obsoletes:      mingw32-pkg-config < 0.28-17
Provides:       mingw32-pkg-config = 0.28-17
%if %{without bootstrap}
Requires:       mingw-binutils-generic
%endif

%description -n mingw32-filesystem
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%package -n mingw64-filesystem
Summary:        MinGW cross compiler base filesystem and environment for the win64 target
Requires:       %{name}-base = %{version}-%{release}
# Replace mingw64-pkg-config
Conflicts:      mingw64-pkg-config < 0.28-17
Obsoletes:      mingw64-pkg-config < 0.28-17
Provides:       mingw64-pkg-config = 0.28-17
%if %{without bootstrap}
Requires:       mingw-binutils-generic
%endif

%description -n mingw64-filesystem
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%package -n ucrt64-filesystem
Summary:        MinGW cross compiler base filesystem and environment for the win64 UCRT target
Requires:       %{name}-base = %{version}-%{release}
# Replace ucrt64-pkg-config
Conflicts:      ucrt64-pkg-config < 0.28-17
Obsoletes:      ucrt64-pkg-config < 0.28-17
Provides:       ucrt64-pkg-config = 0.28-17
%if %{without bootstrap}
Requires:       mingw-binutils-generic
%endif

%description -n ucrt64-filesystem
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c -T
cp %{SOURCE0} COPYING


%build
# nothing


%install
mkdir -p %{buildroot}%{_libexecdir}
install -m 755 %{SOURCE11} %{buildroot}%{_libexecdir}/mingw-scripts

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
for i in mingw32-configure mingw32-cmake mingw32-make mingw32-meson mingw32-pkg-config \
         mingw64-configure mingw64-cmake mingw64-make mingw64-meson mingw64-pkg-config \
         ucrt64-configure ucrt64-cmake ucrt64-make ucrt64-meson ucrt64-pkg-config ; do
  ln -s %{_libexecdir}/mingw-scripts $i
done
for i in i686-w64-mingw32-pkg-config  \
         x86_64-w64-mingw32-pkg-config \
         x86_64-w64-mingw32ucrt-pkg-config ; do
  ln -s %{_bindir}/pkgconf $i
done
popd

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/profile.d/
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/profile.d/
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/profile.d/

mkdir -p %{buildroot}%{macrosdir}
install -m 644 %{SOURCE1} %{buildroot}%{macrosdir}/macros.mingw
install -m 644 %{SOURCE2} %{buildroot}%{macrosdir}/macros.mingw32
install -m 644 %{SOURCE3} %{buildroot}%{macrosdir}/macros.mingw64
install -m 644 %{SOURCE4} %{buildroot}%{macrosdir}/macros.ucrt64

mkdir -p %{buildroot}%{_sysconfdir}/rpmlint
install -m 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/rpmlint/

for target in i686-w64-mingw32 x86_64-w64-mingw32 x86_64-w64-mingw32ucrt; do
  # Create the folders required for gcc and binutils
  mkdir -p %{buildroot}%{_prefix}/$target
  mkdir -p %{buildroot}%{_prefix}/$target/bin
  mkdir -p %{buildroot}%{_prefix}/$target/lib

  # The MinGW system root which will contain Windows native binaries
  # and Windows-specific header files, pkgconfig, etc.
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/bin
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/etc
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/include
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/include/sys
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/lib
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/lib/pkgconfig
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/lib/cmake
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/libexec
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/libexec/installed-tests
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/sbin

  # We don't normally package manual pages and info files, except
  # where those are not supplied by a Fedora native package.  So we
  # need to create the directories.
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/doc
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/info
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/man
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/man/man{1,2,3,4,5,6,7,8,l,n}
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/aclocal
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/themes
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/cmake
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/locale
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/pkgconfig
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/xml
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/icons
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/metainfo
  mkdir -p %{buildroot}%{_prefix}/$target/sys-root/mingw/share/installed-tests

  mkdir -p %{buildroot}%{_prefix}/lib/debug/%{_prefix}/$target
done

# Own folders for all locales
# Snippet taken from the Fedora filesystem package
sed -n -f %{SOURCE102} /usr/share/xml/iso-codes/iso_639.xml > %{buildroot}/iso_639.tab
sed -n -f %{SOURCE103} /usr/share/xml/iso-codes/iso_3166.xml > %{buildroot}/iso_3166.tab

grep -v "^$" %{buildroot}/iso_639.tab | grep -v "^#" | while read a b c d ; do
    [[ "$d" =~ "^Reserved" ]] && continue
    [[ "$d" =~ "^No linguistic" ]] && continue

    locale=$c
    if [ "$locale" = "XX" ]; then
        locale=$b
    fi
    echo "%lang(${locale}) %{_prefix}/i686-w64-mingw32/sys-root/mingw/share/locale/${locale}" >> filelist_mingw32
    echo "%lang(${locale}) %{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/locale/${locale}" >> filelist_mingw64
    echo "%lang(${locale}) %{_prefix}/x86_64-w64-mingw32ucrt/sys-root/mingw/share/locale/${locale}" >> filelist_ucrt
done

cat %{SOURCE101} | grep -v "^#" | grep -v "^$" | while read loc ; do
    locale=$loc
    locality=
    special=
    [[ "$locale" =~ "@" ]] && locale=${locale%%%%@*}
    [[ "$locale" =~ "_" ]] && locality=${locale##*_}
    [[ "$locality" =~ "." ]] && locality=${locality%%%%.*}
    [[ "$loc" =~ "_" ]] || [[ "$loc" =~ "@" ]] || special=$loc

    # If the locality is not official, skip it
    if [ -n "$locality" ]; then
        grep -q "^$locality" %{buildroot}/iso_3166.tab || continue
    fi
    # If the locale is not official and not special, skip it
    if [ -z "$special" ]; then
        grep -Eq "[[:space:]]${locale%%_*}[[:space:]]" %{buildroot}/iso_639.tab || continue
    fi
    echo "%lang(${locale}) %{_prefix}/i686-w64-mingw32/sys-root/mingw/share/locale/${loc}" >> filelist_mingw32
    echo "%lang(${locale}) %{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/locale/${loc}" >> filelist_mingw64
    echo "%lang(${locale}) %{_prefix}/x86_64-w64-mingw32ucrt/sys-root/mingw/share/locale/${loc}" >> filelist_ucrt
done

rm -f %{buildroot}/iso_639.tab
rm -f %{buildroot}/iso_3166.tab

cat filelist_mingw32 filelist_mingw64 filelist_ucrt | grep "locale" | while read a b ; do
    mkdir -p -m 755 %{buildroot}/$b/LC_MESSAGES
done

# NB. NOT _libdir
mkdir -p %{buildroot}/usr/lib/rpm
install -m 0755 %{SOURCE8} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE9} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE10} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE16} %{buildroot}%{_rpmconfigdir}

mkdir -p %{buildroot}/usr/lib/rpm/fileattrs
install -m 0644 %{SOURCE17} %{buildroot}%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE18} %{buildroot}%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE19} %{buildroot}%{_rpmconfigdir}/fileattrs/

mkdir -p %{buildroot}%{_datadir}/mingw
install -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/mingw/
install -m 0644 %{SOURCE14} %{buildroot}%{_datadir}/mingw/
install -m 0644 %{SOURCE15} %{buildroot}%{_datadir}/mingw/
install -m 0644 %{SOURCE20} %{buildroot}%{_datadir}/mingw/
install -m 0644 %{SOURCE21} %{buildroot}%{_datadir}/mingw/
install -m 0644 %{SOURCE22} %{buildroot}%{_datadir}/mingw/

mkdir -p %{buildroot}%{pkgconfig_personalitydir}
install -m 0644 %{SOURCE23} %{buildroot}%{pkgconfig_personalitydir}/i686-w64-mingw32.personality
install -m 0644 %{SOURCE24} %{buildroot}%{pkgconfig_personalitydir}/x86_64-w64-mingw32.personality
install -m 0644 %{SOURCE25} %{buildroot}%{pkgconfig_personalitydir}/x86_64-w64-mingw32ucrt.personality

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
install -m 0644 %{SOURCE26} %{buildroot}%{_sysconfdir}/ld.so.conf.d/mingw32-hostlib.conf
install -m 0644 %{SOURCE27} %{buildroot}%{_sysconfdir}/ld.so.conf.d/mingw64-hostlib.conf

# Link mingw-pkg-config man pages to pkgconf(1)
mkdir -p %{buildroot}%{_mandir}/man1/
echo ".so man1/pkgconf.1" > %{buildroot}%{_mandir}/man1/i686-w64-mingw32-pkg-config.1
echo ".so man1/pkgconf.1" > %{buildroot}%{_mandir}/man1/x86_64-w64-mingw32-pkg-config.1
echo ".so man1/pkgconf.1" > %{buildroot}%{_mandir}/man1/x86_64-w64-mingw32ucrt-pkg-config.1


%files base
%doc COPYING
%dir %{_sysconfdir}/rpmlint/
%config(noreplace) %{_sysconfdir}/rpmlint/mingw-rpmlint.config
%{macrosdir}/macros.mingw
%{_libexecdir}/mingw-scripts
%{_rpmconfigdir}/mingw*
%dir %{_datadir}/mingw/

%files -n mingw32-filesystem
%{macrosdir}/macros.mingw32
%config(noreplace) %{_sysconfdir}/profile.d/mingw32.sh
%{_bindir}/mingw32-configure
%{_bindir}/mingw32-cmake
%{_bindir}/mingw32-make
%{_bindir}/mingw32-meson
%{_bindir}/mingw32-pkg-config
%{_bindir}/i686-w64-mingw32-pkg-config
%{_prefix}/i686-w64-mingw32
%{_rpmconfigdir}/fileattrs/mingw32.attr
%{_datadir}/mingw/toolchain-mingw32.cmake
%{_datadir}/mingw/toolchain-mingw32.meson
%{pkgconfig_personalitydir}/i686-w64-mingw32.personality
%{_mandir}/man1/i686-w64-mingw32-pkg-config.1*
%{_sysconfdir}/ld.so.conf.d/mingw32-hostlib.conf
%dir %{_prefix}/lib/debug/%{_prefix}
%dir %{_prefix}/lib/debug/%{_prefix}/i686-w64-mingw32


%files -n mingw64-filesystem
%{macrosdir}/macros.mingw64
%config(noreplace) %{_sysconfdir}/profile.d/mingw64.sh
%{_bindir}/mingw64-configure
%{_bindir}/mingw64-cmake
%{_bindir}/mingw64-make
%{_bindir}/mingw64-meson
%{_bindir}/mingw64-pkg-config
%{_bindir}/x86_64-w64-mingw32-pkg-config
%{_prefix}/x86_64-w64-mingw32
%{_rpmconfigdir}/fileattrs/mingw64.attr
%{_datadir}/mingw/toolchain-mingw64.cmake
%{_datadir}/mingw/toolchain-mingw64.meson
%{pkgconfig_personalitydir}/x86_64-w64-mingw32.personality
%{_mandir}/man1/x86_64-w64-mingw32-pkg-config.1*
%{_sysconfdir}/ld.so.conf.d/mingw64-hostlib.conf
%dir %{_prefix}/lib/debug/%{_prefix}
%dir %{_prefix}/lib/debug/%{_prefix}/x86_64-w64-mingw32


%files -n ucrt64-filesystem
%{macrosdir}/macros.ucrt64
%config(noreplace) %{_sysconfdir}/profile.d/ucrt64.sh
%{_bindir}/ucrt64-configure
%{_bindir}/ucrt64-cmake
%{_bindir}/ucrt64-make
%{_bindir}/ucrt64-meson
%{_bindir}/ucrt64-pkg-config
%{_bindir}/x86_64-w64-mingw32ucrt-pkg-config
%{_prefix}/x86_64-w64-mingw32ucrt
%{_rpmconfigdir}/fileattrs/ucrt64.attr
%{_datadir}/mingw/toolchain-ucrt64.cmake
%{_datadir}/mingw/toolchain-ucrt64.meson
%{pkgconfig_personalitydir}/x86_64-w64-mingw32ucrt.personality
%{_mandir}/man1/x86_64-w64-mingw32ucrt-pkg-config.1*
%dir %{_prefix}/lib/debug/%{_prefix}
%dir %{_prefix}/lib/debug/%{_prefix}/x86_64-w64-mingw32ucrt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 151-1
- Prepare for Oreon 11 (RP1)
