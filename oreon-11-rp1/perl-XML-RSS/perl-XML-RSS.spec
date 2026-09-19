%global source0_hash bb3b231f5081445912ee866a9046dfacb085cfd317e342e9d89663c85ca680f0

Name:           perl-XML-RSS
Version:        1.65
Release:        3%{?dist}
Summary:        Perl module for managing RDF Site Summary (RSS) files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-RSS
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-RSS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser) >= 2.23
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Module::Build not used
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
# Test::Run::CmdLine::Iface not used
# Optional tests:
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TrailingSpace)
Requires:  perl(XML::Parser) >= 2.23

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser\\)$

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

%check
make test

%files
%doc Changes README TODO examples
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::RSS*.3*

%changelog
%autochangelog
