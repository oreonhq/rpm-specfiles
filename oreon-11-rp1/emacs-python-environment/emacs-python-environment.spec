%global source0_hash 8855d036ee858b8cfebf02f003a042dc1c7f4b8b00bf4c103cb12668b7fa3146
%global pkg python-environment
Name:           emacs-%{pkg}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Python virtualenv API for Emacs Lisp
License:        GPL-3.0-or-later
URL:            https://github.com/tkf/%{name}/
Source0:        https://github.com/tkf/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-deferred
Requires:       virtualenv
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-deferred
# /oreon:deps
%description
Emacs integrates well with external tools written in languages other than Emacs
Lisp and thus use of these tools should be encouraged. However, many people try
to avoid using non-Emacs Lisp software tools since it makes installation of
their Emacs plugin hard. python-environment.el solves this problem (only for the
case the tool is written in Python) by providing virtualenv API in Emacs Lisp so
that you can automate installation of tools written in Python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
