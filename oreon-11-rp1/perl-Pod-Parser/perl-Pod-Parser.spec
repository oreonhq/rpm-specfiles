%global source0_hash 5deccbf55d750ce65588cd211c1a03fa1ef3aaa15d1ac2b8d85383a42c1427ea
%bcond_with perl_Pod_Parser_enables_optional_test
Name:           perl-Pod-Parser
Version:        1.67
Release:        1%{?dist}
Summary:        Basic perl modules for handling Plain Old Documentation (POD)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Parser
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Pod_Parser_enables_optional_test}
%endif
Requires:       perl(Config)
Provides:       perl(Pod::Parser)
Provides:       perl(Pod::Find)
Provides:       perl(Pod::ParseUtils)
Provides:       perl(Pod::PlainText)
Provides:       perl(Pod::Select)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This software distribution contains the packages for using Perl5 POD (Plain
Old Documentation). See the "perlpod" and "perlsyn" manual pages from your
Perl5 distribution for more information about POD.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Parser-%{version}
find -type f -exec chmod -x {} +
chmod +x scripts/*
for F in ANNOUNCE CHANGES README TODO; do
    tr -d '\r' < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.67-7
- Prepare for Oreon 11 (RP1)
