%global source0_hash d0984e3f7a1be17ae014575f70c1678151a5bcc9622185dc5a052cb63271a761
Summary:        Search mailboxes for a particular email
Name:		grepmail
Version:	5.3111
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		https://metacpan.org/release/grepmail
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/grepmail-%{version}.tar.gz
Patch0:		grepmail-5.3111-Test-Compile.patch
BuildArch:	noarch
Requires:	perl(Date::Manip)
Requires:	perl(Date::Parse)
Requires:	perl(Digest::MD5)
Requires:	perl(File::Find)
Requires:	perl(Mail::Mbox::MessageParser) >= 1.4001
Requires:	perl(Time::Local)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir::Unix)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Mail::Mbox::MessageParser)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

export TZ=GMT0
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
