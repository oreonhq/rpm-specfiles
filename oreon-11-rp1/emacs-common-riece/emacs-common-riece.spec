%global source0_hash e2da635832a07c8a44bdc4ff57e6f427d270fad9a5c71423b8de5811f21ef5a6

%global pkg riece
%global pkgname Riece

Name:		emacs-common-%{pkg}
Version:	8.0.0
Release:	31%{?dist}
Summary:	Yet Another IRC Client for Emacs and XEmacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://riece.nongnu.org
Source0:	http://dl.sv.gnu.org/releases/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs-nox, texinfo-tex
%if 0%{?fedora} < 36
BuildRequires:	xemacs
%endif
BuildRequires:	make

%description
Riece is an IRC client for Emacs.

Riece provides the following features:

- Several IRC servers may be used at the same time.
- Essential features can be built upon the extension framework (called
  "add-on") capable of dependency tracking.
- Installation is easy.  Riece doesn't depend on other packages.
- Setup is easy.  Automatically save/restore the configuration.
- Riece uses separate windows to display users, channels, and
  dialogues.  The user can select the window layout.
- Step-by-step instructions (in info format) are included.
- Mostly compliant with RFC 2812.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}
%if 0%{?fedora} < 36
Obsoletes:	xemacs-%{pkg} < 8.0.0-20
%endif

%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run
%{pkgname} with GNU Emacs.

%if 0%{?fedora} < 36
%package -n xemacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under XEmacs
Requires:	xemacs(bin) >= %{_xemacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	xemacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	xemacs-%{pkg}-el < %{version}-%{release}

%description -n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use
%{pkgname} with XEmacs.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}-%{version}

%build
%configure
cat > %{name}-init.el <<"EOF"
(autoload 'riece "riece" "Start Riece" t)
EOF

%install
make -C doc install infodir=$RPM_BUILD_ROOT%{_infodir}
# don't package but instead update in pre and post
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# byte-compile & install elisp files with emacs
make -C lisp EMACS=emacs
make -C lisp install EMACS=emacs lispdir=$RPM_BUILD_ROOT%{_emacs_sitelispdir}
%__mkdir_p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{name}-init.el $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
make -C lisp clean

%if 0%{?fedora} < 36
# byte-compile & install elisp files with xemacs
%__mkdir_p $RPM_BUILD_ROOT%{_xemacs_sitepkgdir}/etc/%{pkg}
make -C lisp EMACS=xemacs
make -C lisp install EMACS=xemacs lispdir=$RPM_BUILD_ROOT%{_xemacs_sitelispdir}

# move data files installed in site-lisp, to sitepkgdir
mv $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/*.rb \
	$RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/*.xpm \
	$RPM_BUILD_ROOT%{_xemacs_sitepkgdir}/etc/%{pkg}/
%__mkdir_p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -m 644 %{name}-init.el $RPM_BUILD_ROOT%{_xemacs_sitestartdir}/%{pkg}-init.el
%endif

%files
%doc README README.ja NEWS NEWS.ja AUTHORS COPYING
%doc %{_infodir}/*.gz

%files -n emacs-riece
%{_emacs_sitelispdir}/riece/*.elc
%{_emacs_sitelispdir}/riece/*.el
%{_emacs_sitelispdir}/riece/*.xpm
%{_emacs_sitelispdir}/riece/*.rb
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/riece

%if 0%{?fedora} < 36
%files -n xemacs-riece
%{_xemacs_sitelispdir}/riece/*.elc
%{_xemacs_sitelispdir}/riece/*.el
%{_xemacs_sitepkgdir}/etc/riece/*.rb
%{_xemacs_sitepkgdir}/etc/riece/*.xpm
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/riece
%endif

%changelog
%autochangelog
