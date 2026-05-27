%global source0_hash none

#%%global devrel dev.12
%global devrel %{nil}

Summary: A text-based Web browser
Name: lynx
Version: 2.9.2
#Release: %%{devrel}.1%%{?dist}
Release: 5%{?dist}
License: GPL-2.0-only

Source0: https://invisible-island.net/archives/lynx/tarballs/lynx%{version}%{devrel}.tar.bz2
Source1: https://invisible-island.net/archives/lynx/tarballs/lynx%{version}%{devrel}.tar.bz2.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc

URL: https://lynx.invisible-island.net/

# RH specific tweaks - directory layout, utf-8 by default, misc. configuration
Patch0: lynx-2.8.9-redhat.patch

# patch preparing upstream sources for rpmbuild, in particular for parallel make
Patch1: lynx-2.8.9-build.patch

# prompt user before executing command via a lynxcgi link even in advanced mode,
# as the actual URL may not be shown but hidden behind an HTTP redirect and set
# TRUSTED_LYNXCGI:none in lynx.cfg to disable all lynxcgi URLs by default
# [CVE-2008-4690]
Patch2: lynx-CVE-2008-4690.patch

Provides: webclient
Provides: text-www-browser
BuildRequires: brotli-devel
BuildRequires: bzip2-devel
BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: libidn2-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: telnet
BuildRequires: unzip
BuildRequires: zip
BuildRequires: zlib-devel

# provides /usr/share/doc/HTML/en-US/index.html used as STARTFILE on RHEL
%if 0%{?rhel} && !0%{?eln}
Requires: redhat-indexhtml
%endif

%description
Lynx is a text-based Web browser. Lynx does not display any images,
but it does support frames, tables, and most other HTML tags. One
advantage Lynx has over graphical browsers is speed; Lynx starts and
exits quickly and swiftly displays web pages.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n lynx%{version}%{devrel}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
sed -e "s,^HELPFILE:.*,HELPFILE:file://localhost%{_pkgdocdir}/lynx_help/lynx_help_main.html,g" -i lynx.cfg
%if 0%{?rhel} && !0%{?eln}
sed -e 's,^STARTFILE:.*,STARTFILE:file:/usr/share/doc/HTML/en-US/index.html,' -i lynx.cfg
%endif

%build
# These options are specified explicitly below but are also defaults in 2.9.0:
#   --enable-addrlist-page
#   --enable-cjk
#   --enable-file-upload
#   --enable-japanese-utf8
#   --enable-justify-elts
#   --enable-locale-charset
#   --enable-persistent-cookies
#   --enable-prettysrc
#   --enable-read-eta
#   --enable-scrollbar
#   --enable-source-cache
#   --with-brotli
#   --with-bzlib
#   --with-zlib
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

# remove unneeded files
rm -f docs/{OS-390.announce,README.jp}
rm -f samples/*.bat

# convert line endings
dos2unix samples/lynx-demo.cfg
dos2unix samples/midnight.lss

cat >$RPM_BUILD_ROOT%{_sysconfdir}/lynx-site.cfg <<EOF
# Place any local lynx configuration options (proxies etc.) here.
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.2-5
- Prepare for Oreon 11 (RP1)
