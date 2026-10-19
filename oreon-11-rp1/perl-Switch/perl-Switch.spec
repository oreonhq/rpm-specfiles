%global source0_hash 31354975140fe6235ac130a109496491ad33dd42f9c62189e23f49f75f936d75
Name:		perl-Switch
Version:	2.17
Release:        35%{?dist}
Summary:        A switch statement for Perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Switch
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Switch-%{version}.tar.gz
Patch0:		Switch-2.17-Filter-1.50.patch
Requires:	perl(deprecate)
BuildArch:	noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Switch.pm provides the syntax and semantics for an explicit case mechanism for 
Perl. The syntax is minimal, introducing only the keywords C<switch> and 
C<case> and conforming to the general pattern of existing Perl control 
structures. The semantics are particularly rich, allowing any one (or more) of 
nearly 30 forms of matching to be used when comparing a switch value with its 
various cases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Switch-%{version}
%patch -P0 -p1 -b .fixme

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17-35
- Import
