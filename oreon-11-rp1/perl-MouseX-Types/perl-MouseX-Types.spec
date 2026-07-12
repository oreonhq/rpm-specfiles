%global source0_hash 77288441fdadd15beeec9a0813ece8aec1542f1d8ceaaec14755b3f316fbcf8b

Name:           perl-MouseX-Types
Summary:        Organize your Mouse types in libraries
Version:        0.06
Release:        41%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-Types
Source0:        https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Types-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Mouse) >= 0.77
BuildRequires:  perl(Mouse::Exporter)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Any::Moose) >= 0.15
BuildRequires:  perl(base)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Mouse) >= 0.77

%{?perl_default_filter}

Provides:       perl(MouseX::Types)
Provides:       perl(MouseX::Types::Moose)
Provides:       perl(MouseX::Types::Mouse)
%description
Organize your Mouse types; much as MooseX::Types does for your Moose types.
For more information, please see the MooseX::Types manpage.

This library was split off from Mouse as of Mouse 0.15.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MouseX-Types-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

# Remove unwanted exec permissions
find lib -type f -name '*.pm' -print0 | xargs -0 chmod -c 0644
chmod -c 0644 t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README t/
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::Types.3*
%{_mandir}/man3/MouseX::Types::Moose.3*
%{_mandir}/man3/MouseX::Types::Mouse.3*

%changelog
%autochangelog
