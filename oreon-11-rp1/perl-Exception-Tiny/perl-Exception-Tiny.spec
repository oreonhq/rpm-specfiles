%global source0_hash 0c41019479c32097f8b2c716d35475d8426ee0e61a453a0bedeb37430c8de65d

Name:           perl-Exception-Tiny
Version:        0.2.1
Release:        34%{?dist}
Summary:        Tiny Perl exception interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Exception-Tiny
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YAPPO/Exception-Tiny-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(overload)
 
%{?perl_default_filter}

%description
Exception::Tiny is a simple exception interface. This is the
implementation of the minimum required in order to implement exception
handling so that anyone can understand the implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Exception-Tiny-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Exception*
%{_mandir}/man3/Exception*

%changelog
%autochangelog
