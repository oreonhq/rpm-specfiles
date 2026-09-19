%global source0_hash 9b04df5d47dcd45ac4299626a10ec990fb40c94ee5a6300c3a88bdfb3575ec29

Name:           perl-Cookie-Baker
Version:        0.12
Release:        7%{?dist}
Summary:        Cookie string generator / parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cookie-Baker
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cookie-Baker-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Time)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
Cookie::Baker provides simple cookie string generator and parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cookie-Baker-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
