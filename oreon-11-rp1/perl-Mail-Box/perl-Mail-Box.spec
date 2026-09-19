%global source0_hash ad66807dd830371278c7fc31f3df9048c16ce9d01430d5fb4414feae05f1fe0d

Name:           perl-Mail-Box
Version:        4.01
Release:        2%{?dist}
Summary:        Manage a mailbox, a folder with messages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::FcntlLock)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Remove) >= 0.20
BuildRequires:  perl(File::Spec) >= 0.7
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report) >= 1.42
BuildRequires:  perl(Mail::Box::Parser::Perl)
# Versions prior to 3.008 result in a failed test (prerequisite)
BuildRequires:  perl(Mail::Message) >= 4.00
BuildRequires:  perl(Mail::Message::Body)
BuildRequires:  perl(Mail::Message::Body::File)
BuildRequires:  perl(Mail::Message::Body::Lines)
BuildRequires:  perl(Mail::Message::Body::Multipart)
BuildRequires:  perl(Mail::Message::Body::String)
BuildRequires:  perl(Mail::Message::Construct)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Reporter)
BuildRequires:  perl(Mail::Transport) >= 4.00
BuildRequires:  perl(Object::Realize::Later) >= 4.00
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(User::Identity::Collection)
BuildRequires:  perl(User::Identity::Item)
BuildRequires:  perl(warnings)
BuildArch:      noarch
Requires:       perl(Mail::Message) >= 4.00
Requires:       perl(Object::Realize::Later) >= 4.00

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Message\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Object::Realize::Later\\)

%description
The Mail::Box folder is a modern mail-folder manager -- at least at
the moment of this writing ;)  It is written to replace Mail::Folder,
although its interface is different.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Box-%{version}

%build
yes y |%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Nuke Zero length files
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Overview.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Cookbook.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Index.pod

%check
make test

%files
%doc README.md README.todo ChangeLog examples/
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Box*.3*
%{_mandir}/man3/Mail::Message*.3*
%{_mandir}/man3/Mail::Server*.3*

%changelog
%autochangelog
