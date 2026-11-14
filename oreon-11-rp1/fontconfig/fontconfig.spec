# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4f7b554a38cdf78c033f666c8871f3749e14a094f65a07f630c91ed0b43d35e3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global freetype_version 2.9.1

Name: fontconfig
Version: 2.18.3
Release: 1%{?dist}
Summary: Font configuration and customization library
License: HPND AND LicenseRef-Fedora-Public-Domain AND Unicode-DFS-2016
URL: https://fontconfig.org
Source0: https://gitlab.freedesktop.org/api/v4/projects/890/packages/generic/fontconfig/%{version}/fontconfig-%{version}.tar.xz
Source1: 25-no-bitmap-oreon.conf
Source2: fc-cache

Patch0: %{name}-sleep-less.patch
Patch4: %{name}-drop-lang-from-pkgkit-format.patch
Patch6: %{name}-lower-nonlatin-conf.patch
Patch7: %{name}-update-fcgenericfamily.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gperf
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: fonts-srpm-macros
BuildRequires: libxml2-devel
BuildRequires: freetype-devel >= %{freetype_version}

Requires: freetype >= %{freetype_version}
Requires(pre): xml-common
Requires(postun): xml-common
Requires(post): grep
Requires(post): coreutils
Suggests: font(notosans)

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by
applications.

%package devel
Summary: Font configuration and customization library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: freetype-devel >= %{freetype_version}
Requires: pkgconfig
Requires: gettext
Provides: pkgconfig(fontconfig) = %{version}

%description devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which
will use fontconfig.

%package devel-doc
Summary: Development Documentation files for fontconfig library
BuildArch: noarch
Requires: %{name}-devel = %{version}-%{release}

%description devel-doc
The fontconfig-devel-doc package contains the documentation files
which is useful for developing applications that uses fontconfig.

%prep
%oreon_sha256

%autosetup -p1

mv conf.d/65-nonlatin.conf conf.d/69-nonlatin.conf
for f in test/*.json; do
  sed -i -e 's/65-nonlatin.conf/69-nonlatin.conf/g' $f
done

%build
%meson -Ddoc=disabled -Dcache-build=disabled -Dxml-backend=libxml2 \
       -Dadditional-fonts-dirs=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/TTF,/usr/local/share/fonts \
       -Dcache-dir=/usr/lib/fontconfig/cache \
       -Dtests-external-fonts=disabled \
       --default-library=shared
%meson_build

%install
%meson_install

install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/fonts/conf.d
ln -s %{_fontconfig_templatedir}/25-unhint-nonlatin.conf %{buildroot}%{_fontconfig_confdir}/

rm %{buildroot}%{_sysconfdir}/fonts/conf.d/10-sub-pixel-*.conf
rm %{buildroot}%{_sysconfdir}/fonts/conf.d/70-*bitmaps*.conf

install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man3
install -d %{buildroot}%{_mandir}/man5
for f in doc/*.1; do
  install -p -m 0644 $f %{buildroot}%{_mandir}/man1
done
for f in doc/*.3; do
  install -p -m 0644 $f %{buildroot}%{_mandir}/man3
done
for f in doc/*.5; do
  install -p -m 0644 $f %{buildroot}%{_mandir}/man5
done
for f in doc/*.txt doc/*.pdf doc/*.html; do
  install -p -m 0644 $f .
done

touch -r doc/fontconfig-user.sgml fontconfig-user.txt
touch -r doc/fontconfig-user.sgml fontconfig-user.html
touch -r doc/fontconfig-user.sgml fontconfig-user.pdf
touch -r doc/fontconfig-devel.sgml fontconfig-devel.txt
touch -r doc/fontconfig-devel.sgml fontconfig-devel.html
touch -r doc/fontconfig-devel.sgml fontconfig-devel.pdf

mv %{buildroot}%{_bindir}/fc-cache %{buildroot}%{_bindir}/fc-cache-%{__isa_bits}

echo ".so man1/fc-cache.1" > %{buildroot}%{_mandir}/man1/fc-cache-%{__isa_bits}.1

install -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/fc-cache

%find_lang %{name}
%find_lang %{name}-conf
cat %{name}-conf.lang >> %{name}.lang

%check
%meson_test

%post
umask 0022

mkdir -p /usr/lib/fontconfig/cache

[[ -d %{_localstatedir}/cache/fontconfig ]] && rm -rf %{_localstatedir}/cache/fontconfig/* 2> /dev/null || :

if [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache --version 2>&1 | grep -q %{version} ; then
  HOME=/root /usr/bin/fc-cache -f
fi

%transfiletriggerin -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
HOME=/root /usr/bin/fc-cache -s

%transfiletriggerpostun -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
HOME=/root /usr/bin/fc-cache -s

%posttrans
if [ -e %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system \
                        "urn:fontconfig:fonts.dtd" \
                        "file://%{_datadir}/xml/fontconfig/fonts.dtd" \
                        %{_sysconfdir}/xml/catalog
fi

%postun
if [ $1 == 0 ] && [ -e %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --del "urn:fontconfig:fonts.dtd" %{_sysconfdir}/xml/catalog
fi

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%doc fontconfig-user.txt fontconfig-user.html fontconfig-user.pdf
%doc %{_fontconfig_confdir}/README
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-cache*
%{_bindir}/fc-cat
%{_bindir}/fc-conflist
%{_bindir}/fc-genconf
%{_bindir}/fc-list
%{_bindir}/fc-match
%{_bindir}/fc-pattern
%{_bindir}/fc-query
%{_bindir}/fc-scan
%{_bindir}/fc-validate
%dir %{_fontbasedir}
%dir %{_fontconfig_masterdir}
%dir %{_fontconfig_confdir}
%dir %{_datadir}/fontconfig
%dir %{_fontconfig_templatedir}
%{_fontconfig_templatedir}/*.conf
%{_datadir}/xml/fontconfig
%config %{_fontconfig_masterdir}/fonts.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%dir /usr/lib/fontconfig
%dir /usr/lib/fontconfig/cache
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/*
%{_includedir}/fontconfig
%{_mandir}/man3/*
%{_datadir}/gettext/its/fontconfig.its
%{_datadir}/gettext/its/fontconfig.loc

%files devel-doc
%doc fontconfig-devel.txt fontconfig-devel.html fontconfig-devel.pdf

%changelog
%autochangelog
