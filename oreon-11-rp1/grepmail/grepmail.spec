%global source0_hash d0984e3f7a1be17ae014575f70c1678151a5bcc9622185dc5a052cb63271a761

Summary:	Search mailboxes for a particular email
Name:		grepmail
Version:	5.3111
Release:	24%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/grepmail
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/grepmail-%{version}.tar.gz
Patch0:		grepmail-5.3111-Test-Compile.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode) >= 2.11
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Fcntl) >= 1.03
BuildRequires:	perl(File::HomeDir::Unix)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(PerlIO::encoding)
BuildRequires:	perl(PerlIO::utf8_strict)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Getopt::Std)
BuildRequires:	perl(Mail::Mbox::MessageParser) >= 1.4001
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Time::Local) >= 1.23
# Test Suite
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More) >= 0.62
BuildRequires:	perl(UNIVERSAL::require)
# Optional Tests
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Dependencies
Requires:	perl(Date::Manip)
Requires:	perl(Date::Parse)
Requires:	perl(Digest::MD5)
Requires:	perl(File::Find)
Requires:	perl(Mail::Mbox::MessageParser) >= 1.4001
Requires:	perl(Time::Local)

%description
Grepmail searches a normal or compressed mailbox for a given regular
expression, and returns those emails that match it. Piped input is allowed,
and date and size restrictions are supported, as are searches using logical
operators.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# Workaround for Test::Compile ≥ 2.0.0
%patch -P 0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
export TZ=GMT0
make test

%files
%license LICENSE
%doc CHANGES README TODO
%{_bindir}/grepmail
%{_mandir}/man1/grepmail.1*

%changelog
%autochangelog
