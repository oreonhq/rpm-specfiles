%global source0_hash 252a192bfa9c2070a4883707d139c3a45d9c4518ccd66a1e699b5b7959bd4fb5
Name:           perl-SDL
Version:        2.548
Release:        1%{?dist}
Summary:        Simple DirectMedia Layer for Perl
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND LGPL-2.1-only AND (GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0) AND OFL-1.1-RFN
URL:            http://sdl.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/SDL-%{version}.tar.gz
Patch0:         SDL-2.548-Fix-implicit-declaration-of-_calc_offset.patch
Patch1:         SDL-2.548-Unbundle-Gentium-Book-Basic-regular-font.patch
Patch2:         SDL-2.548-Adapt-to-perl-5.37.1.patch
Patch3:         SDL-2.548-Fix-reference-counting-in-set_event_filter.patch
Patch4:         SDL-2.548-Fix-building-in-ISO-C23.patch
Patch5:         SDL-2.548-core_surface.t-test-data-icon.bmp-is-really-4-bits-p.patch
Patch6:         SDL-2.548-Adapt-to-SDL-3.2.24.patch
Patch7:         SDL-2.548-Read-only-t-core_rwops.t.patch
Requires:       sil-gentium-basic-book-fonts
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Most\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(SDL::TestTool\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(SDL::TestTool\\)
# oreon:deps
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl(Alien::SDL)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  sil-gentium-basic-book-fonts
# /oreon:deps
%description
SDL_perl is a package of Perl modules that provide both functional and
object oriented interfaces to the Simple DirectMedia Layer for Perl 5. This
package takes some liberties with the SDL API, and attempts to adhere to
the spirit of both the SDL and Perl.

%package -n perl-Module-Build-SDL
Summary:        Module::Build subclass for building SDL applications
License:        LGPL-2.1-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(ExtUtils::CBuilder::Base)
%description -n perl-Module-Build-SDL
Module::Build::SDL is a subclass of Module::Build created to make easy
some tasks specific to SDL applications - e.g. packaging SDL
application/game into PAR archive.

%package tests
Summary:        Tests for %{name}
License:        LGPL-2.1-or-later AND (GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0)
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Most) >= 0.21
Requires:       sil-gentium-basic-book-fonts
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SDL-%{version}
# Delete a bundled font file, code removed with
# Unbundle-Gentium-Book-Basic-regular-font.patch.
rm -r share
# Move the pod files directly to directory lib to have correctly generated
# man pages without prefix pods::
cd lib/pods
find * -type d -exec mkdir -p ../{} \;
find * -type f -exec mv {} ../{} \;
cd ..
rm -r pods
cd ..
sed -i -e 's|lib/pods|lib|' MANIFEST
# Disable the sdlx_controller_interface.t test, it hangs on arm
rm t/sdlx_controller_interface.t
sed -i -e '/t\/sdlx_controller_interface\.t/d' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream
cp -a t test %{buildroot}%{_libexecdir}/%{name}/upstream
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name}/upstream && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Module-Build-SDL usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Build-SDL -f %{oreon_filedir}/perl-Module-Build-SDL.list
%files -n perl-SDL-tests -f %{oreon_filedir}/perl-SDL-tests.list

%changelog

%autochangelog
