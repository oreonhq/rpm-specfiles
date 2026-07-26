%global source0_hash f6e7fd0b68aed292e85bb686616baf6551d5c9424adcddca11d808ba318cb320

Name:           global
Version:        6.6.14
Release:        1%{?dist}
Summary:        Source code tag system
# The entire source code is GPL-3.0-or-later except:
# LGPL-2.0-or-later
#   libglibc/fnmatch.{c,h}
#   libglibc/regex.{c,h}
#   libglibc/snprintf.c
#   libltdl/*.{c,h}
# LGPL-2.1-or-later
#   libglibc/getopt{.c,1.c,.h,_int.h}
#   libglibc/hash-string.{c,h}
#   libglibc/obstack.{c,h}
# BSD-3-Clause
#   gtags-cscope/*.{c,h}
#   libdb/bt_*.c
#   libdb/{db,mpool}.{c,h}
#   libdb/{btree,compat,extern,queue}.h
# MIT
#   htags/jquery
# LicenseRef-Fedora-Public-Domain
#   htags/icons/
#   htags-refkit/htags_path2url.c
#   plugin-factory/uctags-scheme.c
# blessing
#   libdb/sqlite3.{c,h}
# GFDL-1.2-or-later
#   doc/global.{info,texi}
License:        GPL-3.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause and MIT and LicenseRef-Fedora-Public-Domain and blessing and GFDL-1.2-or-later
URL:            https://www.gnu.org/software/global
Source:         https://ftp.gnu.org/pub/gnu/global/global-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  python3-devel
BuildRequires:  emacs
%if 0%{?fedora} < 36
BuildRequires:  xemacs
%endif
BuildRequires:  sqlite-devel
BuildRequires:  make
Requires:       emacs-filesystem >= %{_emacs_version}
%if 0%{?fedora} < 36
Requires:       xemacs-filesystem >= %{_xemacs_version}
%endif
Obsoletes:      emacs-global <= 6.5.1-1
Obsoletes:      emacs-global-el <= 6.5.1-1
Provides:       emacs-global = %{version}-%{release}
Provides:       emacs-global-el = %{version}-%{release}

Patch0100:      libdb-dbpanic-function-pointers.patch

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

%package        ctags
Summary:        Integration of Universal Ctags and Pygments with GLOBAL
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}, python3-pygments

%description    ctags
This package contains plug-ins that provides support for more languages
through Pygments and Universal Ctags.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
touch -r configure.ac configure aclocal.m4 Makefile.in

%build
%configure --with-posix-sort=/usr/bin/sort --with-universal-ctags=/usr/bin/ctags \
           --localstatedir=/var/tmp/ --without-included-ltdl --with-sqlite3 \
           --with-python-interpreter=%{python3} --disable-static
%make_build

%install
%make_install

# Remove empty useless directory
rm -f %{buildroot}%{_infodir}/dir

rm -f %{buildroot}%{_libdir}/gtags/*.*a
rm -f %{buildroot}%{_libdir}/gtags/user-custom.*

rm %{buildroot}/%{_datadir}/gtags/{gtags.el,gtags.conf}
rm %{buildroot}/%{_datadir}/gtags/{AUTHORS,COPYING,ChangeLog,DONORS,FAQ,INSTALL,LICENSE,NEWS,README,THANKS}

# fix rpmlint error
chmod +x %{buildroot}/%{_datadir}/gtags/{global,completion}.cgi

mkdir -p %{buildroot}%{_sysconfdir}
install gtags.conf -t %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_emacs_sitelispdir}
install gtags.el -p -t %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/gtags.el
chmod -x %{buildroot}%{_emacs_sitelispdir}/gtags.el
%if 0%{?fedora} < 36
mkdir -p %{buildroot}%{_xemacs_sitelispdir}
install gtags.el -p -t %{buildroot}%{_xemacs_sitelispdir}
%{_xemacs_bytecompile} %{buildroot}%{_xemacs_sitelispdir}/gtags.el
chmod -x %{buildroot}%{_xemacs_sitelispdir}/gtags.el
%endif

## Remove executable flag
chmod -x %{buildroot}/%{_sysconfdir}/gtags.conf

%files
%doc README THANKS AUTHORS FAQ NEWS
%doc DONORS ChangeLog
%license LICENSE COPYING
%config(noreplace) %{_sysconfdir}/gtags.conf
%{_bindir}/*
%{_infodir}/global.info*
%{_mandir}/man*/*
%{_datadir}/gtags
%{_emacs_sitelispdir}/gtags.el*
%if 0%{?fedora} < 36
%{_xemacs_sitelispdir}/gtags.el*
%endif

%files ctags
%dir %{_libdir}/gtags
%{_libdir}/gtags/*

%changelog
%autochangelog
