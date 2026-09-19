%global source0_hash 78484f2759216a9fc705461201edc763a0b4179bdf30c9036f1e4d774923319a

Name:           perl-Catalyst-Controller-FormBuilder
Version:        0.06
Release:        44%{?dist}
Summary:        Catalyst FormBuilder Base Controller
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Controller-FormBuilder
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Catalyst-Controller-FormBuilder-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime) >= 5.7
BuildRequires:  perl(Catalyst::View)
BuildRequires:  perl(Catalyst::View::HTML::Template)
BuildRequires:  perl(Catalyst::View::Mason)
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CGI::FormBuilder) >= 3.02
BuildRequires:  perl(CGI::FormBuilder::Source::File)
BuildRequires:  perl(CGI::FormBuilder::Util)
BuildRequires:  perl(Class::Data::Inheritable) >= 0.04
BuildRequires:  perl(Class::Inspector) >= 1.13
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(mro)
BuildRequires:  perl(MRO::Compat) >= 0.09
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst) >= 0.37
BuildRequires:  perl(Tie::IxHash) >= 1.21
BuildRequires:  perl(warnings)
BuildRequires:  sed

# not auto-picked up, or to keep rpmlint happy...
Requires:       perl(Catalyst)
Requires:       perl(warnings)
Requires:       perl(lib)

%description
This base controller merges the functionality of CGI::FormBuilder with
Catalyst and the following templating systems: Template Toolkit, Mason and
HTML::Template. This gives you access to all of FormBuilder's niceties,
such as controllablefield stickiness, multilingual support, and Javascript
generation. For more details, see CGI::FormBuilder or the website at:
http://www.formbuilder.org

%{?filter_setup:
%filter_from_requires /perl(FindBin)/d; /perl(Test::.*)/d
%filter_from_provides /perl(TestApp.*)/d
%{?perl_default_filter}
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\((FindBin|Test::.*)\\)
%global __provides_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(TestApp.*\\)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Controller-FormBuilder-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
