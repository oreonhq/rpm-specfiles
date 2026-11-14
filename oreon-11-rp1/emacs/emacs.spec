# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1da5790d9580c81932b5bf700633114468da7b3412d69faa767daebf974f4586

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond gpm 0
%bcond treesitter 0

Summary:       GNU Emacs text editor
Name:          emacs
Epoch:         1
Version:       31.1
Release:       1%{?dist}
License:       GPL-3.0-or-later AND CC0-1.0
URL:           https://www.gnu.org/software/emacs/

Source0:       https://mirror.cs.odu.edu/gnu/emacs/emacs-%{version}.tar.xz
Source1:       https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz.sig
Source2:       emacs-keyring.asc

Source4:       dotemacs.el
Source5:       site-start.el
Source6:       default.el

Source10:      emacs_lisp.attr
Source11:      emacs_lisp.rec

Patch:         0001-Pong-and-Tetris-are-excluded.patch
Patch:         emacs-spellchecker.patch
Patch:         emacs-system-crypto-policies.patch
Patch:         0001-Don-t-specify-StartupWMClass-in-emacs.desktop.patch
Patch:         0001-flymake.el-Generalize-trusted-content-p-check-to-all.patch
Patch:         emacs-metainfo-internet.patch

BuildRequires: oreon-rpm-macros
BuildRequires: bzip2
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gnupg2
BuildRequires: gnutls-devel
BuildRequires: gzip
BuildRequires: libacl-devel
BuildRequires: libgccjit-devel
BuildRequires: libselinux-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: sqlite-devel
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: texinfo
BuildRequires: zlib-devel
BuildRequires: appstream

%if %{with treesitter}
BuildRequires: pkgconfig(tree-sitter)
%endif

%if %{with gpm}
BuildRequires: gpm-devel
%endif

%define site_lisp %{_datadir}/emacs/site-lisp
%define site_start_d %{site_lisp}/site-start.d
%define pkgconfig %{_datadir}/pkgconfig
%define emacs_libexecdir %{_libexecdir}/emacs/%{version}/%{_host}
%define native_lisp %{_libdir}/emacs/%{version}/native-lisp

%global desc %{expand:GNU Emacs is a powerful, customizable, self-documenting, modeless text
editor. It contains special code editing features, a scripting language
(elisp), and the capability to read mail, news, and more without leaving
the editor.
}

Provides:      emacs(bin) = %{epoch}:%{version}-%{release}
Requires:      emacs-nw = %{epoch}:%{version}-%{release}

%description
%desc

%package nw
Summary:       GNU Emacs text editor with no window system support
Requires(preun): /usr/sbin/alternatives
Requires(posttrans): /usr/sbin/alternatives
Requires:      emacs-common = %{epoch}:%{version}-%{release}
Provides:      emacs-nox = %{epoch}:%{version}-%{release}
Obsoletes:     emacs-nox < 1:30

%description nw
%desc
This package provides an emacs-nw binary without graphical display
support, for running on a terminal only.

%package -n emacsclient
Summary:       Remotely control GNU Emacs
Conflicts:     emacs-common < 1:29.4-12

%description -n emacsclient
%desc
This package provides emacsclient, which can be used to control an Emacs
server.

%package common
Summary:       Emacs common files
License:       GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND BSD-3-Clause
Requires(preun): /usr/sbin/alternatives
Requires(posttrans): /usr/sbin/alternatives
Requires:      /usr/bin/readlink
Requires:      %{name}-filesystem >= 1:30.2
Requires:      emacsclient
Requires:      libgccjit
Recommends:    emacs = %{epoch}:%{version}-%{release}
Recommends:    info
Provides:      %{name}-el = %{epoch}:%{version}-%{release}
Obsoletes:     emacs-el < 1:24.3-29
Provides:      emacs-transient = 0.7.2.2
Obsoletes:     emacs-transient < 0.3.0-4
Recommends:    /usr/bin/git
Recommends:    gcc

%global _local_file_attrs emacs_lisp
%{load:%SOURCE10}
%global __emacs_lisp_recommends \
        %{_builddir}/%{name}-%{version}/build-nw/src/emacs -x %SOURCE11

%description common
%desc
This package contains all the common files needed by emacs and emacs-nw.

%package devel
Summary: Development header files for Emacs

%description devel
Development header files for Emacs.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}

%autosetup -N -c
cd %{name}-%{version}
%autopatch -p1

rm lisp/play/pong.el lisp/play/pong.elc \
   lisp/play/tetris.el lisp/play/tetris.elc

%ifarch %{ix86}
%define setarch setarch %{_arch} -R
%else
%define setarch %{nil}
%endif

