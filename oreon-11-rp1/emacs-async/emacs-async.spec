%global source0_hash eaf88ce8428044c9c7499f9fb3a5f4830bffcad2f95b4a7b51dd7778c05d904f
%global pkg async
Name:           emacs-%{pkg}
Version:        1.9.9
Release:        1%{?dist}
Summary:        Asynchronous processing in Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/jwiegley/emacs-async
Source0:        https://github.com/jwiegley/%{name}/archive/v%{version}/%{pkg}-%{version}.tar.gz
BuildArch:      noarch
Requires:       emacs(bin)%{?_emacs_version: >= %{_emacs_version}}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  make
# /oreon:deps
%description
%{name} is a module for doing asynchronous processing in Emacs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/%{pkg}
make DESTDIR=%{buildroot}/%{_emacs_sitelispdir}/%{pkg} install
%oreon_autofiles main

%check

emacs --batch -L . -l async-test.el -f async-test-1 -f async-test-2 \
      -f async-test-3 -f async-test-4 -f async-test-5 -f async-test-6
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
