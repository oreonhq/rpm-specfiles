%global source0_hash 14a3704ebc755b8afc980975968160e36e8b682ec0ca4bf1bddb585232e28a10
Name:           perl-Params-CallbackRequest
Version:        1.20
Release:        1%{?dist}
Summary:        Functional and object-oriented callback architecture
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Params-CallbackRequest
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/Params-CallbackRequest-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Attribute::Handlers) >= 0.77
Requires:       perl(Carp)
Requires:       perl(Class::ISA)
Requires:       perl(Exception::Class) >= 1.10
Requires:       perl(Params::Validate) >= 0.59
%global __requires_exclude ^perl\\((Exception::Class|Params::Validate)\\)$
# oreon:deps
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
Params::CallbackRequest provides functional and object-oriented callbacks
to method and function parameters. Callbacks may be either code references
provided to the new() constructor, or methods defined in subclasses of
Params::Callback. Callbacks are triggered either for every call to the
Params::CallbackRequest request() method, or by specially named keys in the
parameters to request().

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Params-CallbackRequest-%{version}

# Avoid spurious warning from Test::Pod
mkdir bin

%build

perl Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
