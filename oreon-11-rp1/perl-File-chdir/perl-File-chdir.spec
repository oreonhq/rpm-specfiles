Name:           perl-File-chdir
Version:        0.1011
Release:        29%{?dist}
Summary:        A more sensible way to change directories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-chdir
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd) >= 3.16
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions) >= 3.27
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies

%description
Perl's chdir() has the unfortunate problem of being very, very, very
global. If any part of your program calls chdir() or if any library you
use calls chdir(), it changes the current working directory for the
whole program.

This is not good.

File::chdir gives you an alternative, $CWD and @CWD. These two variables
combine all the power of chdir(), File::Spec and Cwd.

%prep
%setup -q -n File-chdir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::chdir.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1011-29
- Prepare for Oreon 11 (RP1)
