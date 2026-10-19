%global source0_hash 59f844e3ed16d352192247926ea0452658c7600c4b10327048031bc563f99aa6
Name:           perl-Scalar-Construct
Version:        0.000
Release:        45%{?dist}
Summary:        Build custom kinds of scalar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-Construct
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Scalar-Construct-%{version}.tar.gz
Requires:       perl(Exporter)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(parent)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module supplies functions to construct Perl scalar objects. While
writable (variable) scalars can easily be constructed using the ordinary
facilities of the Perl language, immutable (constant) scalars require a
library such as this.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Scalar-Construct-%{version}

%build

perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
