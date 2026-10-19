%global source0_hash 8219736e401c2311da5f515775de43fd87e6384b504da36a192f2b217643077f
Name:           perl-Cairo
Version:        1.109
Release:        1%{?dist}
Summary:        Perl interface to the cairo library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Cairo
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSCH/Cairo-%{version}.tar.gz
Patch0:		perl-Cairo-strlen-type-fix.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
Cairo provides Perl bindings for the vector graphics library cairo.
It supports multiple output targets, including the X Window Systems,
PDF, and PNG.  Cairo produces identical output on all those targets
and makes use of hardware acceleration wherever possible.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cairo-%{version}
%patch -P0 -p1 -b .strlen-type-fix
chmod -c a-x examples/*.pl

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{?_with_testsuite:make test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
