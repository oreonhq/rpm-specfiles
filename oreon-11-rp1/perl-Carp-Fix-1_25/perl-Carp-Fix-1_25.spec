%global source0_hash 241ebd75dbbd6564a0430a9c413caf9805ea27e94bce5034fb85b33b5e26984a

Name:		perl-Carp-Fix-1_25
Version:	1.000001
Release:	37%{?dist}
Summary:	Smooth over incompatible changes in Carp 1.25
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Carp-Fix-1_25
Source0:	https://cpan.metacpan.org/modules/by-module/Carp/Carp-Fix-1_25-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.36
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
Carp 1.25 made a change to its formatting, adding a period at the end of the
message. This can mess up tests and code that are looking for error messages.
Carp::Fix::1_25 makes the message consistent, regardless of what version of
Carp you're using.

Carp::Fix::1_25 exports its own carp functions, which change the Carp message
to match the 1.25 version. Carp::Fix::1_25 otherwise acts exactly like Carp and
it will honor Carp global variables such as @CARP_NOT and %%Carp::Internal.

Why do this instead of just upgrading Carp? Upgrading Carp would affect all
installed code all at once. You might not be ready for that, or you might not
want your module to foist that on its users. This lets you fix things one
namespace at a time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carp-Fix-1_25-%{version}

# Unbundle Test-Simple and use the system one (#998410)
rm -rf t/lib/Test
sed -i -e '/^t\/lib\/Test\//d' MANIFEST

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
%doc Changes README
%{perl_vendorlib}/Carp/
%{_mandir}/man3/Carp::Fix::1_25.3*

%changelog
%autochangelog
