%global source0_hash 9915db17c3e0deb4ff4c9065dc2eaf1d3833096937a0d46e573f6f2a76158c54

Name:		perl-Mail-Message
Version:	4.04
Release:	1%{?dist}
Summary:	MIME message handling
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mail-Message
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Message-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.16
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Encode) >= 2.26
BuildRequires:	perl(Encode::Alias)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec) >= 0.7
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Hash::Case) >= 1.05
BuildRequires:	perl(Hash::Case::Preserve)
BuildRequires:	perl(HTML::FormatPS)
BuildRequires:	perl(HTML::FormatText) >= 2.01
BuildRequires:	perl(HTML::TreeBuilder) >= 3.13
BuildRequires:	perl(integer)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Lines)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Log::Report) >= 1.42
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Mail::Address) >= 2.17
BuildRequires:	perl(Mail::Header)
BuildRequires:	perl(Mail::Identity)
BuildRequires:	perl(Mail::Internet) >= 2.01
%if !%{defined perl_bootstrap}
BuildRequires:	perl(Mail::Transport::Send) >= 4
%endif
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(MIME::Entity) >= 3.0
BuildRequires:	perl(MIME::Parser)
BuildRequires:	perl(MIME::QuotedPrint)
BuildRequires:	perl(MIME::Types) >= 1.004
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util) >= 1.13
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test::More) >= 1.00
BuildRequires:	perl(Text::Autoformat)
BuildRequires:	perl(Time::HiRes) >= 1.51
BuildRequires:	perl(Time::Zone)
BuildRequires:	perl(URI) >= 1.23
BuildRequires:	perl(User::Identity) >= 4
BuildRequires:	perl(User::Identity::Collection::Emails)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# Test Suite
# (no additional dependencies)
# Optional Tests
%if !%{defined perl_bootstrap}
BuildRequires:	perl(Email::Abstract)
%endif
# Dependencies
Requires:	perl(Date::Parse)
%if !%{defined perl_bootstrap}
Requires:	perl(Mail::Transport::Send) >= 4
%endif
Requires:	perl(Net::Domain)
Requires:	perl(Time::HiRes) >= 1.51
Requires:	perl(Time::Zone)
Requires:	perl(User::Identity) >= 4

# I'm not sure why these provides aren't getting picked up automatically.
Provides:	perl(Mail::Message::Body::Construct) = %{version}
Provides:	perl(Mail::Message::Construct) = %{version}
Provides:	perl(Mail::Message::Construct::Bounce) = %{version}
Provides:	perl(Mail::Message::Construct::Build) = %{version}
Provides:	perl(Mail::Message::Construct::Forward) = %{version}
Provides:	perl(Mail::Message::Construct::Read) = %{version}
Provides:	perl(Mail::Message::Construct::Rebuild) = %{version}
Provides:	perl(Mail::Message::Construct::Reply) = %{version}
Provides:	perl(Mail::Message::Construct::Text) = %{version}

%description
MIME message handling code, formerly part of the Mail::Box package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Message-%{version}
# The licensing on these test files is unclear.
# They seem to contain content posted publicly to usenet
# so there is an argument that the content is distributable
# but it's not under a Free license.
# We delete these files to resolve the issue.
# https://rt.cpan.org/Public/Bug/Display.html?id=120149
rm -rf t/203-mlfolder.mbox t/204-sgfolder.mbox
rm -rf t/203head-listgroup.t t/204head-spamgroup.t
perl -i -ne 'print $_ unless m{^t/20[34]-(ml|sg)folder\.mbox$}' MANIFEST
perl -i -ne 'print $_ unless m{^t/20[34]head-(list|spam)group\.t$}' MANIFEST

%build
yes y |perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::*.3*

%changelog
%autochangelog
