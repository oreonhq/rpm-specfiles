%global source0_hash 88928dc21df3f3b15158e64b77268882544e6afa1d93f3545435ce430837fd2d
%global pkg riece
%global pkgname Riece
Name:		emacs-common-%{pkg}
Version:	9.0.0
Release:        1%{?dist}
Summary:        Yet Another IRC Client for Emacs and XEmacs
License:	GPL-2.0-or-later
URL:		http://riece.nongnu.org
Source0:        http://dl.sv.gnu.org/releases/%{pkg}/%{pkg}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  emacs-nox
BuildRequires:  make
BuildRequires:  texinfo-tex
# /oreon:deps
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
%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run
%{pkgname} with GNU Emacs.

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
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
make -C lisp EMACS=emacs
make -C lisp install EMACS=emacs lispdir=$RPM_BUILD_ROOT%{_emacs_sitelispdir}
%__mkdir_p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{name}-init.el $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
make -C lisp clean
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n emacs-riece -f %{oreon_filedir}/emacs-riece.list

%changelog

%autochangelog
