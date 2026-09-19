%global source0_hash 4f2f017f7a8754fbb6e91206c88ed13c756a14e3bea178188c3b97746366eb32

Name:           perl-HTML-FormFu
Version:        2.07
Release:        22%{?dist}
Summary:        HTML Form Creation, Rendering and Validation Framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI) >= 3.37
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Class::MOP::Method)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any) >= 0.18
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Visitor) >= 0.26
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(DateTime) >= 0.38
BuildRequires:  perl(DateTime::Format::Builder) >= 0.80
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.20
BuildRequires:  perl(DateTime::Locale) >= 0.45
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
BuildRequires:  perl(Hash::Flatten)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::TokeParser::Simple) >= 3.14
BuildRequires:  perl(HTTP::Headers) >= 1.64
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose) >= 1.00
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::Attribute::Chained) >= 1.0.1
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(Number::Format)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(YAML::XS) >= 0.32
BuildRequires:  sed
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

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_bindir}/*.pl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
