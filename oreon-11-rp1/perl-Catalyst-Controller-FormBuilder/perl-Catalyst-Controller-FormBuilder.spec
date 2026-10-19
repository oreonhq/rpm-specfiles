%global source0_hash 78484f2759216a9fc705461201edc763a0b4179bdf30c9036f1e4d774923319a
Name:           perl-Catalyst-Controller-FormBuilder
Version:        0.06
Release:        44%{?dist}
Summary:        Catalyst FormBuilder Base Controller
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Controller-FormBuilder
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Catalyst-Controller-FormBuilder-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Catalyst)
Requires:       perl(warnings)
Requires:       perl(lib)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI::FormBuilder)
BuildRequires:  perl(CGI::FormBuilder::Source::File)
BuildRequires:  perl(CGI::FormBuilder::Util)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::View)
BuildRequires:  perl(Catalyst::View::HTML::Template)
BuildRequires:  perl(Catalyst::View::Mason)
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
