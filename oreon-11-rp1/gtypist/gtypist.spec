%global source0_hash ca618054e91f1ed5ef043fcc43500bbad701c959c31844d4688ff22849ac252d
Name:           gtypist
Version:        2.10.1
Release:        1%{?dist}
Summary:        GNU typing tutor
License:        GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
Url:            https://www.gnu.org/software/gtypist/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       fortune-mod
Requires:       emacs-filesystem >= %{_emacs_version}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
GNU Typist (or gtypist) is free software that assists you in learning
to type correctly.

It is intended to be used on a raw terminal without graphics. It has
been compiled and used in Unix (GNU/Linux, Aix, Solaris, openBSD) and
also in DOS/Windows (DOS 6.22, Windows 98, Windows XP).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-lispdir=%{_datadir}/emacs/site-lisp/gtypist
%make_build
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cat > %{buildroot}%{_emacs_sitestartdir}/gtypist-init.el <<EOF
(autoload 'gtypist-mode "gtypist-mode")
(setq auto-mode-alist (append '(("\\.typ$" . gtypist-mode)) auto-mode-alist))
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
