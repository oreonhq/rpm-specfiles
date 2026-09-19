%global source0_hash 6f13b2c07aff8307a3d3805a0f407a6d9481a2a554b3501fa008beb4a47d6d69

Name:           perl-Bisect-Perl-UsingGit
Version:        0.33
Release:        40%{?dist}
Summary:        Help you to bisect Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Bisect-Perl-UsingGit
Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/Bisect-Perl-UsingGit-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types::Path::Class)
# Tests only:
BuildRequires:  perl(Test::More) >= 0.01
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       git
Requires:       perl(MooseX::Getopt)

%description
Bisect::Perl::UsingGit is a module which holds the code which helps you to
bisect Perl. See bisect_perl_using_git for practical examples.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Bisect-Perl-UsingGit-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
