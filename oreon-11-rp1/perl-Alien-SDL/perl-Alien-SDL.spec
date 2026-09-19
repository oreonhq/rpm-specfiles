%global source0_hash c9aa2c9dc3c63d89773c7d7203f2a46d1b924d0c72d9f801af147a3dc8bc512a

Name:           perl-Alien-SDL
Version:        1.446
Release:        33%{?dist}
Summary:        Finding and using SDL binaries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-SDL
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/Alien-SDL-%{version}.tar.gz
# Do not set unnecessary rpath, not suitable for an upstream
Patch0:         Alien-SDL-1.446-Do-not-set-rpath-on-Linux.patch
# Place temporary files into a writable location,
# <https://github.com/PerlGameDev/SDL/issues/297>
Patch1:         Alien-SDL-1.446-Place-temporary-files-into-a-writable-location.patch
# Keep full-arch because Alien::SDL::ConfigData stores architecture-specific
# paths.
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Extract)
# Not needed (https://github.com/PerlGameDev/SDL/issues/234):
# Archive::Tar
# Archive::Zip
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch) >= 0.24
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Patch) >= 1.4
BuildRequires:  perl(warnings)
BuildRequires:  sdl12-compat-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_ttf-devel
# Run-time:
BuildRequires:  perl(Capture::Tiny)
# Data::Dumper not used at tests
# Tests only:
BuildRequires:  perl(Test::More)
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

%description
In short Alien::SDL can be used to detect and get configuration settings from 
an installed SDL and related libraries.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# t/002_config.t checks that the optional files cached in
# Alien::SDL::config(ld_shared_libs) exist.
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
# Move Alien::SDL::ConfigData to perl_vendorarch
install -d %{buildroot}%{perl_vendorarch}/Alien
mv %{buildroot}%{perl_vendorlib}/Alien/SDL %{buildroot}%{perl_vendorarch}/Alien
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorarch}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
