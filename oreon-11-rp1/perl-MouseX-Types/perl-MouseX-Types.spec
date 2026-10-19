%global source0_hash 77288441fdadd15beeec9a0813ece8aec1542f1d8ceaaec14755b3f316fbcf8b
Name:           perl-MouseX-Types
Summary:        Organize your Mouse types in libraries
Version:        0.06
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-Types
Source0:        https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Types-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Mouse) >= 0.77
%{?perl_default_filter}
Provides:       perl(MouseX::Types)
Provides:       perl(MouseX::Types::Moose)
Provides:       perl(MouseX::Types::Mouse)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Carp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Exporter)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
