%global source0_hash 3031b25a15c18f157bb4a5185fdbdee38c6401eaee3ddc1594040b215989e895
%global pkg with-editor
%global pkgname With-Editor
Name:           emacs-%{pkg}
Version:        3.5.4
Release:        1%{?dist}
Summary:        Use Emacsclient as the editor of child processes
License:        GPL-3.0-or-later
URL:            https://github.com/magit/with-editor
Source0:        https://github.com/magit/%{pkg}/archive/v%{version}/%{pkg}-%{version}.tar.gz
BuildArch:      noarch
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash >= 2.13
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
%{pkgname} makes it possible to reliably use the Emacsclient as the editor
of child processes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%make_build
%install
install -D -p -m 644 docs/%{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  lisp/%{pkg}-autoloads.el lisp/%{pkg}.el lisp/%{pkg}.elc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