cd ..
mv %{name}-%{version} build-nw

%build
export CFLAGS="-DMAIL_USE_LOCKF %{build_cflags}"
%set_build_flags

cd build-nw
%configure \
           --disable-gc-mark-trace \
           --with-modules \
           --with-native-compilation=aot \
           --with-sqlite3 \
           --with-systemduserunitdir=%{_userunitdir} \
%if %{with treesitter}
           --with-tree-sitter \
%else
           --without-tree-sitter \
%endif
%if %{without gpm}
           --with-gpm=no \
%endif
           --with-x=no \
    || ( cat config.log && false )
%{setarch} %make_build bootstrap
%{setarch} %make_build
cd ..

cat > emacs.pc << EOF
sitepkglispdir=%{site_lisp}
sitestartdir=%{site_start_d}

Name: emacs
Description: GNU Emacs text editor
Version: %{epoch}:%{version}
EOF

cat > macros.emacs << EOF
%%_emacs_version %{version}
%%_emacs_ev %{?epoch:%{epoch}:}%{version}
%%_emacs_evr %{?epoch:%{epoch}:}%{version}-%{release}
%%_emacs_archsitelispdir %%{_libdir}/emacs/site-lisp
%%_emacs_sitelispdir %{site_lisp}
%%_emacs_sitestartdir %{site_start_d}
%%_emacs_bytecompile(W) /usr/bin/emacs -batch --no-init-file --no-site-file --eval '(push nil load-path)' %%{-W:--eval '(setq byte-compile-error-on-warn t)' }-f batch-byte-compile %%*
EOF

cat > 00-dynamic-module-dir.el << 'EOF'
;;; 00-dynamic-module-dir.el --- Add arch-specifc dir to load-path -*- lexical-binding: t -*-

;;; Commentary:
;;
;; This directory is for installing Emacs dynamic modules into.  See
;; also RPM macro %%_emacs_archsitelispdir.

