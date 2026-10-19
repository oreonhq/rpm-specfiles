%global source0_hash 7f060cc34d11656ce069db061e3d60edc0cabc8f89a4a2dc7eaae95dac856d2d
Name:           perl-Pod-Eventual
Version:        0.094003
Release:        9%{?dist}
Summary:        Read a POD document as a series of trivial events
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Eventual
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Eventual-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Pod::Eventual::Simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Mixin::Linewise::Readers)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Eventual-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.094003-9
- Prepare for Oreon 11 (RP1)
