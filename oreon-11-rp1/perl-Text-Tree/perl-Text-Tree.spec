%global source0_hash d03ee54ddc224d5967689ab29979e518933de0278f7a52e8ab6084da424c1246

Name:           perl-Text-Tree
Version:        1.0
Release:        50%{?dist}
Summary:        Format a simple tree of strings into a textual tree graph
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Tree
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISAACSON/Text-Tree-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)

%description
Allows the caller to develop a tree structure, using nested arrays of
strings and references. Once developed, the whole tree can be printed as a
diagram, with the root of the tree at the top, and child nodes formatted
horizontally below them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Tree-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
