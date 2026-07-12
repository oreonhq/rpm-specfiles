%global source0_hash ade3be31c447b8448869fecdfcace258d6d587b8c6c773c5f22735f70d82d6da

# Unbundle Apache-Reload
%{bcond_with mod_perl_enables_bundled_Apache_Reload}
# Run optional test
%{bcond_without mod_perl_enables_optional_test}

%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

%global regenerate_xs 0

Name:           mod_perl
Version:        2.0.13
Release:        12%{?dist}
Summary:        An embedded Perl interpreter for the Apache HTTP Server
# other files:                  ASL 2.0
## Not in binary packages
# docs/os/win32/distinstall:    GPL+ or Artistic
# docs/os/win32/mpinstall:      GPL+ or Artistic
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://perl.apache.org/

Source0:        https://www.apache.org/dist/perl/mod_perl-%{version}.tar.gz
Source1:        https://www.apache.org/dist/perl/mod_perl-%{version}.tar.gz.asc
Source2:        https://www.apache.org/dist/perl/KEYS
Source3:        perl.conf
Source4:        perl.module.conf

# Normalize documentation encoding
Patch0:         mod_perl-2.0.12-Convert-documentation-to-UTF-8.patch
Patch1:         mod_perl-2.0.4-inline.patch
Patch2:         mod_perl-32bit-ftbs.patch

BuildRequires:  lmdb-devel
BuildRequires:  openldap-devel
BuildRequires:  apr-devel >= 1.2.0
BuildRequires:  apr-util-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gnupg2
BuildRequires:  httpd
BuildRequires:  httpd-devel >= 2.4.0
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Module::CoreList not helpful
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Win32 not used
BuildRequires:  sed
%if %{regenerate_xs}0
BuildRequires:  perl(Data::Flow) >= 0.05
BuildRequires:  perl(Tie::IxHash)
%endif
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(base)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
# IO::Dir not used at tests
BuildRequires:  perl(Linux::Pid)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(subs)
# TAP::Formatter::Console not use at tests
# TAP::Harness not used at tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
# Tests:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(locale)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(threads)
BuildRequires:  perl(Test::More)
%if %{with mod_perl_enables_optional_test}
# Optional tests:
BuildRequires:  perl(CGI) >= 2.93
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
%endif

Requires:       httpd-mmn = %{_httpd_mmn}
# For Apache::SizeLimit::Core
Requires:       perl(Linux::Pid)

%{?perl_default_filter}

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Apache2::Connection\\)$
%global __provides_exclude %__provides_exclude|perl\\(Apache2::RequestRec\\)$
%global __provides_exclude %__provides_exclude|perl\\(warnings\\)$
%global __provides_exclude %__provides_exclude|perl\\(HTTP::Request::Common\\)$
%global __provides_exclude %__provides_exclude|mod_perl\\.so\\(.*$
%global __provides_exclude %__provides_exclude|mod_perl\\.so$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Apache::Test.*\\)
%global __requires_exclude %__requires_exclude|perl\\(Data::Flow\\)
%global __requires_exclude %__requires_exclude|perl\\(Apache2::FunctionTable\\)
%global __requires_exclude %__requires_exclude|perl\\(Apache2::StructureTable\\)

# Hide dependencies on broken provides
%global __requires_exclude %__requires_exclude|^perl\\(Apache2::MPM\\)

Provides:       perl(Apache2::Log)
Provides:       perl(Apache2::Log)
Provides:       perl(ModPerl::Util)
%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.
Mod_perl links the Perl run-time library into the Apache web server and
provides an object-oriented Perl interface for Apache's C language
API.  The end result is a quicker CGI script turnaround process, since
no external Perl interpreter has to be started.

Install mod_perl if you're installing the Apache web server and you'd
like for it to directly incorporate a Perl interpreter.


%package devel
Summary:        Files needed for building XS modules that use mod_perl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       httpd-devel%{?_isa}
Requires:       perl(IO::Dir)

%description devel 
The mod_perl-devel package contains the files needed for building XS
modules that use mod_perl.


%if %{with mod_perl_enables_bundled_Apache_Reload}
%package -n perl-Apache-Reload
Version:        0.13
Summary:        Reload changed Perl modules
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
# The mod_perl2 1.99022 is not used, pick for example ModPerl::Util to
# constrain the version.
Requires:       perl(ModPerl::Util) >= 1.99022
Conflicts:      mod_perl < 2.0.10-4
Provides:       bundled(Apache-Reload) = %{version}

# Fiter-underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ModPerl::Util\\)$

%description -n perl-Apache-Reload
This mod_perl extension allows to reload Perl modules that changed on the disk.
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

# Remove docs/os. It's only win32 info with non-ASL-2.0 license. Bug #1199044.
rm -rf docs/os
# Remove bundled Apache-Reload
%if %{without mod_perl_enables_bundled_Apache_Reload}
rm -rf Apache-Reload
sed -i -e '/Apache-Reload/d' Makefile.PL MANIFEST
%endif
# Remove failing tests, CPAN RT#118919, CPAN RT#132919
for F in \
    ModPerl-Registry/t/closure.t \
    ModPerl-Registry/t/special_blocks.t \
    ModPerl-Registry/t/perlrun_extload.t \
    t/filter/in_bbs_inject_header.t \
    t/filter/TestFilter/in_bbs_inject_header.pm \
;do
    rm "$F"
    sed -i -e '\,^'"$F"',d' MANIFEST
done

