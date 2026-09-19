%global source0_hash 6913d14cadc251b23c5b7235f8d4ac3de287138d712b75bd94b002af0b8fa5ee

%define upstream_name    Test-RunValgrind

Name:       perl-%{upstream_name}
Version:    0.2.2
Release:    15%{?dist}

Summary:    Tests that an external program is valgrind-clean
License:    MIT
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build) >= 0.280.0
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Test::Trap)
BuildRequires: perl(blib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
valgrind is an open source and convenient memory debugger that runs on some
platforms. This module runs valgrind (the
http://en.wikipedia.org/wiki/Valgrind manpage) on an executable and makes
sure that valgrind did not find any faults in it.

It originated from some code used to test the Freecell Solver executables
using valgrind, and was extracted into its own CPAN module to allow for
reuse by other projects, including fortune-mod (the
https://github.com/shlomif/fortune-mod manpage).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
%autochangelog
