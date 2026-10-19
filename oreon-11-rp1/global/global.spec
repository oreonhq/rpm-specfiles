%global source0_hash fdab590c9bda2d68d55e99c51c7e60c2c8595ae4dcebab9bbbb0795f2a5c8bf7
Name:           global
Version:        6.7
Release:        1%{?dist}
Summary:        Source code tag system
License:        GPL-3.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause and MIT and LicenseRef-Fedora-Public-Domain and blessing and GFDL-1.2-or-later
URL:            https://www.gnu.org/software/global
Source0:        https://ftp.gnu.org/pub/gnu/global/global-%{version}.tar.gz
Requires:       emacs-filesystem >= %{_emacs_version}
Obsoletes:      emacs-global <= 6.5.1-1
Obsoletes:      emacs-global-el <= 6.5.1-1
Provides:       emacs-global = %{version}-%{release}
Provides:       emacs-global-el = %{version}-%{release}
Patch0100:      libdb-dbpanic-function-pointers.patch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
# /oreon:deps
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
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/gtags/*.*a
rm -f %{buildroot}%{_libdir}/gtags/user-custom.*
rm %{buildroot}/%{_datadir}/gtags/{gtags.el,gtags.conf}
rm %{buildroot}/%{_datadir}/gtags/{AUTHORS,COPYING,ChangeLog,DONORS,FAQ,INSTALL,LICENSE,NEWS,README,THANKS}
chmod +x %{buildroot}/%{_datadir}/gtags/{global,completion}.cgi
mkdir -p %{buildroot}%{_sysconfdir}
install gtags.conf -t %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}
install gtags.el -p -t %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/gtags.el
chmod -x %{buildroot}%{_emacs_sitelispdir}/gtags.el
chmod -x %{buildroot}/%{_sysconfdir}/gtags.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n global-ctags -f %{oreon_filedir}/global-ctags.list

%changelog

%autochangelog
