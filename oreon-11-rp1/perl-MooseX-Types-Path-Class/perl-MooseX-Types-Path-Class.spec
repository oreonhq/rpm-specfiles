%global source0_hash e784bab53698ae95a709a8663306145ffec55668df6cf31615333523fbe7ef7e
Name:           perl-MooseX-Types-Path-Class 
Summary:        A Path::Class type library for Moose
Version:        0.09
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-Path-Class
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Types-Path-Class-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 0.39
Suggests:       perl(Moose::Getopt) >= 0.05
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooseX::Types::Path::Class creates common Moose types, coercions and option
specifications useful for dealing with Path::Class objects as Moose attributes.  

Coercions (see Moose::Util::TypeConstraints) are made from both 'Str' and 
'ArrayRef' to both Path::Class::Dir and Path::Class::File objects.  If you
have MooseX::Getopt installed, the Getopt option type ("=s") will be added
for both Path::Class::Dir and Path::Class::File.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-Path-Class-%{version}

# Fix shellbangs in tests
sed -i '1s:^#!.*perl:#!%{__perl}:' t/*.t

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
