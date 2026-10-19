%global source0_hash 9fb65d5a6343368288f6ac83d9f4fad40b1e2ab4811ac1279536c177be9c28f2
Name:       perl-MooseX-MultiInitArg 
Version:    0.02 
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:        Attributes with aliases for constructor arguments
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRODWITH/MooseX-MultiInitArg-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-MultiInitArg
BuildArch:  noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
If you've ever wanted to be able to call an attribute any number of
things while you're passing arguments to your object constructor, Now
You Can. This is an attribute metaclass / trait to allow easy new()-time
attribute aliasing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-MultiInitArg-%{version}

%build

perl Build.PL --installdirs vendor
./Build
%install
./Build install --destdir $RPM_BUILD_ROOT --create_packlist 0
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
