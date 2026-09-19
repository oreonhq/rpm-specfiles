%global source0_hash ff786008bf8c022064ececd3b7ed89c76b35e8d1eac6cf472a9f51771c1c9f2c

Name:		perl-Mock-Quick
Version:	1.111
Release:	27%{?dist}
Summary:	Quickly mock objects and classes, side-effect free
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mock-Quick
Source0:	http://cpan.metacpan.org/authors/id/E/EX/EXODIST/Mock-Quick-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.42
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Exporter::Declare) >= 0.103
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Fennec::Lite) >= 0.004
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Exception) >= 0.29
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
Mock-Quick is here to solve the current problems with Mocking libraries.

There are a couple of Mocking libraries available on CPAN. The primary problems
with these libraries include verbose syntax, and most importantly side-effects.
Some Mocking libraries expect you to mock a specific class, and will unload it
then redefine it. This is particularly a problem if you only want to override
a class on a lexical level.

Mock-Object provides a declarative mocking interface that results in a very
concise, but clear syntax. There are separate facilities for mocking object
instances, and classes. You can quickly create an instance of an object with
custom attributes and methods. You can also quickly create an anonymous class,
optionally inheriting from another, with whatever methods you desire.

Mock-Object also provides a tool that provides an OO interface to overriding
methods in existing classes. This tool also allows for the restoration of the
original class methods. Best of all, this is a localized tool: when your
control object falls out of scope, the original class is restored.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mock-Quick-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Mock/
%{perl_vendorlib}/Object/
%{_mandir}/man3/Mock::Quick.3*
%{_mandir}/man3/Mock::Quick::Class.3*
%{_mandir}/man3/Mock::Quick::Method.3*
%{_mandir}/man3/Mock::Quick::Object.3*
%{_mandir}/man3/Mock::Quick::Object::Control.3*
%{_mandir}/man3/Mock::Quick::Util.3*
%{_mandir}/man3/Object::Quick.3*

%changelog
%autochangelog
