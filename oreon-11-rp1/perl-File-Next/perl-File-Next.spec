%global source0_hash f900cb39505eb6e168a9ca51a10b73f1bbde1914b923a09ecd72d9c02e6ec2ef

Name:           perl-File-Next
Version:        1.18
Release:        20%{?dist}
Summary:        An iterator-based module for finding files
License:        Artistic-2.0
URL:            https://metacpan.org/release/File-Next
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Next-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(File::Spec)
# Tests:
# App::Ack not used
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

%description
File::Next is an iterator-based module for finding files.  It's
lightweight, has no dependencies, runs under taint mode, and puts your
program more directly in control of file selection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Next-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
