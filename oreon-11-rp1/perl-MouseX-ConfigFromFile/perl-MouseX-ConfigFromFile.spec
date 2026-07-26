%global source0_hash 921b31cb13fc1f982a602f8e23815b7add23a224257e43790e287504ce879534

Name:		perl-MouseX-ConfigFromFile
Summary:	An abstract Mouse role for setting attributes from a config file
Version:	0.05
Release:	37%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-ConfigFromFile
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-ConfigFromFile-%{version}.tar.gz
Patch0:		MouseX-ConfigFromFile-0.05-hunspell.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Module::Install::AuthorTests)
BuildRequires:	perl(Module::Install::ReadmeFromPod)
BuildRequires:	perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:	perl(Module::Install::Repository)
# Module Runtime
BuildRequires:	perl(Mouse) >= 0.39
BuildRequires:	perl(Mouse::Role)
BuildRequires:	perl(MouseX::Types::Path::Class) >= 0.06
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.94
BuildRequires:	perl(Test::UseAllModules)
# Author Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Spelling), hunspell-en
# Dependencies
Requires:	perl(Mouse) >= 0.39

%description
This is an abstract role that provides an alternate constructor for creating
objects using parameters passed in from a configuration file. The actual
implementation of reading the configuration file is left to concrete sub-roles.

It declares an attribute configfile and a class method new_with_config, and
requires that concrete roles derived from it implement the class method
get_config_from_file.

Attributes specified directly as arguments to new_with_config supersede those
in the configfile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-ConfigFromFile-%{version}

# Add support for hunspell speller
%patch -P 0

# Unbundle Module::Install stuff and Test::UseAllModules
# to check for issues with current toolchain modules
rm -rf inc/
perl -ni -e 'print unless /^inc\//;' MANIFEST

# Avoid the need for Module::Install::AuthorRequires and
# all of upstream's toolchain modules as a result of the unbundling
perl -ni -e 'print unless /author_requires/;' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_POD=1 TEST_VERBOSE=1

%files
%doc Changes README
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::ConfigFromFile.3*

%changelog
%autochangelog
