%global source0_hash de3ea8ef452dd9501ea8c4eda8744b7224602602b04692607edd7d62b79f038f
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:		perl-MouseX-Getopt
Summary:        Mouse role for processing command line options
Version:	0.38
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-Getopt
Source0:        https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Getopt-%{version}.tar.gz
Patch0:		MouseX-Getopt-0.38-GLD-0.113.patch
Patch1:		MouseX-Getopt-0.38-GLD-0.116.patch
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1}
%endif
Requires:	perl(Mouse) >= 0.64
Requires:	perl(Mouse::Meta::Attribute)
%global __requires_exclude ^perl\\(Mouse\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Meta::Attribute)
BuildRequires:  perl(Mouse::Meta::Class)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::ConfigFromFile)
BuildRequires:  perl(MouseX::SimpleConfig)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
