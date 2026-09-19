%global source0_hash 5723c0aa9cc10bab9ed1e3bfd9d5c95f7159e71c1a475414eb1af1dee3a46237

Summary:	A fast and simple mbox folder reader
Name:		perl-Mail-Mbox-MessageParser
Version:	1.5111
Release:	23%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/Mail-Mbox-MessageParser
Source0:	https://cpan.metacpan.org/modules/by-module/Mail/Mail-Mbox-MessageParser-%{version}.tar.gz
Source1:	perl-module-version-filter
Patch0:		Mail-Mbox-MessageParser-1.5111-Test-Compile.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	grep, gzip, bzip2, lzip >= 1.3, xz, /usr/bin/diff
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode) >= 2.11
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(PerlIO::encoding)
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FileHandle::Unget)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Path) >= 2.08
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Dependencies
Requires:	grep, gzip, bzip2, lzip >= 1.3, xz, /usr/bin/diff
Requires:	perl(Storable)

%description
Mail::Mbox::MessageParser is a feature-poor but very fast mbox parser. It uses
the best of three strategies for parsing a mailbox: either using cached folder
information, GNU grep, or highly optimized Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Mbox-MessageParser-%{version}

# Workaround for Test::Compile ≥ 2.0.0
%patch -P 0 -p0

# Auto provides aren't clever enough for what Mail::Mbox::MessageParser does
%if 0%{?__perllib_provides:1}
%global provfilt /bin/sh -c "%{__perllib_provides} | perl -n -s %{SOURCE1} -lib=%{_builddir}/%{buildsubdir}/lib"
%global __perllib_provides %{provfilt}
%else
%global provfilt /bin/sh -c "%{__perl_provides} | perl -n -s %{SOURCE1} -lib=%{_builddir}/%{buildsubdir}/lib"
%global __perl_provides %{provfilt}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor \
	BZIP=/usr/bin/bzip2 \
	BZIP2=/usr/bin/bzip2 \
	CAT=/bin/cat \
	DIFF=/usr/bin/diff \
	GREP=/bin/grep \
	GZIP=/bin/gzip \
	LZIP=/usr/bin/lzip \
	XZ=/usr/bin/xz

make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc anonymize_mailbox CHANGES README TODO
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Mbox::MessageParser.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Cache.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Config.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Grep.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::MetaInfo.3*
%{_mandir}/man3/Mail::Mbox::MessageParser::Perl.3*

%changelog
%autochangelog
