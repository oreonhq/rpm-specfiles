%global source0_hash b1311e5e749917c6a26e59ab1deadf56ccb8f71cc105355f511323b36501f968

Name:           shigofumi
Version:        0.9
Release:        15%{?dist}
Summary:        Command line client for accessing the Czech Data Boxes
# COPYING:          GPL-3.0 text
# README:           GPL-3.0-or-later
# src/gettext.h:    LGPL-2.1-or-later
# src/shigofumi.c:  GPL-3.0-or-later
## Not in the binary packages
# aclocal.m4:       GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFULLRWD
# compile:          GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:       GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.guess:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.rpath:     FSFULLR
# configure:        FSFUL
# depcomp:          GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/Makefile.in:  FSFULLRWD
# doc/po/cs/Makefile.in:    FSFULLRWD
# doc/po/Makefile.in:       FSFULLRWD
# install-sh:       X11 AND LicenseRef-Fedora-Public-Domain
# m4/gettext.m4:    FSFULLR
# m4/host-cpu-c-abi.m4: FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# m4/readline.m4:   GPL-1.0-or-later WITH Autoconf-exception-generic
# Makefile.in:      FSFULLRWD
# missing:          GPL-2.0-or-later WITH Autoconf-exception-generic
# po/insert-header.sin: FSFUL
# po/Makefile.in.in:    FSFAP
# po/remove-potcdate.sin:   FSFAP
# po/Rules-quot:    FSFUL
# src/Makefile.in:  FSFULLRWD
# test/Makefile.in: FSFULLRWD
# test-driver:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-1.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP AND LicenseRef-Fedora-Public-Domain
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# Fix building with GCC 12, in upstream after 0.9
Patch0:         shigofumi-0.9-Fix-building-with-GCC-12.patch
# Fix use-after-frees when handling XML ISDS documents, in upstream after 0.9
Patch1:         shigofumi-0.9-Fix-two-use-after-frees-when-handling-XML-ISDS-docum.patch
# Adapt to changes in libxml2-2.12.0, in upstream after 0.9
Patch2:         shigofumi-0.9-Fix-building-with-libxml2-2.12.0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  gettext-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libisds) >= 0.10.7
BuildRequires:  readline-devel

%description
This is Shigofumi, an ISDS (Informační systém datových schránek / Data Box
Information System) client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build
%configure \
    --disable-debug \
    --enable-doc \
    --enable-fatalwarnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-xattr
%{make_build}

%install
%{make_install}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO ChangeLog
%{_bindir}/shigofumi
%{_mandir}/man1/shigofumi.*
%{_mandir}/*/man1/shigofumi.*
%{_mandir}/man5/shigofumirc.*
%{_mandir}/*/man5/shigofumirc.*

%changelog
%autochangelog
