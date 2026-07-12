%global source0_hash 5821cf0b40aa11913992c3b832201aa309a38cb99cab7fea357d6ed8d5ca211a

Name:           perl-ColorThemeRole-ANSI
Version:        0.001
Release:        16%{?dist}
Summary:        Roles for using ColorTheme::* with ANSI codes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ColorThemeRole-ANSI/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/ColorThemeRole-ANSI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(ColorThemeUtil::ANSI)
BuildRequires:  perl(Role::Tiny)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(ColorTheme::Test::Static)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98

Provides:       perl(ColorThemeRole::ANSI)
%description
This module can be mixed in with a ColorTheme::* class. Handy when using
color theme in terminal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ColorThemeRole-ANSI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
