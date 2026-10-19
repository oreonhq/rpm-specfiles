%global source0_hash 92b937636084dc910a3d04fac3e64d08df5444b34143ea903c8bd827fde8a8a6
%global srcname company-mode
%global giturl  https://github.com/company-mode/company-mode
Name:           emacs-%{srcname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Modular in-buffer completion framework for Emacs
License:        GPL-3.0-or-later
URL:            https://company-mode.github.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{srcname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
# oreon:deps
BuildRequires:  emacs-nw
# /oreon:deps
%description
Company is a text completion framework for Emacs.  The name stands for
"complete anything".  It uses pluggable back-ends and front-ends to retrieve
and display completion candidates.  It comes with several back-ends such as
Elisp, Clang, Semantic, Eclim, Ropemacs, Ispell, CMake, BBDB, Yasnippet,
dabbrev, etags, gtags, files, keywords and a few others.

The CAPF back-end provides a bridge to the standard
completion-at-point-functions facility, and thus works with any major mode
that defines a proper completion function.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/company-loaddefs.el\"))"
%_emacs_bytecompile *.el
%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{srcname}
install -p -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/%{srcname}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/%{srcname}/company-loaddefs.el \
  %{buildroot}%{_emacs_sitestartdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
