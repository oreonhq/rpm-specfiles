%global source0_hash 0645042e42295c978fff5c73828dd030d565de2d4daae87f0ed788aade699fdc

%global debug_package %{nil}
Name:           git-remote-hg
Version:        1.0.4
Release:        7%{?dist}
BuildArch:      noarch
Summary:        Mercurial wrapper for git
License:        GPL-2.0-or-later
URL:            https://github.com/mnauw/git-remote-hg
Source0:        https://github.com/mnauw/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc >= 8.4.1
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  mercurial >= 5.4
Requires:       python3
Requires:       git-core >= 2.0.0
Requires:       mercurial >= 5.4

%description
git-remote-hg is the semi-official Mercurial bridge from Git project.
Once installed, it allows you to clone, fetch and push to and from Mercurial
repositories as if they were Git ones.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e "1 s|^#!.*|#!%{__python3}|" git-remote-hg
sed -i -e 's|\tinstall|\tinstall -p|' Makefile

%build
make doc

%check
#make test

%install
export HOME=%{_prefix}
export DESTDIR=%{buildroot}
export PYTHON=%{python3}
make install
make install-doc

%files
%doc LICENSE
%{_bindir}/git-remote-hg
%{_bindir}/git-hg-helper
%{_mandir}/man1/*

%changelog
%autochangelog
