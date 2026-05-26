Name:		perl-ExtUtils-Config
Version:	0.010
Release:	4%{?dist}
Summary:	A wrapper for perl's configuration
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/ExtUtils-Config
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Config-0.010.tar.gz
# oreon url source checksums begin
%global source0_sha256 82e7e4e90cbe380e152f5de6e3e403746982d502dd30197a123652e46610c66d
%global source0_file ExtUtils-Config-0.010.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.6
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(ExtUtils::MakeMaker::Config)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
Requires:	perl(Data::Dumper)

%description
ExtUtils::Config is an abstraction around the %%Config hash.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ExtUtils-Config-0.010.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "82e7e4e90cbe380e152f5de6e3e403746982d502dd30197a123652e46610c66d" || { echo "oreon: Source0 SHA256 mismatch for ExtUtils-Config-0.010.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n ExtUtils-Config-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::Config.3*
%{_mandir}/man3/ExtUtils::Config::MakeMaker.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.010-4
- Import
