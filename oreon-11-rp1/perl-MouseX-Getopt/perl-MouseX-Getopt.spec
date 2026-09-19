%global source0_hash de3ea8ef452dd9501ea8c4eda8744b7224602602b04692607edd7d62b79f038f

Name:		perl-MouseX-Getopt
Summary:	Mouse role for processing command line options
Version:	0.38
Release:	30%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-Getopt
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Getopt-%{version}.tar.gz
Patch0:		MouseX-Getopt-0.38-GLD-0.113.patch
Patch1:		MouseX-Getopt-0.38-GLD-0.116.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build::Tiny) >= 0.035
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Getopt::Long) >= 2.37
BuildRequires:	perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:	perl(Mouse) >= 0.64
BuildRequires:	perl(Mouse::Meta::Attribute)
BuildRequires:	perl(Mouse::Role)
BuildRequires:	perl(Mouse::Util::TypeConstraints)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Mouse::Meta::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception) >= 0.21
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Mouse)
BuildRequires:	perl(Test::Warn) >= 0.21
BuildRequires:	perl(Test2::V0)
# Optional Tests (have circular dependencies)
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(MouseX::ConfigFromFile)
BuildRequires:	perl(MouseX::SimpleConfig) >= 0.07
%endif
# Dependencies
Requires:	perl(Mouse) >= 0.64
Requires:	perl(Mouse::Meta::Attribute)

# Filter under-specified dependency
%global __requires_exclude ^perl\\(Mouse\\)$

%description
This is a Mouse role that provides an alternate constructor for creating
objects using parameters passed in from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-Getopt-%{version}

# Fix compatibility with GLD 0.107 .. 0.113
# https://github.com/gfx/mousex-getopt/pull/15
%patch -P 0

# Fix compatibility with GLD 0.116
# https://github.com/gfx/mousex-getopt/pull/16
%patch -P 1 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
# Note: malformed LICENSE file in 0.35 .. 0.38 not shipped
# https://github.com/gfx/mousex-getopt/issues/2
%doc Changes README.md
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::Getopt.3*
%{_mandir}/man3/MouseX::Getopt::Basic.3*
%{_mandir}/man3/MouseX::Getopt::Dashes.3*
%{_mandir}/man3/MouseX::Getopt::GLD.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::NoGetopt.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::Trait.3*
%{_mandir}/man3/MouseX::Getopt::Meta::Attribute::Trait::NoGetopt.3*
%{_mandir}/man3/MouseX::Getopt::OptionTypeMap.3*
%{_mandir}/man3/MouseX::Getopt::Strict.3*

%changelog
%autochangelog
