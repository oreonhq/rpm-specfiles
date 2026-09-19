%global source0_hash ccf81bba5200d3a0ad6901f923af173a3d4416618aea08a6938baaffdef4cb20

Name:           perl-Catalyst-Action-REST
Version:        1.21
Release:        25%{?dist}
Summary:        Automated REST Method Dispatching
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Action-REST
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Action-REST-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Log)
BuildRequires:  perl(Catalyst::Request)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80030
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Inspector) >= 1.13
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Taxi)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.75 
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(JSON) >= 2.12
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::UserAgent) >= 5.00
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 1.03
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Validate) >= 0.76
BuildRequires:  perl(PHP::Serialization)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::Syck)
Requires:       perl(Catalyst::Runtime) >= 5.80030
Requires:       perl(Class::Inspector) >= 1.13
Requires:       perl(Config::General)
Requires:       perl(Data::Taxi)
Requires:       perl(FreezeThaw)
Requires:       perl(JSON) >= 2.12
Requires:       perl(LWP::UserAgent) >= 5.00
Requires:       perl(Moose) >= 1.03
Requires:       perl(MRO::Compat) >= 0.10
Requires:       perl(Params::Validate) >= 0.76
Requires:       perl(PHP::Serialization)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::Syck)

%{?perl_default_filter}

%description
This Action handles doing automatic method dispatching for REST requests.
It takes a normal Catalyst action, and changes the dispatch to append an
underscore and method name. First it will try dispatching to an action
with the generated name, and failing that it will try to dispatch to a
regular method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Action-REST-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
