%global source0_hash fcf21ddcc6bae0d367236058badabd3b37240d3e5ead3630541281606d172cf2

Name:           perl-Geo-ShapeFile
Version:        3.03
Release:        8%{?dist}
Summary:        Perl extension for handling ESRI GIS Shapefiles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Geo-ShapeFile
Source0:        https://cpan.metacpan.org/modules/by-module/Geo/Geo-ShapeFile-%{version}.tar.gz
# Remove rlib dependency from test suite as rlib is not available in Fedora and does not have a license
Patch1:         geo_shapefile_remove_rlib.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(autovivification)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig) >= 1.04
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tree::R)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Geo::ShapeFile::TestHelpers\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
The Geo::ShapeFile module reads ESRI ShapeFiles containing GIS mapping
data, it has support for shp (shape), shx (shape index), and dbf (data
base) formats.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-ShapeFile-%{version}
%patch -P1 -p1
perl -pi -e 's|\r||g' lib/Geo/ShapeFile.pm lib/Geo/ShapeFile/Shape/Index.pm lib/Geo/ShapeFile/Shape.pm lib/Geo/ShapeFile/Point.pm
perl -pi -e 's|\r||g' Changes README
perl -pi -e 's|\r||g' eg/shpdump.pl
perl -MConfig -pi -e 's|^#!.*/bin/perl\b|$Config{startperl}|' eg/shpdump.pl

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
