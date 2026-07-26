%global source0_hash b66ff756db8c8479ab99d2c9ec9827bf624b8bca2e96ef9ccf2395e279731662

Name:			Rex
Version:		1.16.1
Release:		3%{?dist}
Summary:		The friendly automation framework on basis of Perl

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:		Apache-2.0
URL:			https://www.rexify.org/
Source0:		https://cpan.metacpan.org/authors/id/F/FE/FERKI/%{name}-%{version}.tar.gz

BuildArch:		noarch

Requires:		perl(Data::Validate::IP)
Requires:		perl(Net::SSH2)
Requires:		perl(Net::OpenSSH)
Requires:		perl(Net::SFTP::Foreign)
Requires:		perl(Parallel::ForkManager)

BuildRequires:  git make rsync

BuildRequires:	perl-generators perl-interpreter
BuildRequires:	perl(AWS::Signature4)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Data::Validate::IP)
BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl(Digest::HMAC_SHA1)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Unix)
BuildRequires:	perl(File::Spec::Win32)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(Hash::Merge)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(JSON::MaybeXS)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Module::Load::Conditional)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(Net::OpenSSH::ShellQuoter)
BuildRequires:	perl(Net::SFTP::Foreign)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Parallel::ForkManager)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sort::Naturally)
BuildRequires:	perl(Storable)
BuildRequires:	perl(String::Escape)
BuildRequires:	perl(Sub::Override)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::UseAllModules)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(Test::mysqld)
BuildRequires:	perl(Text::Glob)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(UNIVERSAL)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::QueryParam)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(YAML)
BuildRequires:	perl(attributes)
BuildRequires:	perl(autodie)
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(if)
BuildRequires:	perl(lib)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)

%description
(R)?ex(ify) is the friendly automation framework on basis of the Perl scripting
language. You can use it in your everyday DevOps life for:

	* Continous Delivery
	* Configuration Management
	* Automation
	* Cloud Deployment
	* Virtualization
	* Software Rollout
	* Server Provisioning

It's friendly to any combinations of local and remote execution, push and pull
style of management, or imperative and declarative approach. Instead of forcing
any specific model on you, it trusts you to be in the best position to decide
what to automate and how, allowing you to build the automation tool your
situation requires.

Rex runs locally, even if managing remotes via SSH. This means it's instantly
usable, without big rollout processes or anyone else to convince, making it
ideal and friendly for incremental automation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%check
make test

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

sed -i "s|/usr/bin/env perl|/usr/bin/perl|" $RPM_BUILD_ROOT/%{_bindir}/rex

%{_fixperms} -c $RPM_BUILD_ROOT

%files
%doc ChangeLog CONTRIBUTORS README
%license LICENSE
%{_mandir}/man1/rex.1*
%{_mandir}/man1/rexify.1*
%{_mandir}/man3/%{name}*
%attr(644, root, root) %{perl_vendorlib}/%{name}.pm
%attr(644, root, root) %{perl_vendorlib}/auto/share/dist/%{name}/
%{perl_vendorlib}/%{name}/
%attr(755, root, root) %{_bindir}/rex
%attr(755, root, root) %{_bindir}/rexify

%changelog
%autochangelog
