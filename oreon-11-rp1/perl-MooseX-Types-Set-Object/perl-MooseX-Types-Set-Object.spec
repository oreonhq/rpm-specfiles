%global source0_hash 107522b6133255f7bb8b5f61d902dc26800196c2390111b1aff2cde12dffefb8
Name:           perl-MooseX-Types-Set-Object
Version:        0.05
Release:        1%{?dist}
Summary:        Set::Object type with coercions and stuff
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-Set-Object
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Set-Object-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides Moose type constraints (see
Moose::Util::TypeConstraints, MooseX::Types).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-Set-Object-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
