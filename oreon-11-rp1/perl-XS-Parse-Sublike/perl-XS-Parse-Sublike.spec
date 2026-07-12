%global source0_hash a10f5e07273b105e5c0b4c6e7e2a6d2d2a68afe9ff4f989c11f38d4bf39cc86d

# Perform optional tests
%if 0%{?rhel}
%bcond_with perl_XS_Parse_Sublike_enables_optional_tests
%else
%bcond_without perl_XS_Parse_Sublike_enables_optional_tests
%endif

# Break a build cycle with perl-Object-Pad
%if %{with perl_XS_Parse_Sublike_enables_optional_tests} && !%{defined perl_bootstrap}
%global optional_tests 1
%else
%global optional_tests 0
%endif

Name:           perl-XS-Parse-Sublike
Version:        0.41
Release:        2%{?dist}
Summary:        XS functions to assist in parsing sub-like syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XS-Parse-Sublike
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Sublike-%{version}.tar.gz
Source1:        macros.perl-XS-Parse-Sublike
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# File::ShareDir 1.00 not used at tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(feature)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0) >= 0.000147
%if %{optional_tests}
# Optional tests:
%global Future_AsyncAwait_min_ver 0.66
BuildRequires:  perl(Future::AsyncAwait) >= %{Future_AsyncAwait_min_ver}
%global Object_Pad_min_ver 0.800
BuildRequires:  perl(Object::Pad) >= %{Object_Pad_min_ver}
BuildRequires:  perl(Test::Pod) >= 1
%endif
# This module maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_sublike() compiled into the users of this module.
# This ABI range is defined with XS::Parse::Sublike/ABIVERSION_MIN and
# XS::Parse::Sublike/ABIVERSION_MAX in lib/XS/Parse/Sublike.xs.
Provides:       perl(:XS_Parse_Sublike_ABI) = 5
Provides:       perl(:XS_Parse_Sublike_ABI) = 6
Provides:       perl(:XS_Parse_Sublike_ABI) = 7
Provides:       perl(:XS_Parse_Sublike_ABI) = 8

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future::AsyncAwait|Object::Pad)\\)$
# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(testcase\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(testcase\\)

Provides:       perl(Sublike::Extended)
Provides:       perl(XS::Parse::Sublike)
Provides:       perl(XS::Parse::Sublike::Builder)
Provides:       perl(XS::Parse::Sublike)
Provides:       perl(XS::Parse::Sublike::Builder)
%description
This module provides some XS functions to assist in writing parsers for
sub-like syntax, primarily for authors of keyword plugins using the
PL_keyword_plugin hook mechanism.

%package Builder
Summary:        Build-time support for XS::Parse::Sublike
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(XS::Parse::Sublike)
# Subpackaged in 0.13
Conflicts:      %{name}%{?_isa} < 0.13

%description Builder
This module provides a build-time helper to assist authors writing XS modules
that use XS::Parse::Sublike. It prepares a Module::Build-using distribution to
be able to make use of XS::Parse::Sublike.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(XSLoader)
%if %{optional_tests}
# Optional tests:
Requires:       perl(Future::AsyncAwait) >= %{Future_AsyncAwait_min_ver}
Requires:       perl(Object::Pad) >= %{Object_Pad_min_ver}
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n XS-Parse-Sublike-%{version}
%if !%{optional_tests}
for F in t/80extended+async.t t/80extended+Object-Pad.t t/99pod.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
# Build object files for tests now. They are installed into tests subpackage.
./Build testlib

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
find %{buildroot}%{_libexecdir}/%{name} -type f \
    \( -name '*.bs' -o -name '*.c' -o -name '*.o' \) -delete
%if %{optional_tests}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/XS
%dir %{perl_vendorarch}/auto/XS/Parse
%{perl_vendorarch}/auto/XS/Parse/Sublike
%dir %{perl_vendorarch}/Sublike
%{perl_vendorarch}/Sublike/Extended.pm
%dir %{perl_vendorarch}/XS
%dir %{perl_vendorarch}/XS/Parse
%{perl_vendorarch}/XS/Parse/Sublike.pm
%{_mandir}/man3/Sublike::Extended.*
%{_mandir}/man3/XS::Parse::Sublike.*

%files Builder
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/module
%{perl_vendorarch}/auto/share/module/XS-Parse-Sublike
%{perl_vendorarch}/XS/Parse/Sublike
%{_mandir}/man3/XS::Parse::Sublike::*
%{_rpmmacrodir}/macros.%{name}

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
