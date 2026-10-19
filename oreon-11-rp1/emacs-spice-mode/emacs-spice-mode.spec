%global source0_hash 39917463131d5310bbfac414c5fa84d8e63a05488abc280b00eae9fe541262fd
%global pkg spice-mode
%global pkgname Emacs-spice-mode
%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 21.1
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif
Name:		emacs-%{pkg}
Version:	1.2.25
Release:        1%{?dist}
Summary:        SPICE Mode for GNU Emacs
License:	GPL-2.0-or-later
URL:		http://spice-mode.4t.com/
Source0:        http://spice-mode.4t.com/spice-mode-1.2.25.tar.gz
Source1:	%{pkg}-init.el
Patch0:		emacs-spice-mode-fix.patch
BuildArch:	noarch
Requires:	emacs >= %{emacs_version} gnucap
Provides:	%{name}-el = %{version}-%{release}
Obsoletes:	%{name}-el < 1.2.25-33
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-el
# /oreon:deps
%description
This package provides an Emacs major mode for editing SPICE decks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}
%patch -P0 -p2

%build

emacs -batch -f batch-byte-compile %{pkg}.el
%install
install -pm 755 -d %{buildroot}%{emacs_lispdir}/%{pkg}/
install -pm 755 -d %{buildroot}%{emacs_startdir}	
install -pm 644 %{pkg}.* %{buildroot}%{emacs_lispdir}/%{pkg}/
install -pm 644 %{SOURCE1} %{buildroot}%{emacs_startdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
