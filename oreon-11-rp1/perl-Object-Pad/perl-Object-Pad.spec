%global source0_hash 3fa84943b6505a5bf9f29fe4202d1b75d6c6ae03f531ddea9edc4c13ff93b1a3
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Object_Pad_enables_Devel_MAT
%bcond_without perl_Object_Pad_enables_optional_test
Name:           perl-Object-Pad
Version:        0.825
Release:        1%{?dist}
Summary:        Simple syntax for lexical slot-based objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Pad
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Object-Pad-%{version}.tar.gz
Source1:        macros.perl-Object-Pad
%if %{with perl_Object_Pad_enables_Devel_MAT}
%endif
%define xs_parse_keyword_min_ver 0.47
%define xs_parse_sublike_min_ver 0.35
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
%define future_min_ver 0.49
%define future_asyncawait_min_ver 0.45
%define sublike_externeded_min_ver 0.29
%define syntax_keyword_dynamically_min_ver 0.04
%endif
%if %{with perl_Object_Pad_enables_optional_test} && %{with perl_Object_Pad_enables_Devel_MAT}
%endif
Requires:       perl(experimental)
Requires:       perl(strict)
Requires:       perl(XS::Parse::Keyword) >= %{xs_parse_keyword_min_ver}
%if %{defined perl_XS_Parse_Keyword_ABI}
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Requires:       perl(XS::Parse::Sublike) >= %{xs_parse_sublike_min_ver}
Provides:       perl(:Object_Pad_ABI) = 0.57
Provides:       perl(:Object_Pad_ABI) = 0.76
Provides:       perl(:Object_Pad_ABI) = 0.810
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future::AsyncAwait|Sublike::Extended|Syntax::Keyword::Dynamically)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((91rt141483Role|ARole|BaseClass|Example)\\)
Provides:       perl(Object::Pad)
Provides:       perl(Object::Pad)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Sublike::Extended)
BuildRequires:  perl(Syntax::Keyword::Dynamically)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Require::Perl)
BuildRequires:  perl(Test2::Require::Threads)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XS::Parse::Keyword)
BuildRequires:  perl(XS::Parse::Keyword::Builder)
BuildRequires:  perl(XS::Parse::Sublike)
BuildRequires:  perl(XS::Parse::Sublike::Builder)
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides a simple syntax for creating object classes, which
uses private variables that look like lexical variables for object member
fields.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-ExtensionBuilder = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Config)
Requires:       perl(strict)
Requires:       perl(Sub::Util)
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
Requires:       perl(Future) >= %{future_min_ver}
Requires:       perl(Future::AsyncAwait) >= %{future_asyncawait_min_ver}
Requires:       perl(Sublike::Extended) >= %{sublike_externeded_min_ver}
Requires:       perl(Syntax::Keyword::Dynamically) >= %{syntax_keyword_dynamically_min_ver}
Requires:       perl(Test::MemoryGrowth)
%endif
%if %{with perl_Object_Pad_enables_optional_test} && %{with perl_Object_Pad_enables_Devel_MAT}
%define devel_mat_min_ver 0.53
Requires:       perl(Devel::MAT) >= %{devel_mat_min_ver}
Requires:       perl(Devel::MAT::Dumper)
Requires:       perl(List::Util)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%package ExtensionBuilder
Summary:        Build-time support for Object::Pad plugins
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(Object::Pad)
Requires:       rpm
%description ExtensionBuilder
This package provides a build-time helper to assist the authors in writing XS
plugins for Object::Pad. It prepares a Module::Build-driven distribution to be
able to make use of Object::Pad.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Object-Pad-%{version}
for F in \
%if !%{with perl_Object_Pad_enables_optional_test} || %{defined perl_bootstrap}
    t/08subclass-Moo.t t/80async-method.t t/80dynamically+Object-Pad.t \
    t/80extended+Object-Pad.t t/81async-method+dynamically.t \
    t/90leak.t t/99pod.t \
%endif
%if !%{with perl_Object_Pad_enables_optional_test} || !%{with perl_Object_Pad_enables_Devel_MAT}
    t/82devel-mat-dumper-helper.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E\b}' MANIFEST
done
chmod +x t/*.t

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
%if %{with perl_Object_Pad_enables_optional_test} && !%{defined perl_bootstrap}
rm %{buildroot}/%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Object-Pad-tests -f %{oreon_filedir}/perl-Object-Pad-tests.list
%files -n perl-Object-Pad-ExtensionBuilder -f %{oreon_filedir}/perl-Object-Pad-ExtensionBuilder.list

%changelog

%autochangelog
