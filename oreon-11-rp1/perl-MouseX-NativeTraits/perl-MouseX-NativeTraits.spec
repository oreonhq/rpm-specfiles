%global source0_hash f8a5bf5a28702dfb13c8093be5c41cab9c5fc1c5d247ab91e22e7dd72764cb5e

Name:           perl-MouseX-NativeTraits
Version:        1.09
Release:        29%{?dist}
Summary:        Extend your attribute interfaces for Mouse
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-NativeTraits
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-NativeTraits-%{version}.tar.gz
Patch0:         MouseX-NativeTraits-1.09-Disable-author-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Any::Moose) >= 0.13
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(inc::Module::Install) >= 1.06
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::TestTarget) >= 0.19
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse) >= 0.82
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(warnings)
Requires:       perl(Mouse) >= 0.82

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mouse\\)

%description
While Mouse attributes provide a way to name your accessors, readers,
writers, clearers and predicates, MouseX::NativeTraits provides commonly
used attribute helper methods for more specific types of data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-NativeTraits-%{version}
%patch -P0 -p1
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
