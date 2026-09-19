%global source0_hash 8040ffcaa77f03eb42060f0c7d8970d0e4c0f05020281e84034da173903e82ae

Name:           perl-Promise-XS
Version:        0.20
Release:        4%{?dist}
Summary:        Fast promises in Perl
# bundled easyxs is MIT
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:            https://metacpan.org/dist/Promise-XS
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/Promise-XS-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Timer)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Future::AsyncAwait::Awaitable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(AnyEvent)
Requires:       perl(IO::Async::Timer)
Requires:       perl(Mojo::IOLoop)

%description
This module exposes a Promise interface with its major parts
implemented in XS for speed. It is a fork and refactor of
AnyEvent::XSPromises. That module’s interface, a “bare-bones” subset of
that from Promises, is retained.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Promise-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

cp -p easyxs/LICENSE LICENSE.easyxs

%check
make test

%files
%doc Changes README.md
%license LICENSE LICENSE.easyxs
%dir %{perl_vendorarch}/auto/Promise
%{perl_vendorarch}/auto/Promise/XS*
%dir %{perl_vendorarch}/Promise
%{perl_vendorarch}/Promise/XS*
%{_mandir}/man3/Promise::XS*

%changelog
%autochangelog
