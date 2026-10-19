%global source0_hash 84053cf1a68fcc8c12056c2f120adf04f7f68e3be34f4408e95d026fee67e33e
Name:		perl-Class-C3
Version:	0.35
Release:        1%{?dist}
Summary:        Pragma to use the C3 method resolution order algorithm
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-C3
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-C3-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1}
%endif
Requires:	perl(Algorithm::C3) >= 0.07
Requires:	perl(Scalar::Util) >= 1.10
Provides:	perl(c3) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(NEXT)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a pragma to change Perl 5's standard method resolution order from
depth-first left-to-right (a.k.a - pre-order) to the more sophisticated C3
method resolution order.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-C3-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
cp -p opt/c3.pm %{buildroot}%{perl_vendorlib}/
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
