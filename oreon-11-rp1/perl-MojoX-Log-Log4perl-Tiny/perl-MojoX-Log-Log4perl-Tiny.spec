%global source0_hash cd637dcd676c31343904f0af500ba22aca77ff2ddb0410a453700eb651132284

Name:           perl-MojoX-Log-Log4perl-Tiny
Version:        0.01
Release:        20%{?dist}
Summary:        Minimalistic Log4perl adapter for Mojolicious
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MojoX-Log-Log4perl-Tiny
Source0:        https://cpan.metacpan.org/authors/id/Y/YO/YOWCOW/MojoX-Log-Log4perl-Tiny-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
# runtime dependencies
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(strict)
# test dependencies
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Log::Log4perl)

%description
MojoX::Log::Log4perl::Tiny allows you to replace default Mojolicious
logging Mojo::Log with your existing Log::Log4perl::Logger instance.

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MojoX-Log-Log4perl-Tiny-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/MojoX*
%{_mandir}/man3/MojoX*

%changelog
%autochangelog
