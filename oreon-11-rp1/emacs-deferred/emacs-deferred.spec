%global source0_hash 941b49635cc80ff62c5f568f393b4262c8848b4d27bc88ae8da36549f072e168

%global pkg deferred

Name:           emacs-%{pkg}
Version:        0.5.1
Release:        14%{?dist}
Summary:        Simple asynchronous functions for Emacs Lisp

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
deferred.el provides facilities to manage asynchronous tasks.

concurrent.el is a higher level library for asynchronous tasks, based on
deferred.el.
It is inspired by libraries of other environments and concurrent programming
models. It has following facilities: pseud-thread, generator, semaphore,
dataflow variables and event management.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
for i in *.el; do
    %{_emacs_bytecompile} $i
done

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

%files
%doc README.markdown README-concurrent.markdown
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
