%global source0_hash e05f8e45d0895164b1fe53a0a8e725dd81e92191a29409e1b48c55f823b03483

Summary:	Modules for parsing and creating MIME entities in Perl
Name:		perl-MIME-tools
Version:	5.517
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MIME-tools
Source0:	https://cpan.metacpan.org/modules/by-module/MIME/MIME-tools-%{version}.tar.gz
Patch0:		MIME-tools-5.510-UTF8.patch
BuildArch:	noarch
# ================ Module Build ======================
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Pod::Man)
BuildRequires:	sed
# ================ Module Runtime ====================
BuildRequires:	perl-MailTools		>= 1.50
BuildRequires:	perl(Carp)
BuildRequires:	perl(Convert::BinHex)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Path)	>= 1
BuildRequires:	perl(File::Spec)	>= 0.6
BuildRequires:	perl(File::Temp)	>= 0.18
BuildRequires:	perl(IO::File)		>= 1.13
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(Mail::Field)	>= 1.05
BuildRequires:	perl(Mail::Header)	>= 1.06
BuildRequires:	perl(Mail::Internet)	>= 1.28
BuildRequires:	perl(MIME::Base64)	>= 3.03
BuildRequires:	perl(MIME::QuotedPrint)
BuildRequires:	perl(version)
# ================ Test Suite ========================
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# ================ Dependencies ======================
Requires:	perl(Convert::BinHex)

# Currently fails a couple of kwalitee tests
BuildConflicts:	perl(Test::Kwalitee)

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

# Put the more useful examples in %%{_bindir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
cd useful-examples
for ex in mime*
do
	install -p -m 755 ${ex} %{buildroot}%{_bindir}/
	pod2man ${ex} > %{buildroot}%{_mandir}/man1/${ex}.1
done
cd -

%check
# POD Coverage test fails due to lots of undocumented routines
TEST_POD_COVERAGE=0 make test

%files
%license COPYING
%doc README ChangeLog
# Adding examples introduces additional deps, but these are all satisfied by
# perl, perl-MIME-tools, and perl-MailTools, which are all deps anyway.
%doc examples/
%{perl_vendorlib}/MIME/
%{_bindir}/mimedump
%{_bindir}/mimeencode
%{_bindir}/mimeexplode
%{_bindir}/mimepostcard
%{_bindir}/mimesend
%{_mandir}/man1/mimedump.1*
%{_mandir}/man1/mimeencode.1*
%{_mandir}/man1/mimeexplode.1*
%{_mandir}/man1/mimepostcard.1*
%{_mandir}/man1/mimesend.1*
%{_mandir}/man3/MIME::Body.3*
%{_mandir}/man3/MIME::Decoder.3*
%{_mandir}/man3/MIME::Decoder::Base64.3*
%{_mandir}/man3/MIME::Decoder::BinHex.3*
%{_mandir}/man3/MIME::Decoder::Binary.3*
%{_mandir}/man3/MIME::Decoder::Gzip64.3*
%{_mandir}/man3/MIME::Decoder::NBit.3*
%{_mandir}/man3/MIME::Decoder::QuotedPrint.3*
%{_mandir}/man3/MIME::Decoder::UU.3*
%{_mandir}/man3/MIME::Entity.3*
%{_mandir}/man3/MIME::Field::ConTraEnc.3*
%{_mandir}/man3/MIME::Field::ContDisp.3*
%{_mandir}/man3/MIME::Field::ContType.3*
%{_mandir}/man3/MIME::Field::ParamVal.3*
%{_mandir}/man3/MIME::Head.3*
%{_mandir}/man3/MIME::Parser.3*
%{_mandir}/man3/MIME::Parser::Filer.3*
%{_mandir}/man3/MIME::Parser::Reader.3*
%{_mandir}/man3/MIME::Parser::Results.3*
%{_mandir}/man3/MIME::Tools.3*
%{_mandir}/man3/MIME::WordDecoder.3*
%{_mandir}/man3/MIME::Words.3*

%changelog
%autochangelog
