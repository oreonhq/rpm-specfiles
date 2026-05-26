# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8386a35a4d2d3cbc28fdcc93c5be007c382c78e3ee079070139f0d822e013325
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: A collection of programs for manipulating patch files
Name: patchutils
Version: 0.4.5
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: http://cyberelk.net/tim/patchutils/
Source0: http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.xz
Obsoletes: interdiff <= 0.0.10
Provides: interdiff = 0.0.11
Requires: patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-generators
BuildRequires: xmlto
BuildRequires: automake
BuildRequires: autoconf

%description
This is a collection of programs that can manipulate patch files in
a variety of ways, such as interpolating between two pre-patches, 
combining two incremental patches, fixing line numbers in hand-edited 
patches, and simply listing the files modified by a patch.

%prep
%oreon_verify_sources
%autosetup -p1

%build
%configure
%make_build

%check
make check

%install
%make_install


%files
%{!?_licensedir:%global license %doc}
%doc AUTHORS ChangeLog README.md BUGS NEWS
%license COPYING
%{_bindir}/*
%{_datadir}/bash-completion/completions/*
%{_mandir}/*/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.5-1
- Prepare for Oreon 11 (RP1)
