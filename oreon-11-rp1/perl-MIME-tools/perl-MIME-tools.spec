%global source0_hash e05f8e45d0895164b1fe53a0a8e725dd81e92191a29409e1b48c55f823b03483
Summary:        Modules for parsing and creating MIME entities in Perl
Name:		perl-MIME-tools
Version:	5.517
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MIME-tools
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/MIME-tools-%{version}.tar.gz
Patch0:		MIME-tools-5.510-UTF8.patch
BuildArch:	noarch
Requires:	perl(Convert::BinHex)
BuildConflicts:	perl(Test::Kwalitee)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::BinHex)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Mail::Field)
BuildRequires:  perl(Mail::Header)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(version)
BuildRequires:  perl-MailTools
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
MIME-tools - modules for parsing (and creating!) MIME entities. Modules in this
toolkit: Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MIME-tools-%{version}

# Remove bundled dependencies
rm -rv inc/
sed -i -e '/^inc\// d' MANIFEST

# Fix character encoding
%patch -P 0

# The more useful examples will go in %%{_bindir}
mkdir useful-examples
mv examples/mime{dump,encode,explode,postcard,send} useful-examples/

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
cd useful-examples
for ex in mime*
do
	install -p -m 755 ${ex} %{buildroot}%{_bindir}/
	pod2man ${ex} > %{buildroot}%{_mandir}/man1/${ex}.1
done
cd -
%oreon_autofiles main

%check

TEST_POD_COVERAGE=0 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
