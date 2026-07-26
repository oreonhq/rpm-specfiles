%global source0_hash 5d9b034f58f0b6ff5b64647bd3c5a9ce05b2a70edee339fbc3173aee747cc050

Name:           perl-JavaScript-Minifier-XS
Version:        0.15
Release:        15%{?dist}
Summary:        XS based JavaScript minifier
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JavaScript-Minifier-XS
Source0:        https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/JavaScript-Minifier-XS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JavaScript::Minifier)
BuildRequires:  perl(Test::DiagINC)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
JavaScript::Minifier::XS is a JavaScript "minifier"; it's designed
to remove unnecessary white space and comments from JavaScript
files without breaking the JavaScript.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JavaScript-Minifier-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
export AUTOMATED_TESTING=1
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JavaScript*
%{_mandir}/man3/*

%changelog
%autochangelog
