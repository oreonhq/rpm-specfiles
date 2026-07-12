%global source0_hash f805953a08c57846a16a4d85d7b766398afaf7c36c1465fcb1dea09e5fa394db

# Perform optional tests
%if 0%{?rhel}
%bcond_with perl_Const_Fast_enables_optional_test
%else
%bcond_without perl_Const_Fast_enables_optional_test
%endif

Name:           perl-Const-Fast
Version:        0.014
Release:        37%{?dist}
Summary:        Facility for creating read-only scalars, arrays, and hashes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Const-Fast
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Const-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Module::Build::Tiny) >= 0.021
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001007
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Const_Fast_enables_optional_test}
# Optional tests
# Pod::Coverage::TrustPod not used
# Test::Pod not used
# Test::Pod::Coverage not used
BuildRequires:  perl(Test::Script) >= 1.05
%endif

%{?perl_default_filter}

Provides:       perl(Const::Fast)
%description
This the only function of this module and it is exported by default. It takes
a scalar, array or hash left-value as first argument, and a list of one or
more values depending on the type of the first argument as the value for the
variable. It will set the variable to that value and subsequently make it
read-only. Arrays and hashes will be made deeply read-only.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Const-Fast-%{version}


%build
perl Build.PL --installdirs vendor
./Build


%install
./Build install --destdir $RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*


%check
unset RELEASE_TESTING
./Build test


%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Const
%{perl_vendorlib}/Const/Fast.pm
%{_mandir}/man3/Const::Fast.*


%changelog
%autochangelog
