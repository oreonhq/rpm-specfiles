%global source0_hash 71733c4c348e98fdd575b44a52042428c39888a18c25656efe59ef3d7d0d27e5

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_indirect_enables_extra_test
%else
%bcond_with perl_indirect_enables_extra_test
%endif

Name:           perl-indirect
Version:        0.39
Release:        29%{?dist}
Summary:        Lexically warn about using the indirect object syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/indirect
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/indirect-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(B)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
# Optional Tests
%if 0%{!?perl_bootstrap:1} && %{with perl_indirect_enables_extra_test}
BuildRequires:  perl(Devel::CallParser)
BuildRequires:  perl(Devel::Declare) >= 0.006007
%endif
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Socket)
# Runtime
Requires:       perl(Carp)
Requires:       perl(XSLoader)

# Avoid provides for perl shared objects
%{?perl_default_filter}

Provides:       perl(indirect)
%description
When enabled (or disabled as some may prefer to say, since you actually
turn it on by calling no indirect), this pragma warns about indirect object
syntax constructs that may have slipped into your code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n indirect-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README samples/
%{perl_vendorarch}/auto/indirect/
%{perl_vendorarch}/indirect.pm
%{_mandir}/man3/indirect.3*

%changelog
%autochangelog
