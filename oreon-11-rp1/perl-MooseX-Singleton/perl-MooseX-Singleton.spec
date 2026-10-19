%global source0_hash 6584b2f31b1d3eb6dd7e23128738e73f6c015b152138b0a8157d3d0d59d06541
Name:           perl-MooseX-Singleton
Version:        0.30
Release:        1%{?dist}
Summary:        Turn your Moose class into a singleton
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Singleton
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Singleton-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
A singleton is a class that has only one instance in an application.
MooseX::Singleton lets you easily upgrade (or downgrade, as it were) your
Moose class to a singleton.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Singleton-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
