%global source0_hash 21262218bddc89a564a9d98ddcd33711691523827195b79cb5a35fc4ff68a312

%global	pkg		w3m
%global	pkgname		Emacs-w3m
%global ver		1.4.632
%global	snap		e3b87d61

Name:			emacs-common-%{pkg}
Version:		%{ver}~0.%{snap}
Release:		7%{?dist}
Summary:		W3m interface for Emacsen

# GPLv3+ bookmark-w3m.el
License:		GPL-2.0-or-later AND GPL-3.0-or-later
URL:			http://emacs-w3m.namazu.org/
## No real archives available since this version is a snapshot from CVS.
#Source0:		http://emacs-w3m.namazu.org/emacs-w3m-%%{version}.tar.gz
#
# How to generate tarball:
# 1. cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot login
# 2. CVS password:[enter]
# 3. cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot co emacs-w3m
# 4. cd emacs-w3m
# 5. autoconf
# 6. make dist
Source0:		emacs-w3m-%{ver}.tar.gz
Source1:		w3m-init.el

BuildArch:		noarch
BuildRequires:		texinfo texinfo-tex
BuildRequires:		emacs emacs-apel flim
%if 0%{?fedora} < 36
BuildRequires:		xemacs xemacs-packages-extra flim-xemacs
%endif
BuildRequires:		make
Requires:		w3m
Provides:		w3m-el-common = %{version}-%{release}
Obsoletes:		w3m-el-common < 1.4.398
%if 0%{?fedora} >= 36
Obsoletes:		xemacs-%{pkg} < 1.4.631-0.9.20180618cvs
%endif

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

%if 0%{?fedora} < 36
%package		-n xemacs-%{pkg}
Summary:		Compiled elisp files to run %{pkgname} Under XEmacs
Requires:		xemacs(bin) >= %{_xemacs_version}
Requires:		emacs-common-%{pkg} = %{version}-%{release}
Requires:		xemacs-packages-extra flim-xemacs
Provides:		w3m-el-xemacs = %{version}-%{release}
Obsoletes:		w3m-el-xemacs < 1.4.398
Provides:		xemacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs
Obsoletes:		xemacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs

%description		-n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use %{pkgname} with
XEmacs.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n emacs-w3m-%{ver}

%build

%install
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
%if 0%{?fedora} < 36
install -d $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
%endif

#
# for Emacs
#
%configure --with-icondir=\$\(prefix\)/share/pixmaps/emacs-%{pkg}
make %{?_smp_mflags}
make install prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} infodir=$RPM_BUILD_ROOT%{_infodir} INSTALL="/usr/bin/install -p"
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}
make install-icons prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} INSTALL="/usr/bin/install -p"

%if 0%{?fedora} < 36
make distclean

#
# for XEmacs
#
%configure --with-xemacs --with-icondir=\$\(datadir\)/pixmaps/emacs-%{pkg}
make %{?_smp_mflags}
make install-package prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} INSTALL="/usr/bin/install -p"
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
%endif

## remove unpackaged files.
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/{ChangeLog,ChangeLog.1,sChangeLog}
%if 0%{?fedora} < 36
rm -rf $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/../{etc,info}
rm -rf $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/{ChangeLog,ChangeLog.1,sChangeLog}
%endif

%files
%doc ChangeLog ChangeLog.1 README
%lang(ja) %doc README.ja
%license COPYING
%{_datadir}/pixmaps/emacs-%{pkg}
%{_infodir}/emacs-w3m*

%files	-n emacs-%{pkg}
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.el.gz
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}

%if 0%{?fedora} < 36
%files	-n xemacs-%{pkg}
%{_xemacs_sitelispdir}/%{pkg}/*.el
%{_xemacs_sitelispdir}/%{pkg}/*.el.gz
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%endif

%changelog
%autochangelog