(add-to-list 'load-path "%{_libdir}/emacs/site-lisp")

;;; 00-dynamic-module-dir.el ends here
EOF

cat > 10-source-directory.el << 'EOF'
;;; 10-source-directory.el --- Set source-directory -*- lexical-binding: t -*-

;;; Commentary:
;;
;; Function `update-directory-autoloads' needs this to work.

(setq source-directory "%{_datadir}/emacs/%{version}/")

;;; 10-source-directory.el ends here
EOF

%install
cd build-nw
%make_install
cd ..

gunzip %{buildroot}%{_datadir}/emacs/%{version}/lisp/jka-compr.el.gz
gunzip %{buildroot}%{_datadir}/emacs/%{version}/lisp/jka-cmpr-hook.el.gz

mv %{buildroot}%{_bindir}/emacs-%{version} %{buildroot}%{_bindir}/emacs-%{version}-nw
ln -s emacs-%{version}-nw %{buildroot}%{_bindir}/emacs-nw
ln -s emacs-%{version}-nw %{buildroot}%{_bindir}/emacs-%{version}-nox
ln -s emacs-%{version}-nw %{buildroot}%{_bindir}/emacs-nox

chmod 755 %{buildroot}%{emacs_libexecdir}/movemail

mkdir -p %{buildroot}%{site_lisp} %{buildroot}%{site_start_d}
install -p -m 0644 %SOURCE5 %{buildroot}%{site_lisp}/site-start.el
install -p -m 0644 %SOURCE6 %{buildroot}%{site_lisp}
install -p -m 0644 00-dynamic-module-dir.el %{buildroot}%{site_start_d}/
install -p -m 0644 10-source-directory.el %{buildroot}%{site_start_d}/

mkdir -p %{buildroot}%{_sysconfdir}/skel
install -p -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/skel/.emacs

mkdir -p %{buildroot}/%{pkgconfig}
install -p -m 0644 emacs.pc %{buildroot}/%{pkgconfig}

mkdir -p \
      %{buildroot}%{_fileattrsdir} \
      %{buildroot}%{_rpmconfigdir} \
      %{buildroot}%{_rpmmacrodir}
install -p -m 0644 %SOURCE10 %{buildroot}%{_fileattrsdir}
install -p -m 0755 %SOURCE11 %{buildroot}%{_rpmconfigdir}
install -p -m 0644 macros.emacs %{buildroot}%{_rpmmacrodir}

rm -f %{buildroot}%{_infodir}/dir

rm -f %{buildroot}%{_datadir}/%{name}/%{version}/etc/%{name}.{desktop,metainfo.xml,service} \
      %{buildroot}%{_datadir}/%{name}/%{version}/etc/%{name}-mail.desktop \
      %{buildroot}%{_datadir}/%{name}/%{version}/etc/org.gnu.emacs.defaults.gschema.xml \
      %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnu.emacs.defaults.gschema.xml

rm -f %{buildroot}%{_datadir}/applications/emacsclient.desktop
rm -f %{buildroot}%{_datadir}/applications/emacsclient-mail.desktop

rm -f *-filelist common-*-files el-*-files

( TOPDIR=${PWD}
  cd %{buildroot}

  find .%{_datadir}/emacs/%{version}/lisp .%{site_lisp} \
    \( -type f -name '*.elc' -fprint $TOPDIR/common-lisp-none-elc-files \) -o \( -type d -fprintf $TOPDIR/common-lisp-dir-files "%%%%dir %%p\n" \) -o \( -name '*.el.gz' -fprint $TOPDIR/el-bytecomped-files -o -fprint $TOPDIR/common-not-comped-files \)

)

sed -i -e "s|\.%{_prefix}|%{_prefix}|" *-files
grep -vhE '%{site_lisp}(|/(default\.el|site-start\.d|site-start\.el))$' {common,el}-*-files > common-filelist

rm -f %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document23.svg

(TOPDIR=${PWD}
 cd %{buildroot}
 find ".%{native_lisp}/$(ls $TOPDIR/build-nw/native-lisp)" \
      \( -type f -name '*eln' -fprintf "$TOPDIR/nw-filelist" "%%%%attr(755,-,-) %%p\n" \) \
      -o \( -type d -fprintf "$TOPDIR/nw-dirlist" "%%%%dir %%p\n" \)
)
echo "%{emacs_libexecdir}/emacs-$(./build-nw/src/emacs --fingerprint).pdmp" \
     >> nw-filelist

sed -i -e "s|\.%{native_lisp}|%{native_lisp}|" *-filelist *-dirlist

find %{buildroot}%{native_lisp}/ -name '*.eln' -type f -print0 \
    | xargs -0 chmod -x

find %{buildroot}%{native_lisp}/ -name '*.eln' -type f -print0 \
    | xargs -0 touch

export QA_SKIP_BUILD_ROOT=0

%check
appstreamcli validate --no-net %{buildroot}/%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
./build-nw/src/emacs --batch --no-init-file --eval '(kill-emacs (if (= (+ 1 2) 3) 0 1))'

%preun nw
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove emacs %{_bindir}/emacs-nw || :
fi

%posttrans nw
/usr/sbin/alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-nw 65 || :
if [ $1 = 2 -a ! -h %{_bindir}/emacs-nw ]; then
    ln -s emacs-%{version}-nw %{_bindir}/emacs-nw
fi

%preun common
/usr/sbin/alternatives --remove emacs.etags %{_bindir}/etags.emacs || :

%files

%files nw -f nw-filelist -f nw-dirlist
%ghost %{_bindir}/emacs
%{_bindir}/emacs-%{version}-nox
%{_bindir}/emacs-%{version}-nw
%{_bindir}/emacs-nox
%{_bindir}/emacs-nw

%files -n emacsclient
%license build-nw/etc/COPYING
%{_bindir}/emacsclient
%{_mandir}/man1/emacsclient.1*

%files common -f common-filelist
%config(noreplace) %{_sysconfdir}/skel/.emacs
%{_fileattrsdir}/emacs_lisp.attr
%{_rpmconfigdir}/emacs_lisp.rec
%{_rpmconfigdir}/macros.d/macros.emacs
%license build-nw/etc/COPYING
%doc build-nw/doc/NEWS build-nw/BUGS build-nw/README
%{_bindir}/ebrowse
%{_bindir}/etags
%{_datadir}/applications/emacs.desktop
%{_datadir}/applications/emacs-mail.desktop
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/emacs.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/apps/emacs.ico
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_infodir}/*
%{_mandir}/man1/ebrowse.1*
%{_mandir}/man1/emacs.1*
%{_mandir}/man1/etags.1*
%dir %{_datadir}/emacs/%{version}
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/site-lisp
%dir %{_libdir}/%{name}/%{version}
%dir %{native_lisp}
%dir %{_libexecdir}/emacs
%dir %{_libexecdir}/emacs/%{version}
%dir %{emacs_libexecdir}
%{emacs_libexecdir}/movemail
%{emacs_libexecdir}/hexl
%{emacs_libexecdir}/rcs2log
%{_userunitdir}/emacs.service
%attr(0644,root,root) %config(noreplace) %{site_lisp}/default.el
%attr(0644,root,root) %config %{site_lisp}/site-start.el
%{pkgconfig}/emacs.pc

%files devel
%{_includedir}/emacs-module.h

%changelog
%autochangelog
