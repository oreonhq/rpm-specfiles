%global source0_hash 448172a27e9437a8def189093e852e8b916e9efd6a754088a6cce634297cdcd5

Name:           perl-Perl-Stripper
Version:        0.10
Release:        24%{?dist}
Summary:        Yet another PPI-based Perl source code stripper
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Stripper
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Perl-Stripper-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(experimental)
BuildRequires:  perl(Log::ger)
BuildRequires:  perl(Moo)
BuildRequires:  perl(PPI)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)

%description
This module is yet another PPI-based Perl source code stripper. Its focus
is on customization and stripping significant information from source code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Stripper-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
