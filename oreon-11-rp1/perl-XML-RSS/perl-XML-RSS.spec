%global source0_hash bb3b231f5081445912ee866a9046dfacb085cfd317e342e9d89663c85ca680f0
Name:           perl-XML-RSS
Version:        1.65
Release:        3%{?dist}
Summary:        Perl module for managing RDF Site Summary (RSS) files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-RSS
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-RSS-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(XML::Parser) >= 2.23
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TrailingSpace)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-RSS-%{version}
chmod 644 Changes README TODO
find examples -type f -exec chmod 644 {} ';'
find examples -type d -exec chmod 755 {} ';'

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
