%global source0_hash 70727224a642c2f2c7739b82ebd0b4d6a6f444c9ad4311cf2a3c76230dd21d9e

Name:       scim-pinyin
Version:    0.5.92
Release:    31%{?dist}
Summary:    Smart Pinyin IMEngine for Smart Common Input Method platform

License:    GPL-2.0-only
URL:        https://github.com/scim-im/scim-pinyin
Source0:    http://dl.sourceforge.net/scim/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  scim-devel, gtk2-devel, gettext, gettext-devel, autoconf, automake,libtool
Requires:   scim
Obsoletes:  iiimf-le-chinput <= 0.3, miniChinput <= 0.0.3
Patch2:         scim-pinyin-showallkeys.patch
# Patch3:         scim-pinyin-helper.patch
# Patch4:         scim-pinyin-0.5.91-13.bz200702.patch
# Patch5:         scim-pinyin-help-translate.patch
Patch6:         scim-pinyin-0.5.91-save-in-temp.patch
# Patch7:         scim-pinyin-0.5.91-fix-load.patch
Patch8:         scim-pinyin-0.5.91-fix-ms-shuangpin.patch
# Patch9:         scim-pinyin-0.5.91-gcc43.patch

%description
Simplified Chinese Smart Pinyin IMEngine for SCIM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1 -b .2-showallkeys
# %patch3 -p1 -b .3-helperi
# %patch4 -p1 -b .4-bz200702
# %patch5 -p1 -b .5-translate
%patch -P6 -p1 -b .6-savetmp
# %patch7 -p1 -b .6-fix-load
%patch -P8 -p1 -b .8-fix-ms-shuangpin
# %patch9 -p1 -b .9-gcc43

%build
./bootstrap
%configure --disable-static
make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/Helper/*.la

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/scim-1.0/*/IMEngine/pinyin.so
%{_libdir}/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
%{_datadir}/scim/pinyin
%{_datadir}/scim/icons/smart-pinyin.png

%changelog
%autochangelog
