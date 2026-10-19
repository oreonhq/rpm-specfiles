%global source0_hash 941b49635cc80ff62c5f568f393b4262c8848b4d27bc88ae8da36549f072e168
%global pkg deferred
Name:           emacs-%{pkg}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Simple asynchronous functions for Emacs Lisp
License:        GPL-3.0-or-later
URL:            https://github.com/kiwanami/%{name}/
Source0:        https://github.com/kiwanami/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
# /oreon:deps
%description
deferred.el provides facilities to manage asynchronous tasks.

concurrent.el is a higher level library for asynchronous tasks, based on
deferred.el.
It is inspired by libraries of other environments and concurrent programming
models. It has following facilities: pseud-thread, generator, semaphore,
dataflow variables and event management.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

for i in *.el; do
    %{_emacs_bytecompile} $i
done
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
