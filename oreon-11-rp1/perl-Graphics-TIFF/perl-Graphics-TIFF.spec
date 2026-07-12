%global source0_hash aba8afcc07148df418a2c519e8415deccef6f6c260475e0acc0a4167b31f1119

# Run optional tests
%{bcond_without perl_Graphics_TIFF_enables_optional_test}

Name:           perl-Graphics-TIFF
Version:        21
Release:        7%{?dist}
Summary:        Perl extension for the LibTIFF library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-TIFF
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Graphics-TIFF-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.3
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
%if %{with perl_Graphics_TIFF_enables_optional_test}
# Optional tests:
# ImageMagick for convert executed by t/1.t
BuildRequires:  ImageMagick
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Test::Requires)
%endif

Provides:       perl(Graphics::TIFF)
%description
The Graphics::TIFF module allows a Perl developer to access TIFF images using
LibTIFF library in a Perlish and object-oriented way.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Graphics_TIFF_enables_optional_test}
# Optional tests:
# ImageMagick for convert executed by t/1.t
Requires:       ImageMagick
Requires:       perl(Image::Magick)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -n Graphics-TIFF-%{version}
# Delete author tests skipped by default
for F in t/91_critic.t t/92_tiffinfo.t t/93_tiff2pdf.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
%if !%{with perl_Graphics_TIFF_enables_optional_test}
for F in t/1.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
%endif
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
%if %{with perl_Graphics_TIFF_enables_optional_test}
cp -a examples %{buildroot}/%{_libexecdir}/%{name}
chmod +x %{buildroot}/%{_libexecdir}/%{name}/examples/*
%endif
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%dir %{perl_vendorarch}/auto/Graphics
%{perl_vendorarch}/auto/Graphics/TIFF
%dir %{perl_vendorarch}/Graphics
%{perl_vendorarch}/Graphics/TIFF.pm
%{_mandir}/man3/Graphics::TIFF.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
