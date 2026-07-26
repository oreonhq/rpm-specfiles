%global source0_hash 601800cd7a47e5c81f266241404d497f4dfc785e9b1227344159a8b64a76e79c

Name:           perl-JSON-Util
Version:        0.06
Release:        31%{?dist}
Summary:        Easy and portable encode/decode of JSON
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-Util
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKUTEJ/JSON-Util-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Any)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
Provides methods to encode and decode JSON.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Util-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
