%global source0_hash 78d5a2b384a7d4a2dd674b0c0b79dc55d46017ba2a21d35d8d4858a025d5ca6c
Name:           perl-Parse-ExuberantCTags
Version:        1.02
Release:        1%{?dist}
Summary:        Efficiently parse exuberant ctags files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-ExuberantCTags
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Parse-ExuberantCTags-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module parses ctags files and handles both traditional ctags as
well as extended ctags files such as produced with Exuberant ctags. To the
best of my knowledge, it does not handle emacs-style "etags" files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-ExuberantCTags-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
