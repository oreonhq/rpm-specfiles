%global source0_hash c350524507cd827fab864e5d4c2cc350b1babaa12fa95aec0ca00843fcc7deeb

Name:		perl-aliased
Version:	0.34
Release:	32%{?dist}
Summary:	Use shorter versions of class names
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/aliased
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/aliased-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build::Tiny) >= 0.039
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
# Runtime
Requires:	perl(Carp)

Provides:       perl(aliased)
Provides:       perl(aliased)
%description
aliased is simple in concept but is a rather handy module. It loads the
class you specify and exports into your namespace a subroutine that returns
the class name. You can explicitly alias the class to another name or, if
you prefer, you can do so implicitly. In the latter case, the name of the
subroutine is the last part of the class name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n aliased-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/aliased.pm
%{_mandir}/man3/aliased.3*

%changelog
%autochangelog
