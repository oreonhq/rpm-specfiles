%global source0_hash a7a87333f8d8fb08670acb51b495893c83b28b8e010e3bdce50fe9231f4438ea
Name:           perl-Text-Haml
Version:        0.990118
Release:        1%{?dist}
Summary:        Haml Perl implementation
License:        Artistic-2.0
URL:            https://metacpan.org/release/Text-Haml
Source0:        https://cpan.metacpan.org/authors/id/V/VT/VTI/Text-Haml-%{version}.tar.gz
%bcond_with pod_tests
BuildArch:      noarch
%if %{with pod_tests}
%endif
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Text::Haml implements the Haml 
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html
specification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Haml-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{?with_pod_tests:TEST_POD=1} ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
