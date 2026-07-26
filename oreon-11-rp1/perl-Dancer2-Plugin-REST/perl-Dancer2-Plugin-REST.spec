%global source0_hash 02ccafdcc2d341bb4f32c4f0b7aca07f218a92e74cc619e42c2bc92b8fd84f82

Name:           perl-Dancer2-Plugin-REST
Version:        1.02
Release:        27%{?dist}
Summary:        Plugin for writing RESTful apps with Dancer2
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Dancer2-Plugin-REST
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Dancer2-Plugin-REST-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Dancer2) >= 0.202000
BuildRequires:  perl(Dancer2::Core::HTTP)
BuildRequires:  perl(Dancer2::Core::Request)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(YAML)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This plugin helps you write a RESTful web-service with Dancer2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer2-Plugin-REST-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README README.mkdn
%license LICENSE
%{perl_vendorlib}/Dancer2*
%{_mandir}/man3/Dancer2*

%changelog
%autochangelog
