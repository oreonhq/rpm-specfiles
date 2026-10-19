%global source0_hash eb7b78dda3125752cc8bcc0396d3977fbd28da33d2d44c5042ad6d35d6cde827
Name:           perl-HTML-FormHandler
Version:        0.40068
Release:        1%{?dist}
Summary:        HTML forms using Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormHandler
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/HTML-FormHandler-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Locale::Maketext) >= 1.09
Requires:       perl(Moose) >= 2.0007
Requires:       perl(MooseX::Getopt) >= 0.16
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Common)
Requires:       perl(MooseX::Types::LoadableClass) >= 0.006
Requires:       perl(namespace::autoclean) >= 0.09
Provides:       perl(HTML::FormHandler::Meta::Role) = %{version}
Provides:       perl(HTML::FormHandler::Model::CDBI) = %{version}
Provides:       perl(HTML::FormHandler::Params) = %{version}
Provides:       perl(HTML::FormHandler::Field::Repeatable::Instance) = %{version}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::LoadableClass)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTML::FormHandler is a form handling class that validates HTML form data and,
for database forms, saves it to the database on validation. It has field
classes that can be used for creating a set of widgets and highly automatic
templates. There are two simple rendering roles plus a set of widget roles for
individual form and field classes. FormHandler is designed to make it easy to
produce alternative rendering modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormHandler-%{version}

find lib -type f -print0 | xargs -0 chmod 644

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
