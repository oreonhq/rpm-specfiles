%global source0_hash b4c29e224bbadae5ca8da3d512672a43f88af98dab5985c2d5181a9bda794e07
Name:           perl-Export-Attrs
Version:        0.1.0
Release:        1%{?dist}
Summary:        The Perl 6 'is export(...)' trait as a Perl 5 attribute
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Export-Attrs
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/Export-Attrs-v%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a fork of Perl6::Export::Attrs created to restore
compatibility with Perl6::Export::Attrs version 0.0.3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Export-Attrs-v%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
