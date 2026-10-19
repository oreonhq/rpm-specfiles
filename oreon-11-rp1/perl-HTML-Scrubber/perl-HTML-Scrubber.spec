%global source0_hash ae285578f8565f9154c63e4234704b57b6835f77a2f82ffe724899d453262bb1
Name:           perl-HTML-Scrubber
Version:        0.19
Release:        1%{?dist}
Summary:        Library for scrubbing/sanitizing html
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Scrubber
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/HTML-Scrubber-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
If you wanna "scrub" or "sanitize" html input in a reliable an flexible
fashion, then this module is for you.
I wasn't satisfied with HTML::Sanitizer because it is based on
HTML::TreeBuilder, so I thought I'd write something similar that works
directly with HTML::Parser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Scrubber-%{version}
%{__perl} -pi -e 's/\r\n/\n/' Changes LICENSE README Scrubber.pm

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
