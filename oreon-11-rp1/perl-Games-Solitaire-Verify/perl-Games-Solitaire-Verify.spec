%global source0_hash 32b20e560c4b78c899a1697ef5c187f2726df9eb10e4845630687e85498ef573

%define upstream_name    Games-Solitaire-Verify

Name:       perl-%{upstream_name}
Version:    0.2601
Release:    4%{?dist}

Summary:    Process and verify solitaire games
License:    MIT
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{version}.tar.gz

BuildRequires: findutils
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Dir::Manifest)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(autodie)
BuildRequires: perl(blib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
This is a CPAN Perl module that verifies the solutions of various variants
of card Solitaire. It does not aim to try to be a solver for them, because
this is too CPU intensive to be adequately done using perl5 (as of
perl-5.10.0). If you're interested in the latter, look at:

* https://fc-solve.shlomifish.org/

* https://fc-solve.shlomifish.org/links.html#other_solvers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}

%build
%__perl Build.PL --installdirs=vendor

./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
chmod 755 %{buildroot}/%{_bindir}/*

%files
%license COPYING LICENSE
%doc Changes README examples
%{_bindir}/expand-solitaire-multi-card-moves
%{_bindir}/verify-solitaire-solution
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
%autochangelog
