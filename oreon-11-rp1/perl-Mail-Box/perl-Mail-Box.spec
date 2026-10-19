%global source0_hash ad66807dd830371278c7fc31f3df9048c16ce9d01430d5fb4414feae05f1fe0d
Name:           perl-Mail-Box
Version:        4.01
Release:        2%{?dist}
Summary:        Manage a mailbox, a folder with messages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Mail::Message) >= 4.00
Requires:       perl(Object::Realize::Later) >= 4.00
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Message\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Object::Realize::Later\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::FcntlLock)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Mail::Box::Parser::Perl)
BuildRequires:  perl(Mail::Message)
BuildRequires:  perl(Mail::Message::Body)
BuildRequires:  perl(Mail::Message::Body::File)
BuildRequires:  perl(Mail::Message::Body::Lines)
BuildRequires:  perl(Mail::Message::Body::Multipart)
BuildRequires:  perl(Mail::Message::Body::String)
BuildRequires:  perl(Mail::Message::Construct)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Reporter)
BuildRequires:  perl(Mail::Transport)
BuildRequires:  perl(Object::Realize::Later)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(User::Identity::Collection)
BuildRequires:  perl(User::Identity::Item)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Overview.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Cookbook.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/Box-Index.pod
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
