%global source0_hash d12be7fb9170d650ae78197983fac05af21ddbf47f7b1a2a14de9aa832ed602c

Name:       ccgo
Version:    0.3.6.5
Release:    29%{?dist}
Summary:    An IGS (Internet Go Server) client written in C++
# *.cc and *.hh:    GPL-3.0-or-later
# COPYING:  GPL-3.0 text
## Unbundled
# aclocal.m4:   GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFULLR
# configure:    FSFUL
# compile:      GPL-2.0-or-later WITH Autoconf-exception-generic
# config.guess: GPL-3.0-or-later
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# depcomp:      GPL-2.0-or-later
# gettext.h:    GPL-3.0-or-later
# go/Makefile.in:   FSFULLRWD
# igs/Makefile.in:  FSFULLRWD
# igs/parser/Makefile.in:   FSFULLRWD
# install-sh:   X11 AND LicenseRef-Fedora-Public-Domain
# m4/gettext.m4:    FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLRWD
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
# po/Makefile.in.in:   "This file can be copied and used freely without restrictions"
License:    GPL-3.0-or-later
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Fedora-Public-Domain
URL:        http://ccdw.org/~cjj/prog/%{name}/
Source0:    %{url}src/%{name}-%{version}.tar.gz
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
# See <http://www.freedesktop.org/software/appstream/docs/> for more details.
Source1:    %{name}.appdata.xml
# Fix building against libsigc++-2.6.0, bug #1304679
Patch0:     ccgo-0.3.6.5-Port-to-libsigc-2.6.0.patch
# Adapt to assert() macro changes in glibc > 2.26, bug #1482990
Patch1:     ccgo-0.3.6.5-Adapt-to-glibc-assert-change.patch
# Update config.sub to support aarch64, bug #925132
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconfmm-2.6)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  sed
# Optional, but ccgo does not signal missing gnugo through GUI
Requires:       gnugo

%description
ccGo allows you to play go with GNU Go on your computer or with other players
on an Internet Go Server (IGS) on the Internet. It supports smart game format
(SGF) suitable for exchanging game records.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Make XDG desktop file compliant
sed -i -e '/^Encoding/d' -e '/^Categories/s/Application;//' \
    %{name}.desktop.in
# Update config.sub to support aarch64, bug #925132
# Remove bundled files
rm ABOUT-NLS aclocal.m4 configure compile config.guess config.sub depcomp gettext.h \
    go/Makefile.in igs/Makefile.in igs/parser/Makefile.in install-sh m4/* \
    Makefile.in missing po/Makefile.in.in
# gettextize breaks configure.ac. Rather symlink the header file.
ln -s /usr/share/gettext/gettext.h gettext.h
autoreconf -i -f

%build
%configure
%{make_build}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%install
%{make_install}

# Register as an application to be visible in the software center
install -d %{buildroot}%{_datadir}/appdata
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/ccgo
%{_mandir}/man6/ccgo.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ccgo
%{_datadir}/pixmaps/ccgo.xpm

%changelog
%autochangelog
