%global source0_hash 7a82fe44a2658d7ccc57f51a69954719473f066bf9148396b9f49b86593b56f5

Name:           perl-Regexp-Stringify
Version:        0.06
Release:        24%{?dist}
Summary:        Stringify a Regexp object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-Stringify
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Regexp-Stringify-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(re)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98

%description
This module is an alternative to Perl's default stringification of Regexp
object and has some features/options, e.g. producing regexp string that is
compatible with certain perl versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Regexp-Stringify-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
