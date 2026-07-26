%global source0_hash 0a24e9fb304c795976669c81f599390748f2c2fcd01c202d5c6ee7e4d4439f17

%global pkg emacs-goodies
%global pkgname Emacs-goodies
%global goodies_dir %{buildroot}%{_emacs_sitelispdir}/goodies/
%global gnus_dir %{buildroot}%{_emacs_sitelispdir}/gnus-bonus/

Name:       %{pkg}
Version:    41.0
Release:    20%{?dist}
Summary:    Miscellaneous add on for Emacs

# Automatically converted from old format: GPLv2+ and GPLv3 - review is highly recommended.
License:    GPL-2.0-or-later AND GPL-3.0-only
URL:        http://packages.debian.org/sid/lisp/emacs-goodies-el
Source0:    http://snapshot.debian.org/archive/debian/20180913T085742Z/pool/main/e/emacs-goodies-el/emacs-goodies-el_41.0.tar.xz
#Patch which adjusts debian specific information to fedora in texi file
#Patch is irrelevant to upstream as it is specific to Fedora
Patch0:     emacs-goodies-el.texi.patch

BuildArch:  noarch
BuildRequires:  emacs texinfo
Requires:   emacs(bin) >= %{_emacs_version}

Obsoletes:  %{name}-el < 41.0-15
Provides:   %{name}-el = %{version}-%{release}

%description
This is %{pkgname} %{version} which provides numerous add on for GNU Emacs
and Gnus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}-el-%{version}
%{__chmod} 644 COPYING-GPL-v3
%{__chmod} 644 COPYING-GPL-v2
%patch -P0 -p1

%build
%{__mkdir} -p elisp/%{pkg}-el/info
cd elisp/%{pkg}-el/
%{__chmod} +x %{pkg}-loaddefs.make
./%{pkg}-loaddefs.make
%{_emacs_bytecompile} *.el
makeinfo emacs-goodies-el.texi
iconv -f iso8859-1 -t utf-8 info/emacs-goodies > info/emacs-goodies.utf
%{__mv} info/emacs-goodies.utf info/emacs-goodies

%install
%{__rm} -rf %{buildroot}
%{__install} -pm 755 -d %{goodies_dir}
%{__install} -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
%{__install} -pm 644 elisp/%{pkg}-el/%{pkg}-loaddefs.el %{buildroot}%{_emacs_sitestartdir}
%{__install} -pm 644 elisp/%{pkg}-el/*.elc %{goodies_dir}
%{__install} -pm 644 elisp/%{pkg}-el/*.el %{goodies_dir}
%{__install} -pm 755 -d %{buildroot}%{_infodir}/
%{__install} -pm 644 elisp/%{pkg}-el/info/%{pkg} %{buildroot}%{_infodir}/

%files
%doc COPYING-GPL-v2 COPYING-GPL-v3
%{_emacs_sitelispdir}/goodies/*.el
%{_emacs_sitelispdir}/goodies/*.elc
%{_emacs_sitestartdir}/emacs-goodies-loaddefs.el
%{_infodir}/%{pkg}.gz
%dir %{_emacs_sitelispdir}/goodies

%changelog
%autochangelog
