%global source0_hash 9915db17c3e0deb4ff4c9065dc2eaf1d3833096937a0d46e573f6f2a76158c54
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:		perl-Mail-Message
Version:	4.04
Release:        1%{?dist}
Summary:        MIME message handling
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mail-Message
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Message-%{version}.tar.gz
BuildArch:	noarch
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
Requires:	perl(Date::Parse)
%if !%{defined perl_bootstrap}
Requires:	perl(Mail::Transport::Send) >= 4
%endif
Requires:	perl(Net::Domain)
Requires:	perl(Time::HiRes) >= 1.51
Requires:	perl(Time::Zone)
Requires:	perl(User::Identity) >= 4
Provides:	perl(Mail::Message::Body::Construct) = %{version}
Provides:	perl(Mail::Message::Construct) = %{version}
Provides:	perl(Mail::Message::Construct::Bounce) = %{version}
Provides:	perl(Mail::Message::Construct::Build) = %{version}
Provides:	perl(Mail::Message::Construct::Forward) = %{version}
Provides:	perl(Mail::Message::Construct::Read) = %{version}
Provides:	perl(Mail::Message::Construct::Rebuild) = %{version}
Provides:	perl(Mail::Message::Construct::Reply) = %{version}
Provides:	perl(Mail::Message::Construct::Text) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::FormatPS)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Hash::Case)
BuildRequires:  perl(Hash::Case::Preserve)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Lines)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Mail::Header)
BuildRequires:  perl(Mail::Identity)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Mail::Transport::Send)
BuildRequires:  perl(Net::Domain)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(URI)
BuildRequires:  perl(User::Identity)
BuildRequires:  perl(User::Identity::Collection::Emails)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
