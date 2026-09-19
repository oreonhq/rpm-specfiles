%global source0_hash 252a192bfa9c2070a4883707d139c3a45d9c4518ccd66a1e699b5b7959bd4fb5

Name:           perl-SDL
Version:        2.548
Release:        32%{?dist}
Summary:        Simple DirectMedia Layer for Perl
# COPYING:                      GPL-2.0 text
# lib/pods/SDL.pod:             GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Platform.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial/Animation.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial/LunarLander.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Layer.pod:          GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/LayerManager.pod:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Music.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Rect.pod:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/SFont.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Sound.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Text.pod:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/SDL.pm:                       LGPL-2.1-or-later
# lib/SDL_perl.pm:                  LGPL-2.1-or-later
# lib/SDL/SMPEG/Info.pm:            LGPL-2.1-or-later
# lib/SDL/TTFont.pm:                LGPL-2.1-or-later
# lib/SDL/Tutorial.pm:              LGPL-2.1-or-later
# lib/SDL/Tutorial/Animation.pm:    LGPL-2.1-or-later
# src/defines.h:        LGPL-2.1-or-later
# src/ppport.h:         GPL-1.0-or-later OR Artistic-1.0-Perl
# src/SDL.xs:           LGPL-2.1-or-later
# src/SDLx/SFont.h:     LGPL-2.1-or-later
# src/SDLx/SFont.xs:    LGPL-2.1-or-later
# test/data/5x7.fnt:        LGPL-2.1-only (see test/data/README)
# test/data/tribe_i.wav:    GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0
#                           (see test/data/README; there is a typo in the file
#                           name)
## Used at build-time, but not in any binary package
# Build.PL:                 refers to LGPL
# inc/My/Builder.pm:        LGPL-2.1-or-later
## Not in any binary package and not used
# META.json:    refers to LGPL-2.1
# OFL.txt:      OFL-1.1-RFN text
## Unbundled:
# share/GenBasR.ttf:    OFL-1.1-RFN
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND LGPL-2.1-only AND (GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0) AND OFL-1.1-RFN
URL:            http://sdl.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/SDL-%{version}.tar.gz
# Fix an implicit function declaration, in upstream after 2.548,
# bug #2177189, <https://github.com/PerlGameDev/SDL/pull/299>.
Patch0:         SDL-2.548-Fix-implicit-declaration-of-_calc_offset.patch
# Unbundle Gentium Book Basic font, not suitable for the upstream, the file is
# deleted in %%prep section.
Patch1:         SDL-2.548-Unbundle-Gentium-Book-Basic-regular-font.patch
# Adapt to perl 5.37.1, in upstream after 2.548,
# <https://github.com/PerlGameDev/SDL/issues/303>
Patch2:         SDL-2.548-Adapt-to-perl-5.37.1.patch
# Fix reference counting an event filter callback, bug #2272636,
# in upstream after 2.548, <https://github.com/PerlGameDev/SDL/pull/308>
Patch3:         SDL-2.548-Fix-reference-counting-in-set_event_filter.patch
# Adapt to GCC 15, bug #2341036,
# <https://github.com/PerlGameDev/SDL/issues/294>, in upstream after 2.548,
# <https://github.com/PerlGameDev/SDL/pull/309>
Patch4:         SDL-2.548-Fix-building-in-ISO-C23.patch
# Adapt t/core_surface.t test to SDL3, incompatible with SDL2, bug #2341036,
# proposed to upstream, <https://github.com/PerlGameDev/SDL/pull/310>
Patch5:         SDL-2.548-core_surface.t-test-data-icon.bmp-is-really-4-bits-p.patch
# Adapt t/core.t test to SDL-3.2.24, bug #2401791, proposed upstream,
# <https://github.com/PerlGameDev/SDL/pull/311>
Patch6:         SDL-2.548-Adapt-to-SDL-3.2.24.patch
# Make the tests read-only, proposed upstream,
# <https://github.com/PerlGameDev/SDL/pull/312>
Patch7:         SDL-2.548-Read-only-t-core_rwops.t.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::SDL) >= 1.446
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# ExtUtils::CBuilder::Base not used at tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  sil-gentium-basic-book-fonts
# Tests:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most) >= 0.21
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       sil-gentium-basic-book-fonts

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Most\\)$
# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(SDL::TestTool\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(SDL::TestTool\\)

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream
cp -a t test %{buildroot}%{_libexecdir}/%{name}/upstream
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name}/upstream && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%files
%license COPYING
%doc CHANGELOG TODO
%{perl_vendorarch}/auto/SDL
%{perl_vendorarch}/auto/SDL_perl
%{perl_vendorarch}/auto/SDLx
%{perl_vendorarch}/SDL
%{perl_vendorarch}/SDL.pm
%{perl_vendorarch}/SDL.pod
%{perl_vendorarch}/SDL_perl.pm
%{perl_vendorarch}/SDLx
%{_mandir}/man3/SDL.*
%{_mandir}/man3/SDL::*
%{_mandir}/man3/SDLx::*

%files -n perl-Module-Build-SDL
%dir %{perl_vendorarch}/Module
%dir %{perl_vendorarch}/Module/Build
%{perl_vendorarch}/Module/Build/SDL.pm
%{_mandir}/man3/Module::Build::SDL.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
