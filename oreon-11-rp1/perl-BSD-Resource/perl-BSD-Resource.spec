%global source0_hash 9d1cfba063cc18f72427a22451f7908836b7331ac8785dbe07553c5b043a0c3d
%bcond_with perl_BSD_Resource_enables_optional_test
Name:           perl-BSD-Resource
Version:        1.2911
%global module_version 1.2911
Release:        1%{?dist}
Summary:        BSD process resource limit and priority functions
License:        (Artistic-2.0 OR LGPL-2.0-only) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/BSD-Resource
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
%if %{with perl_BSD_Resource_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(BSD::Resource)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A module providing an interface for testing and setting process limits
and priorities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n BSD-Resource-%{module_version} 

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
%make_build
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
