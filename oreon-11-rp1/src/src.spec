%global source0_hash 59affec59aabd470b65f107b5ff98ca8eab220b500c5c6937173e216e4de41bd

Name:           src
Version:        1.38
Release:        5%{?dist}
Summary:        Simple Revision Control

License:        BSD-2-Clause
URL:            https://gitlab.com/esr/src
Source0:        https://gitlab.com/esr/src/-/archive/%{version}/%{name}-%{version}.tar.bz2
    
BuildRequires:  rubygem-asciidoctor
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rcs

Requires:       rcs
Requires:       python3
Recommends:     git-core

BuildArch:      noarch

%description
Simple Revision Control is RCS reloaded with a modern UI, designed to
manage single-file solo projects kept more than one to a directory.
Has a modern, svn/hg/git-like UI

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%py3_shebang_fix src

%build
%make_build all FAQ.html

%install
%make_install prefix=%{_prefix}

%files
%license COPYING
%doc FAQ.html
%{_bindir}/src
%{_mandir}/man1/src.1*

%changelog
%autochangelog
