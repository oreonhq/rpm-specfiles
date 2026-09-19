%global source0_hash 78d5a2b384a7d4a2dd674b0c0b79dc55d46017ba2a21d35d8d4858a025d5ca6c

Name:           perl-Parse-ExuberantCTags
Version:        1.02
Release:        49%{?dist}
Summary:        Efficiently parse exuberant ctags files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-ExuberantCTags
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Parse-ExuberantCTags-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

# Filter autoloader libraries out
%{?perl_default_filter}

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

%check
make test

%files
%doc Changes perlobject.map README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Parse*
%{_mandir}/man3/*

%changelog
%autochangelog
