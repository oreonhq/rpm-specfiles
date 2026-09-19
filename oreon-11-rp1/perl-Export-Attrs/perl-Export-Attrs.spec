%global source0_hash b4c29e224bbadae5ca8da3d512672a43f88af98dab5985c2d5181a9bda794e07

Name:           perl-Export-Attrs
Version:        0.1.0
Release:        26%{?dist}
Summary:        The Perl 6 'is export(...)' trait as a Perl 5 attribute
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Export-Attrs
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/Export-Attrs-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

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

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Export*
%{_mandir}/man3/Export*

%changelog
%autochangelog
