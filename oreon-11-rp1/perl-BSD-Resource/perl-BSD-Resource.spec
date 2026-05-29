%global source0_hash 9d1cfba063cc18f72427a22451f7908836b7331ac8785dbe07553c5b043a0c3d

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_BSD_Resource_enables_optional_test
%else
%bcond_with perl_BSD_Resource_enables_optional_test
%endif

Name:           perl-BSD-Resource
Version:        1.291.100
%global module_version 1.2911
Release:        31%{?dist}
Summary:        BSD process resource limit and priority functions
# No matter what the pm and xs headers say, this is stated in the POD and,
# according to upstream changelog for 1.2905, is correct.
# No matter what POD says, ppport.h comes from perl with perl's license.
License:        (Artistic-2.0 OR LGPL-2.0-only) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/BSD-Resource
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
%if %{with perl_BSD_Resource_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif

%{?perl_default_filter}

%description
A module providing an interface for testing and setting process limits
and priorities.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n BSD-Resource-%{module_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorarch}/BSD/
%{perl_vendorarch}/auto/BSD/
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.291.100-31
- Prepare for Oreon 11 (RP1)
