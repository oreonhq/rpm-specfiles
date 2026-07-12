%global source0_hash d28e88516ce9b5295c31631dcccdc0fc8f2ab7d8a5cc876bb1b20131087b01db

Name:           perl-Mixin-Linewise
Version:        0.111
Release:        9%{?dist}
Summary:        Write your linewise code for handles; this does the rest
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mixin-Linewise
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mixin-Linewise-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter) >= 0.9
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
# Runtime

Provides:       perl(Mixin::Linewise::Readers)
Provides:       perl(Mixin::Linewise::Writers)
%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With Mixin::Linewise::Readers and
Mixin::Linewise::Writers, you can just write a method to handle handles,
and methods for handling strings and file names are added for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mixin-Linewise-%{version}

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
%{perl_vendorlib}/Mixin/
%{_mandir}/man3/Mixin::Linewise.3*
%{_mandir}/man3/Mixin::Linewise::Readers.3*
%{_mandir}/man3/Mixin::Linewise::Writers.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.111-9
- Import
