%global source0_hash fc59dd5b44890b584516b405f6b258e3da7804f351a03027086ed6bcc2ba6257

%global pkg with-editor
%global pkgname With-Editor

Name:           emacs-%{pkg}
Version:        3.4.8
Release:        %autorelease
Summary:        Use Emacsclient as the editor of child processes
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/magit/with-editor
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make texinfo texinfo-tex
BuildRequires:  emacs-dash >= 2.13
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash >= 2.13

%description
%{pkgname} makes it possible to reliably use the Emacsclient as the editor
of child processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build
%make_build

%install
# With-Editor doesn't provide an install target.
install -D -p -m 644 docs/%{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  lisp/%{pkg}-autoloads.el lisp/%{pkg}.el lisp/%{pkg}.elc

%files
%license LICENSE
%doc README.org
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*

%changelog
%autochangelog
