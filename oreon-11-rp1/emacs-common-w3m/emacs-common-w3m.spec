%global source0_hash 21262218bddc89a564a9d98ddcd33711691523827195b79cb5a35fc4ff68a312
%global	pkg		w3m
%global	pkgname		Emacs-w3m
%global ver		1.4.632
%global	snap		e3b87d61
Name:			emacs-common-%{pkg}
Version:		%{ver}~0.%{snap}
Release:        1%{?dist}
Summary:        W3m interface for Emacsen
License:		GPL-2.0-or-later AND GPL-3.0-or-later
URL:			http://emacs-w3m.namazu.org/
Source0:        emacs-%{pkg}-%{ver}.tar.gz
Source1:		w3m-init.el
BuildArch:		noarch
Requires:		w3m
Provides:		w3m-el-common = %{version}-%{release}
Obsoletes:		w3m-el-common < 1.4.398
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-apel
BuildRequires:  flim
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
W3m is a text based World Wide Web browser with IPv6 support. It
features excellent support for tables and frames. It can be used as a
standalone pager such as lv, less, and more.

This package contains the files common to both the GNU Emacs and XEmacs
%{pkgname} packages.

%package		-n emacs-%{pkg}
Summary:		Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:		emacs(bin) >= %{_emacs_version}
Requires:		emacs-common-%{pkg} = %{version}-%{release}
Requires:		emacs-apel flim
Provides:		w3m-el = %{version}-%{release}
Obsoletes:		w3m-el < 1.4.398
Provides:		emacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs
Obsoletes:		emacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs
%description		-n emacs-%{pkg}
This package contains the byte compiled elisp packages to run %{pkgname} with GNU
Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n emacs-w3m-%{ver}

%build

%install
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
%configure --with-icondir=\$\(prefix\)/share/pixmaps/emacs-%{pkg}
make %{?_smp_mflags}
make install prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} infodir=$RPM_BUILD_ROOT%{_infodir} INSTALL="/usr/bin/install -p"
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}
make install-icons prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} INSTALL="/usr/bin/install -p"
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/{ChangeLog,ChangeLog.1,sChangeLog}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n emacs-w3m -f %{oreon_filedir}/emacs-w3m.list

%changelog

%autochangelog
