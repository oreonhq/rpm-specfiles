%global source0_hash c9aa2c9dc3c63d89773c7d7203f2a46d1b924d0c72d9f801af147a3dc8bc512a
Name:           perl-Alien-SDL
Version:        1.446
Release:        1%{?dist}
Summary:        Finding and using SDL binaries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-SDL
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/Alien-SDL-%{version}.tar.gz
Patch0:         Alien-SDL-1.446-Do-not-set-rpath-on-Linux.patch
Patch1:         Alien-SDL-1.446-Place-temporary-files-into-a-writable-location.patch
%global debug_package %{nil}
Requires:       perl(Data::Dumper)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Module::Build)
Requires:       sdl12-compat-devel
Suggests:       SDL_gfx-devel
Suggests:       SDL_image-devel
Suggests:       SDL_mixer-devel
Suggests:       SDL_Pango-devel
Suggests:       SDL_ttf-devel
%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(File::ShareDir\\)$
# oreon:deps
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  coreutils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Patch)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sdl12-compat-devel
# /oreon:deps
%description
In short Alien::SDL can be used to detect and get configuration settings from 
an installed SDL and related libraries.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       SDL_gfx-devel
Requires:       SDL_image-devel
Requires:       SDL_mixer-devel
Requires:       SDL_Pango-devel
Requires:       SDL_ttf-devel
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Alien-SDL-%{version}
rm t/release-pod-*
perl -i -ne 'print $_ unless m{\At/release-pod-}' MANIFEST

%build

perl Build.PL installdirs=vendor --travis
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
install -d %{buildroot}%{perl_vendorarch}/Alien
mv %{buildroot}%{perl_vendorlib}/Alien/SDL %{buildroot}%{perl_vendorarch}/Alien
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-SDL-tests -f %{oreon_filedir}/perl-Alien-SDL-tests.list

%changelog

%autochangelog
