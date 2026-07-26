%global source0_hash 8bd7cf1c4ee6952ce8e31c081d184f6de340a481b1ec90db3da88bad194f54ac

Name:           perl-MasonX-Interp-WithCallbacks
Version:        1.20
Release:        4%{?dist}
Summary:        Mason callback support via Params::CallbackRequest
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MasonX-Interp-WithCallbacks
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/MasonX-Interp-WithCallbacks-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Class::Container) >= 0.09
BuildRequires:  perl(HTML::Mason) >= 1.23
BuildRequires:  perl(HTML::Mason::Exceptions)
BuildRequires:  perl(HTML::Mason::Interp)
BuildRequires:  perl(HTML::Mason::MethodMaker)
BuildRequires:  perl(Params::CallbackRequest) >= 1.15
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(base)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Mason::ApacheHandler)
BuildRequires:  perl(HTML::Mason::CGIHandler)
BuildRequires:  perl(Params::Callback)
BuildRequires:  perl(Params::CallbackRequest::Exceptions)
BuildRequires:  perl(Test::More) >= 0.17
# Runtime
Requires:       perl(Class::Container) >= 0.09
Requires:       perl(HTML::Mason) >= 1.23
Requires:       perl(HTML::Mason::MethodMaker)
Requires:       perl(Params::CallbackRequest) >= 1.15

%description
MasonX::Interp::WithCallbacks subclasses HTML::Mason::Interp in order to
provide a Mason callback system built on Params::CallbackRequest. Callbacks
may be either code references provided to the new() constructor, or methods
defined in subclasses of Params::Callback. Callbacks are triggered either
for every request or by specially named keys in the Mason request
arguments, and all callbacks are executed at the beginning of a request,
just before Mason creates and executes the request component stack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MasonX-Interp-WithCallbacks-%{version}

# Silence warning from Pod test
mkdir bin

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorlib}/MasonX/
%{_mandir}/man3/MasonX::Interp::WithCallbacks.3pm*

%changelog
%autochangelog
