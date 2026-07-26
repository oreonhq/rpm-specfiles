%global source0_hash 6297a9001a1b2acf6a2e34ea4d814e2b28ffe40131b48fcfe36391f3d844e70d

Name:           perl-Mojolicious-Plugin-AssetPack
Version:        2.15
Release:        4%{?dist}
Summary:        Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojolicious-Plugin-AssetPack
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-Plugin-AssetPack-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(CSS::Minifier::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Imager::File::PNG)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(JavaScript::Minifier::XS)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::ByteStream)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Types)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(overload)
BuildRequires:  perl(warnings)
Requires:       perl(Imager::File::PNG)
Requires:       perl(Mojo::UserAgent)

%{?perl_default_filter}

%description
Mojolicious::Plugin::AssetPack is a Mojolicious plugin which can be used to
cram multiple assets of the same type into one file. This means that if you
have a lot of CSS files (.css, .less, .sass, ...) as input, the AssetPack
can make one big CSS file as output. This is good, since it will often
speed up the rendering of your page. The output file can even be minified,
meaning you can save bandwidth and browser parsing time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojolicious-Plugin-AssetPack-%{version}
for PL in not-found.pl sprites.pl rollup.pl; do
    /usr/bin/sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' examples/"$PL"
done
/usr/bin/sed -i -e '1s,#!.*node,,' lib/Mojolicious/Plugin/AssetPack/Pipe/*.js

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes examples README.md
%{perl_vendorlib}/Mojolicious*
%{_mandir}/man3/Mojolicious*

%changelog
%autochangelog
