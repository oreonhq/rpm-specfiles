%global source0_hash 228d4b4f3f0ed9547278691d0b7c5fe53d90874a69df709a49703c6af87c09de
Name:		perl-MouseX-Types-Path-Class
Summary:        A Path::Class type library for Mouse
Version:	0.07
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-Types-Path-Class
Source0:        https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-Types-Path-Class-%{version}.tar.gz
Patch0:		MouseX-Types-Path-Class-0.07-hunspell.patch
BuildArch:	noarch
Requires:	perl(Mouse) >= 0.39
Requires:	perl(MouseX::Getopt) >= 0.22
Requires:	perl(MouseX::Types) >= 0.02
%global __requires_exclude ^perl\\(MouseX::Types\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  hunspell-en
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(MouseX::Getopt)
BuildRequires:  perl(MouseX::Types)
BuildRequires:  perl(MouseX::Types::Mouse)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MouseX::Types::Path::Class creates common Mouse types, coercions and option
specifications useful for dealing with Path::Class objects as Mouse attributes.

Coercions (see Mouse::Util::TypeConstraints) are made from both Str and
ArrayRef to both Path::Class::Dir and Path::Class::File objects. If you have
MouseX::Getopt installed, the Getopt option type ("=s") will be added for both
Path::Class::Dir and Path::Class::File.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-Types-Path-Class-%{version}

# Add support for hunspell speller
%patch -P 0

# Unbundle inc::Module::Install; we'll use the system version instead
rm -rf inc/
perl -ni -e 'print unless /^inc\//;' MANIFEST

# Avoid the need for Module::Install::AuthorRequires and
# all of upstream's toolchain modules as a result of the unbundling
perl -ni -e 'print unless /author_requires/;' Makefile.PL

# F19's dictionary doesn't have coercions
echo coercions >> xt/03_podspell.t

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test TEST_POD=1 TEST_VERBOSE=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
