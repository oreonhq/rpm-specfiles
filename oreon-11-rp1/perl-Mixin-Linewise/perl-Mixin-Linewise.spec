%global source0_hash d28e88516ce9b5295c31631dcccdc0fc8f2ab7d8a5cc876bb1b20131087b01db
Name:           perl-Mixin-Linewise
Version:        0.111
Release:        9%{?dist}
Summary:        Write your linewise code for handles; this does the rest
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mixin-Linewise
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mixin-Linewise-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Mixin::Linewise::Readers)
Provides:       perl(Mixin::Linewise::Writers)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.111-9
- Import
