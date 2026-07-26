%global source0_hash fe87301cd5141f5d047ddc79077d0ad3753089a7df9189dcb5a2fdf8fc11fc7e

Name:           perl-JSON-RPC-LWP
Version:        0.007
Release:        21%{?dist}
Summary:        JSON RPC over any libwww supported protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-RPC-LWP
Source0:        https://cpan.metacpan.org/authors/id/B/BG/BGILLS/JSON-RPC-LWP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.008
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::RPC::Common)
BuildRequires:  perl(JSON::RPC::Common::Marshal::HTTP)
BuildRequires:  perl(JSON::RPC::Common::TypeConstraints)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Deprecated)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI) >= 1.58
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# used with Moose 'with' so not found by perl-generators
Requires:       perl(MooseX::Deprecated)

%description
Use any version of JSON RPC over any libwww supported transport protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-RPC-LWP-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
