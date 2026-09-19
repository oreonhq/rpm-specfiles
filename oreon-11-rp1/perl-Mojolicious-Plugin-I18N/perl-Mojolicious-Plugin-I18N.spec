%global source0_hash 32fb5ef8037d954b7ecebef5c1b2b24b420abd829702312f4ad42794f52b514d

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(I18N::LangTags\\)$

Name:           perl-Mojolicious-Plugin-I18N
Version:        1.6
Release:        25%{?dist}
Summary:        Internationalization Plugin for Mojolicious
License:        Artistic-2.0
URL:            https://metacpan.org/release/Mojolicious-Plugin-I18N
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHARIFULN/Mojolicious-Plugin-I18N-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(I18N::LangTags) >= 0.35
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojolicious) >= 5
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(I18N::LangTags) >= 0.35
Requires:       perl(Mojolicious) >= 5
Requires:       perl(Mojolicious::Plugin)
Requires:       perl(strict)
Requires:       perl(warnings)

%description
Mojolicious::Plugin::I18N is internationalization plugin for Mojolicious. It
works with Mojolicious 4.0+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Mojolicious-Plugin-I18N-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes script
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
