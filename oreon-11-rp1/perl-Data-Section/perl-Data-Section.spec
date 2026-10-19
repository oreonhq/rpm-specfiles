%global source0_hash 83acc7a55d3dd7ed36e9d78d350af3138c69cfa178a44765822712ff433b990e
%bcond_with perl_Data_Section_enables_extra_test
%bcond_with perl_Data_Section_enables_optional_test
Name:           perl-Data-Section
Version:        0.200008
Release:        1%{?dist}
Summary:        Read multiple hunks of data out of your DATA section
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Section
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-Section-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Data_Section_enables_optional_test}
%endif
%if %{with perl_Data_Section_enables_extra_test}
%endif
Provides:       perl(Data::Section)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Data::Section provides an easy way to access multiple named chunks of
line-oriented data in your module's DATA section. It was written to allow
modules to store their own templates, but probably has other uses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Section-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} -c $RPM_BUILD_ROOT
%oreon_autofiles main

%check

make test
%if %{with perl_Data_Section_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.200008-9
- Prepare for Oreon 11 (RP1)
