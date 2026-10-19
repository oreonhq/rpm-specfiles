%global source0_hash 4f2f017f7a8754fbb6e91206c88ed13c756a14e3bea178188c3b97746366eb32
Name:           perl-HTML-FormFu
Version:        2.07
Release:        1%{?dist}
Summary:        HTML Form Creation, Rendering and Validation Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/HTML-FormFu-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Captcha::reCAPTCHA) >= 0.93
Requires:       perl(Class::Accessor::Chained::Fast)
Requires:       perl(Config::Any) >= 0.18
Requires:       perl(Crypt::DES)
Requires:       perl(Data::Visitor) >= 0.26
Requires:       perl(Date::Calc)
Requires:       perl(DateTime) >= 0.38
Requires:       perl(DateTime::Format::Builder) >= 0.80
Requires:       perl(HTML::TokeParser::Simple) >= 3.14
Requires:       perl(HTTP::Headers) >= 1.64
Requires:       perl(Locale::Maketext)
Requires:       perl(MooseX::Attribute::Chained) >= 1.0.1
Requires:       perl(Template)
Requires:       perl(YAML::XS) >= 0.32
%{?perl_default_filter:
%filter_from_provides /perl(unicode/d
%filter_from_requires /perl(Catalyst/d; /perl(default/d; /perl(model_config)/d;
%perl_default_filter
}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Class::MOP::Method)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Visitor)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::TokeParser::Simple)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(Hash::Flatten)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(Number::Format)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
HTML::FormFu is a HTML form framework which aims to be as easy as possible
to use for basic web forms, but with the power and flexibility to do
anything else you might want to do (as long as it involves forms).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormFu-%{version}

find examples -type f | xargs chmod 644
find examples -type f | xargs sed -i -e 's/\r//'

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/blib
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
