%global source0_hash 695b6b8206c4c5cb2e61a31ee5d4be927474e469e5201443953a1e688844cc76

%define     version     0.177.5
%define     repoid      32988

Summary:    2ch client for KDE
Name:       kita
Version:    %{version}
Release:    44%{?dist}
Source:     http://downloads.sourceforge.jp/kita/%{repoid}/kita-%{version}.tar.gz
#Patch0:     kita-0.177.3-nonweak-symbol.patch
Patch10:    kita-0.177.5-g++44.patch
Patch11:    kita-0.177.5-ui-include-fix.patch
Patch12:    kita-0.177.5-acinclude-m4-syntax-fix.patch

# Overall		GPL-2.0-or-later
# kita/src/libkita/qcp932codec.cpp	MIT
# SPDX confirmed
License:    GPL-2.0-or-later AND MIT
URL:        http://sourceforge.jp/projects/kita/

BuildRequires:       gcc-c++
BuildRequires:       libart_lgpl-devel
BuildRequires:       kdelibs3-devel
BuildRequires:       libjpeg-devel

BuildRequires:       automake
BuildRequires:       libtool
BuildRequires:       desktop-file-utils
BuildRequires:       gettext
BuildRequires:       make

Requires:            mona-fonts-VLGothic

%description
Kita is a 2ch client for KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#%%patch0 -p2 -b .link
%patch -P10 -p1 -b .g++
%patch -P11 -p1 -b .include
%patch -P12 -p1 -b .syntax

# Support automake 1.11
%{__sed} -i.automake \
	-e 's|automake\*1\.10*|automake*1.1*|' \
	admin/cvs.sh

# Support autoconf 2.71
%{__sed} -i.autoconf \
	-e 's@autoconf\*2\.6\*@autoconf*2.6* | autoconf*2.7*@' \
	-e 's@autoheader\*2\.6\*@autoheader*2.6* | autoheader*2.7*@' \
	admin/cvs.sh

%{__sed} -i.soname \
   -e 's|kita_la_|libkitamain_la_|' \
   -e 's| kita\.la| libkitamain.la|' \
   -e 's|-avoid-version||' \
   kita/src/Makefile.{in,am}
	

sed -i -e 's|grep klineedit|grep -i klineedit|' \
	acinclude.m4 \
	admin/acinclude.m4.in \
	configure \
	%{nil}

%{__sed} -i.dsktop -e 's|Terminal=0|Terminal=false|' \
   kita/src/kita.desktop

make dist -f Makefile.cvs

%build
export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
if [ %{_lib} != lib ] ; then
   SUF=64
else
   SUF=
fi

unset QTDIR || :
. %{_sysconfdir}/profile.d/qt.sh

%configure \
    --disable-rpath \
    --enable-libsuffix=$SUF \
    --libdir=%{_libdir}/%{name} \
    --enable-xdg-menu

# -j2 failed
# make only succeeds with autoconf-2.63, not autoconf-2.64
# Don't know why... and I don't know where to investigate...
# For now using system-wide libtool
%{__make} -j1 \
	LIBTOOL=%{_bindir}/libtool

%install
%{__rm} -rf %{buildroot}

export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
%{__make} \
   kdelnkdir=%{_datadir}/applications \
   DESTDIR=%{buildroot} \
   install

desktop-file-install \
      --delete-original \
%if 0%{?fedora} < 19
      --vendor fedora \
%endif
      --dir %{buildroot}%{_datadir}/applications \
      --add-category KDE \
      --add-category Qt \
      --remove-category Application \
      %{buildroot}/%{_datadir}/applications/%{name}.desktop

# remove unneeded files
find %{buildroot}%{_libdir} -name \*.so -or -name \*.la | xargs %{__rm} -f

unlink %{buildroot}%{_datadir}/doc/HTML/en/kita/common
ln -sf ../common %{buildroot}%{_datadir}/doc/HTML/en/kita/common

# convert encoding
for f in README README.2ch TODO ; do
   iconv -f EUCJP -t UTF8 ${f} > ${f}.tmp && \
      ( touch -r ${f} ${f}.tmp ; %{__mv} -f ${f}.tmp ${f} )
   %{__rm} -f ${f}.tmp
done

# install mo file
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%defattr(-, root, root,-)
%doc AUTHORS
%license COPYING
%doc ChangeLog
%doc README
%doc README.2ch
%doc TODO
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/apps/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%{_datadir}/doc/HTML/en/kita/

%changelog
%autochangelog
