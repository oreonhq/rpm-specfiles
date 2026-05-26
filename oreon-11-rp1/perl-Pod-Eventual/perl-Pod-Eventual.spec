Name:           perl-Pod-Eventual
Version:        0.094003
Release:        9%{?dist}
Summary:        Read a POD document as a series of trivial events
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Eventual
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Pod-Eventual-0.094003.tar.gz
# oreon url source checksums begin
%global source0_sha256 7f060cc34d11656ce069db061e3d60edc0cabc8f89a4a2dc7eaae95dac856d2d
%global source0_file Pod-Eventual-0.094003.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.102
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
# Optional Tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Explicit dependencies:

%description
POD is a pretty simple format to write, but it can be a big pain to deal with
reading it and doing anything useful with it. Most existing POD parsers care
about semantics, like whether a =item occurred after an =over but before a
back, figuring out how to link a L<>, and other things like that.

Pod::Eventual is much less ambitious and much more stupid. Fortunately, stupid
is often better (that's what I keep telling myself, anyway).

Pod::Eventual reads line-based input and produces events describing each POD
paragraph or directive it finds. Once complete events are immediately passed to
the handle_event method. This method should be implemented by Pod::Eventual
sub-classes. If it isn't, Pod::Eventual's own handle_event will be called, and
will raise an exception.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Pod-Eventual-0.094003.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7f060cc34d11656ce069db061e3d60edc0cabc8f89a4a2dc7eaae95dac856d2d" || { echo "oreon: Source0 SHA256 mismatch for Pod-Eventual-0.094003.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Pod-Eventual-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Pod/
%{_mandir}/man3/Pod::Eventual.3*
%{_mandir}/man3/Pod::Eventual::Simple.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.094003-9
- Prepare for Oreon 11 (RP1)
