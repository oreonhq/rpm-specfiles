%global source0_hash e7e38aa7c3b78b5734e9d43cf76832fce00767e6a53d5dd79a1722d8676d5e4e

Name:           perl-MooseX-Attribute-Chained
Version:        1.0.3
Release:        29%{?dist}
Summary:        Attribute that returns the instance to allow for chaining
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Attribute-Chained
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOMHUKINS/MooseX-Attribute-Chained-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Method::Accessor)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# for release testing, but they mostly fail
#BuildRequires:  perl(Pod::Coverage::TrustPod)
#BuildRequires:  perl(Test::HasVersion)
#BuildRequires:  perl(Test::Kwalitee)
#BuildRequires:  perl(Test::MinimumVersion)
#BuildRequires:  perl(Test::Pod)
#BuildRequires:  perl(Test::Pod::Coverage)

# renamed from perl-MooseX-ChainedAccessors in January 2012
# no explicit provides necessary as this package still contains the old classes
# and rpm automatically detects them
Obsoletes:      perl-MooseX-ChainedAccessors <= 0.02-3.fc17

%?perl_default_filter

%description
MooseX::Attribute::Chained is a Moose Trait which allows for method
chaining on accessors by returning $self on write/set operations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Attribute-Chained-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