%build
CFLAGS="$RPM_OPT_FLAGS -fpic" perl Makefile.PL </dev/null \
         PREFIX=$RPM_BUILD_ROOT/%{_prefix} \
         INSTALLDIRS=vendor \
         MP_APXS=%{_httpd_apxs} \
         MP_APR_CONFIG=%{_bindir}/apr-1-config

# This is not needed now when we are using httpd24 branch, but I will keep
# it here in case someone will have to regenerate *.xs files again.
%if %{regenerate_xs}0
%{make_build} source_scan
%{make_build} xs_generate
CFLAGS="$RPM_OPT_FLAGS -fpic" perl Makefile.PL </dev/null \
         PREFIX=$RPM_BUILD_ROOT/%{_prefix} \
         INSTALLDIRS=vendor \
         MP_APXS=%{_httpd_apxs} \
         MP_APR_CONFIG=%{_bindir}/apr-1-config
%endif

%{make_build} -C src/modules/perl OPTIMIZE="$RPM_OPT_FLAGS -fpic"
%{make_build}

%install
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_moddir}
# Not parallel-safe
make install \
    MODPERL_AP_LIBEXECDIR=$RPM_BUILD_ROOT%{_httpd_moddir} \
    MODPERL_AP_INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}/httpd

# Remove files not suitable for distribution.
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name perllocal.pod -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
# Remove empty vendor_perl/auto/mod_perl2 directory.
find $RPM_BUILD_ROOT -depth -type d -empty -delete

# Fix permissions to avoid strip failures on non-root builds.
%{_fixperms} $RPM_BUILD_ROOT/*

# Install the config file
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_confdir}
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_modconfdir}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_httpd_confdir}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_httpd_modconfdir}/02-perl.conf

# Move set of modules to -devel
devmods="ModPerl::Code ModPerl::BuildMM ModPerl::CScan \
          ModPerl::TestRun ModPerl::Config ModPerl::WrapXS \
          ModPerl::BuildOptions ModPerl::Manifest \
          ModPerl::MapUtil ModPerl::StructureMap \
          ModPerl::TypeMap ModPerl::FunctionMap \
          ModPerl::ParseSource ModPerl::MM \
          Apache2::Build Apache2::ParseSource Apache2::BuildConfig \
          Bundle::ApacheTest"
for m in $devmods; do
   test -f $RPM_BUILD_ROOT%{_mandir}/man3/${m}.3pm &&
     echo "%{_mandir}/man3/${m}.3pm*"
   fn=${m//::/\/}
   test -f $RPM_BUILD_ROOT%{perl_vendorarch}/${fn}.pm &&
        echo %{perl_vendorarch}/${fn}.pm
   test -d $RPM_BUILD_ROOT%{perl_vendorarch}/${fn} && 
        echo %{perl_vendorarch}/${fn}
   test -d $RPM_BUILD_ROOT%{perl_vendorarch}/auto/${fn} && 
        echo %{perl_vendorarch}/auto/${fn}
done | tee devel.files | sed 's/^/%%exclude /' > exclude.files
echo "%%exclude %{_mandir}/man3/Apache::Test*.3pm*" >> exclude.files

# perl build script generates *.orig files, they get installed and later they
# break provides so mod_perl requires mod_perl-devel. We remove them here.
find "$RPM_BUILD_ROOT" -type f -name *.orig -delete

%check
make test TEST_VERBOSE=1 && RETVAL=$?
if test "$RETVAL" != 0; then
    # Echo both error_log files if make test returns failure.
    echo BEGIN t/logs/error_log
    cat t/logs/error_log
    echo END t/logs/error_log

    echo BEGIN ModPerl-Registry/t/logs/error_log
    cat ModPerl-Registry/t/logs/error_log
    echo END ModPerl-Registry/t/logs/error_log

    exit 1
fi

%files -f exclude.files
%license LICENSE
%doc Changes CONTRIBUTING.md NOTICE README* STATUS SVN-MOVE docs/
%config(noreplace) %{_httpd_confdir}/perl.conf
%config(noreplace) %{_httpd_modconfdir}/02-perl.conf
%{_bindir}/*
%{_httpd_moddir}/mod_perl.so
%{perl_vendorarch}/auto/*
%dir %{perl_vendorarch}/Apache/
%{perl_vendorarch}/Apache/SizeLimit*
%{perl_vendorarch}/Apache2/
%exclude %{perl_vendorarch}/Apache2/Reload.pm
%{perl_vendorarch}/Bundle/
%{perl_vendorarch}/APR/
%{perl_vendorarch}/ModPerl/
%{perl_vendorarch}/*.pm
%{_mandir}/man3/*.3*
%exclude %{_mandir}/man3/Apache::Reload.3pm*
%exclude %{_mandir}/man3/Apache2::Reload.3pm*

%files devel -f devel.files
%{_includedir}/httpd/*
%{perl_vendorarch}/Apache/Test*.pm
%{_mandir}/man3/Apache::Test*.3pm*

%if %{with mod_perl_enables_bundled_Apache_Reload}
%files -n perl-Apache-Reload
%dir %{perl_vendorarch}/Apache/
%{perl_vendorarch}/Apache/Reload.pm
%dir %{perl_vendorarch}/Apache2/
%{perl_vendorarch}/Apache2/Reload.pm
%{_mandir}/man3/Apache::Reload.3pm*
%{_mandir}/man3/Apache2::Reload.3pm*
%endif

%changelog
%autochangelog
