%global source0_hash 40c85c8be10a54994ff3f70daea5e56b62c2ee508b75ab714e7d948db1877480

%global pkgname Text-Xslate

Name:           perl-%{pkgname}
Version:        3.5.9
Release:        15%{?dist}
Summary:        Scalable template engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://xslate.org/
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/%{pkgname}-v%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Module::Build::XSUtil)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::MessagePack) >= 0.38
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mouse) >= 2.5.0
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader) >= 0.02
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Devel::StackTrace) >= 1.30
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Plack) >= 0.99
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(SelectSaver)
# Template not used
BuildRequires:  perl(Template::Plugin::Math)
BuildRequires:  perl(Template::Plugin::String)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(utf8)
Requires:       perl(B)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::MessagePack) >= 0.38
Requires:       perl(Digest::MD5)
Requires:       perl(Encode) >= 2.26
Requires:       perl(File::Path)
Requires:       perl(Mouse) >= 2.5.0
Requires:       perl(parent) >= 0.221
Requires:       perl(Scalar::Util) >= 1.14
Requires:       perl(XSLoader) >= 0.02

# Filter under-specified Symbols
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::MessagePack|Mouse|parent|Scalar::Util)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Text::Xslate\\)$

%description
Xslate is a template engine, tuned for persistent applications, safe as an
HTML generator, and with rich features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-v%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes example HACKING
%{_bindir}/xslate
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man1/xslate.1*
%{_mandir}/man3/*

%changelog
%autochangelog
