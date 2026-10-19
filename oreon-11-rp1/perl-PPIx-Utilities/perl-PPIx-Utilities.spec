%global source0_hash 03a483386fd6a2c808f09778d44db06b02c3140fb24ba4bf12f851f46d3bcb9b
%bcond_with perl_PPIx_Utilities_enables_extra_test
Name:		perl-PPIx-Utilities
Version:	1.001000
Release:        56%{?dist}
Summary:        Extensions to PPI
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/PPIx-Utilities
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1} && %{with perl_PPIx_Utilities_enables_extra_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Document::Fragment)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is a collection of functions for dealing with PPI objects, many of
which originated in Perl::Critic. They are organized into modules by the
kind of PPI class they relate to, by replacing the "PPI" at the front of
the module name with "PPIx::Utilities", e.g. functionality related to
PPI::Nodes is in PPIx::Utilities::Node.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPIx-Utilities-%{version}

# Remove date-sensitive copyright.t, which also upsets Perl::Critic
# (#1139503)
rm xt/author/copyright.t
sed -i -e '/copyright\.t/d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%if 0%{!?perl_bootstrap:1} && %{with perl_PPIx_Utilities_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
