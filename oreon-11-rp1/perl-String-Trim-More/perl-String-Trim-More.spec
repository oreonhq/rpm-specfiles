%global source0_hash 739cfbd73e0a92897c6f31f0ad8d72a56302f8805e9707d4edca5e5086c14e7f

Name:           perl-String-Trim-More
Version:        0.03
Release:        20%{?dist}
Summary:        Various string trimming utilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/String-Trim-More
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/String-Trim-More-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)

%description
This is an alternative to String::Trim. Instead of a single trim function, this
module provides several from which you can choose on, depending on your needs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n String-Trim-More-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::Trim::More*.*

%changelog
%autochangelog
