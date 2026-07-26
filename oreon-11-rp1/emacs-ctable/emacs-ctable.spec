%global source0_hash 08da7bb579ef4c37cf972fd5cd9a5a990ed7220abe55fcfa0e27078c77c079d3

%global pkg ctable

Name:           emacs-%{pkg}
Version:        0.1.2
Release:        15%{?dist}
Summary:        Table Component for Emacs Lisp

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
ctable.el is a table component for Emacs Lisp. Emacs lisp programs can display a
nice table view from an abstract data model. The many emacs programs have the
code for displaying table views, such as dired, list-process, buffer-list and so
on. So, ctable.el would provide functions and a table framework for the table
views.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

%check
emacs --batch -q --no-site-file --no-splash \
    -l $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/%{pkg}.el \
    -l test-ctable.el \
    -f ctbl:test-all

%files
%doc readme.md
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
