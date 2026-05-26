Name:           perl-Variable-Magic
Version:        0.64
Release:        7%{?dist}
Summary:        Associate user-defined magic to variables from Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Variable-Magic
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 9f7853249c9ea3b4df92fb6b790c03a60680fc029f44c8bf9894dccf019516bd
%global source0_file Variable-Magic-0.64.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(bytes)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional Tests
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Perl::Destruct::Level)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
# Dependencies
Requires:       perl(Carp)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Magic is Perl way of enhancing objects. This mechanism let the user add
extra data to any variable and hook syntactical operations (such as access,
assignation or destruction) that can be applied to it. With this module,
you can add your own magic to any variable without the pain of the C API.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Variable-Magic-0.64.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9f7853249c9ea3b4df92fb6b790c03a60680fc029f44c8bf9894dccf019516bd" || { echo "oreon: Source0 SHA256 mismatch for Variable-Magic-0.64.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Variable-Magic-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/Variable/
%{perl_vendorarch}/Variable/
%{_mandir}/man3/Variable::Magic.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-7
- Prepare for Oreon 11 (RP1)
