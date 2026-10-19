%global source0_hash 3bf68bb212298fa699a52749dddff35583a74f36a92ca89c843b854f29d87c77
Summary:        Various ancient mail-related perl modules
Name:		perl-MailTools
Version:	2.22
Release:        4%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MailTools
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Net::Domain) >= 1.05
Requires:	perl(Net::NNTP)
Provides:       perl(Mail::Address)
Provides:       perl(Mail::Send)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(Net::NNTP)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Net::SMTP::SSL)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
MailTools is a set of ancient Perl modules related to mail applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MailTools-%{version}

# Set up example scripts
cd examples
for file in *.PL; do
	perl $file
done
chmod -c -x *_demo
# Remove example-generation scripts, no longer needed
rm *.PL
cd -
sed -i -e '/^examples\/.*\.PL/d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
make test TEST_FILES="xt/*.t"
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.22-4
- Prepare for Oreon 11 (RP1)
