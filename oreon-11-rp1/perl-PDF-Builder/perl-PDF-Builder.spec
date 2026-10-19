%global source0_hash 62c5d1b7481b7b3c12c589244316b13e5cab179f6685be80840b5d0487975a8c
%bcond_without perl_PDF_Builder_enables_html
%bcond_without perl_PDF_Builder_enables_markdown
%bcond_without perl_PDF_Builder_enables_optional_test
%bcond_without perl_PDF_Builder_enables_png
%bcond_without perl_PDF_Builder_enables_svg
%bcond_without perl_PDF_Builder_enables_tiff
Name:           perl-PDF-Builder
Version:        3.028
Release:        1%{?dist}
Summary:        Creation and modification of PDF files in Perl
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND MIT
URL:            https://metacpan.org/release/PDF-Builder
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMPERRY/PDF-Builder-%{version}.tar.gz
Patch0:         PDF-Builder-3.024-Don-t-skip-ghostscript-9.56.-0-1.patch
BuildArch:      noarch
%if %{with perl_PDF_Builder_enables_tiff}
%endif
%if %{with perl_PDF_Builder_enables_html}
%endif
%if %{with perl_PDF_Builder_enables_png}
%endif
%if %{with perl_PDF_Builder_enables_svg}
%endif
%if %{with perl_PDF_Builder_enables_markdown}
%endif
%if %{with perl_PDF_Builder_enables_optional_test}
%endif
Requires:       perl(Compress::Zlib) >= 1
%if %{with perl_PDF_Builder_enables_tiff}
Recommends:     perl(Graphics::TIFF) >= 19
%endif
%if %{with perl_PDF_Builder_enables_html}
Recommends:     perl(HTML::TreeBuilder) >= 5.07
%endif
%if %{with perl_PDF_Builder_enables_png}
Recommends:     perl(Image::PNG::Const)
Recommends:     perl(Image::PNG::Libpng) >= 0.57
%endif
%if %{with perl_PDF_Builder_enables_svg}
Recommends:     perl(SVGPDF) >= 0.087
%endif
%if %{with perl_PDF_Builder_enables_markdown}
Recommends:     perl(Text::Markdown) >= 1.000031
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Compress::Zlib|Test::Memory::Cycle)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Graphics::TIFF\\)|Image::PNG::)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  coreutils
BuildRequires:  font(dejavusans)
BuildRequires:  ghostscript
BuildRequires:  libtiff-tools
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Font::TTF::Font)
BuildRequires:  perl(GD)
BuildRequires:  perl(Graphics::TIFF)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Image::PNG::Const)
BuildRequires:  perl(Image::PNG::Libpng)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(SVGPDF)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  urw-base35-gothic-fonts
# /oreon:deps
%description
This Perl library enables you to create, import and modify documents in
Portagble Document Format (mostly compliant to PDF 1.4 version).

%package tests
Summary:        Tests for %{name}
License:        LGPL-2.1-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Memory::Cycle) >= 1
%if %{with perl_PDF_Builder_enables_svg}
Requires:       perl(SVGPDF) >= 0.091
%endif
%if %{with perl_PDF_Builder_enables_optional_test}
Requires:       font(dejavusans)
Requires:       ghostscript >= 9.25.0
Requires:       ImageMagick >= 6.9.7
Requires:       libtiff-tools
Requires:       perl(GD)
Requires:       urw-base35-gothic-fonts
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n PDF-Builder-%{version}
# Remove disabled features
for F in \
%if !%{with perl_PDF_Builder_enables_optional_test}
    t/gd.t \
%endif
;do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Correct EOLs
perl -i -pe 's/\r$//' Changes CONTRIBUTING.md INFO/ACKNOWLEDGE.md \
    INFO/Changes_2021 INFO/Changes_2023 INFO/Prereq_fixes.md INFO/SPONSORS \
    README.md
# Help generators to recognize Perl scripts
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-all-usable.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PDF-Builder-tests -f %{oreon_filedir}/perl-PDF-Builder-tests.list

%changelog

%autochangelog
