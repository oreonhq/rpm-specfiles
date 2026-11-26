# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 174b7f2866a60f3247ba75f5c7dbb10b124aede4a1359312de15f3bfebd2050f
%global source1_hash 6c12f9bfeef6e7df055b27ea546c7adddaa9c53831b76e633ac771196671bb0f
%global source2_hash eec7eccb51a27ae633784d1b1ef42eb775130c782ea51a6c47fa7a901484d6db
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global devrel %{nil}

Summary: A text-based Web browser
Name: lynx
Version: 2.9.3
Release: 1%{?dist}
License: GPL-2.0-only

Source0: https://invisible-island.net/archives/lynx/tarballs/lynx%{version}%{devrel}.tar.bz2
Source1: https://invisible-island.net/archives/lynx/tarballs/lynx%{version}%{devrel}.tar.bz2.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc

URL: https://lynx.invisible-island.net/

Patch0: lynx-2.8.9-redhat.patch

Patch1: lynx-2.8.9-build.patch

Patch2: lynx-CVE-2008-4690.patch

Provides: webclient
Provides: text-www-browser
BuildRequires: oreon-rpm-macros
BuildRequires: brotli-devel
BuildRequires: bzip2-devel
BuildRequires: dos2unix
BuildRequires: clang
BuildRequires: gettext
BuildRequires: libidn2-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: unzip
BuildRequires: zip
BuildRequires: zlib-devel


%description
Lynx is a text-based Web browser. Lynx does not display any images,
but it does support frames, tables, and most other HTML tags. One
advantage Lynx has over graphical browsers is speed; Lynx starts and
exits quickly and swiftly displays web pages.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n lynx%{version}%{devrel}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
sed -e "s,^HELPFILE:.*,HELPFILE:file://localhost%{_pkgdocdir}/lynx_help/lynx_help_main.html,g" -i lynx.cfg
sed -e "s,^STARTFILE:.*,STARTFILE:https://oreonhq.com/," -i lynx.cfg

%build
%configure --libdir=/etc            \
    --disable-font-switch           \
    --disable-rpath-hack            \
    --enable-addrlist-page          \
    --enable-charset-choice         \
    --enable-cgi-links              \
    --enable-cjk                    \
    --enable-debug                  \
    --enable-default-colors         \
    --enable-externs                \
    --enable-file-upload            \
    --enable-gzip-help              \
    --enable-internal-links         \
    --enable-ipv6                   \
    --enable-japanese-utf8          \
    --enable-justify-elts           \
    --enable-locale-charset         \
    --enable-kbd-layout             \
    --enable-libjs                  \
    --enable-nls                    \
    --enable-nsl-fork               \
    --enable-persistent-cookies     \
    --enable-prettysrc              \
    --enable-read-eta               \
    --enable-scrollbar              \
    --enable-source-cache           \
    --enable-warnings               \
    --with-screen=ncursesw          \
    --with-ssl=%{_libdir}           \
    --with-brotli                   \
    --with-bzlib                    \
    --with-zlib                     \
    ac_cv_path_RLOGIN=/usr/bin/rlogin

%make_build

%install
chmod -x samples/mailto-form.pl
%make_install

rm -f docs/{OS-390.announce,README.jp}
rm -f samples/*.bat

dos2unix samples/lynx-demo.cfg
dos2unix samples/midnight.lss

cat >$RPM_BUILD_ROOT%{_sysconfdir}/lynx-site.cfg <<EOF
EOF

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc docs README samples
%doc test lynx.hlp lynx_help
%{_bindir}/lynx
%{_mandir}/man1/lynx.1.*
%config(noreplace) %{_sysconfdir}/lynx.cfg
%config(noreplace) %{_sysconfdir}/lynx.lss
%config(noreplace,missingok) %{_sysconfdir}/lynx-site.cfg

%changelog
%autochangelog
