Name:           perl-Pod-Markdown
Version:        3.400
Release:        7%{?dist}
Summary:        Convert POD to Markdown
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Markdown
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Pod-Markdown-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a626e99bcd4e7d214e43d4722a54e3aafac3713862f7479cfb94a0e2879f8442
%global source0_file Pod-Markdown-3.400.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Encode)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Simple) >= 3.27
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)

%description
This module subclasses Pod::Parser and converts POD to Markdown.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Pod-Markdown-3.400.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a626e99bcd4e7d214e43d4722a54e3aafac3713862f7479cfb94a0e2879f8442" || { echo "oreon: Source0 SHA256 mismatch for Pod-Markdown-3.400.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Pod-Markdown-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c $RPM_BUILD_ROOT

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/pod2markdown
%{perl_vendorlib}/Pod/
%{_mandir}/man1/pod2markdown.1*
%{_mandir}/man3/Pod::Markdown.3*
%{_mandir}/man3/Pod::Perldoc::ToMarkdown.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.400-7
- Prepare for Oreon 11 (RP1)
