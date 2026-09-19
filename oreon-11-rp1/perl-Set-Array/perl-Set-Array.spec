%global source0_hash d9f024c8e3637feccdebcf6479b6754b6c92f1209f567feaf0c23818af31ee3c

Name:           perl-Set-Array
Version:        0.30
Release:        35%{?dist}
Summary:        Arrays as objects with lots of handy methods
License:        Artistic-2.0
URL:            https://metacpan.org/release/Set-Array
Source0:        https://cpan.metacpan.org/modules/by-module/Set/Set-Array-%{version}.tgz
Patch0:         Set-Array-0.30-utf8.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(attributes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Want)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
Set::Array allows you to create arrays as objects and use OO-style methods
on them. Many convenient methods are provided here that appear in the
FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc. In addition,
there are Set methods with corresponding (overloaded) operators for the
purpose of Set comparison, i.e. +, ==, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Set-Array-%{version}

# Fix documentation character encoding
%patch -P 0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Set/
%{_mandir}/man3/Set::Array.3*

%changelog
%autochangelog
