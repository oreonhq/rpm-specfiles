%global source0_hash 2d99975685242980d0a9904f639144c059d6ece15899efde4acb742d3253f105
Name:           perl-autovivification
Version:        0.18
Release:        28%{?dist}
Summary:        Lexically disable autovivification
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/autovivification
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/autovivification-%{version}.tar.gz
Requires:       perl(XSLoader)
%{?perl_default_filter}
Provides:       perl(autovivification)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When an undefined variable is dereferenced, it gets silently upgraded to an
array or hash reference (depending of the type of the dereferencing). This
behavior is called autovivification and usually does what you mean (e.g.
when you store a value) but it's sometimes unnatural or surprising because
your variables gets populated behind your back. This is especially true
when several levels of dereferencing are involved, in which case all levels
are vivified up to the last, or when it happens in intuitively read-only
constructs like exists.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n autovivification-%{version}

%build

perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}"  \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
