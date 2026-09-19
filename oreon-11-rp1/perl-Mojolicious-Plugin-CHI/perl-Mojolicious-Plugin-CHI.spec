%global source0_hash d04a5ce98ec6cb8f675a37c19c4957796a9d97c98a3d7a5d178bbd7d5e9c5cfe

Name:           perl-Mojolicious-Plugin-CHI
Version:        0.20
Release:        22%{?dist}
Summary:        Use CHI Caches in Mojolicious
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojolicious-Plugin-CHI
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKRON/Mojolicious-Plugin-CHI-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(CHI)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Mojolicious) >= 4.77
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output) >= 1
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Mojolicious::Plugin::CHI is a simple plugin to work with CHI caches within
Mojolicious.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojolicious-Plugin-CHI-%{version}
find lib -type f -exec chmod -c -x {} ';'
chmod -c -x Changes LICENSE

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
