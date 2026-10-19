%global source0_hash 81940f299d6487248fbf30d8f1fb7df6c6a34b3df9440a5621b135c8e34fcff2
%{bcond_with perl_File_Find_Object_Rule_enables_optional_test}
Name:           perl-File-Find-Object-Rule
Version:        0.0313
Release:        1%{?dist}
Summary:        Alternative interface to File::Find::Object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Object-Rule
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Find-Object-Rule-%{version}.tar.gz
Patch0:         File-Find-Object-Rule-0.0310-shellbang.patch
BuildArch:      noarch
Provides:       perl(File::Find::Object::Rule)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find::Object)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
File::Find::Object::Rule is a friendlier interface to File::Find::Object. It 
allows you to build rules that specify the desired files and directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qn File-Find-Object-Rule-%{version}

# Avoid use of /usr/bin/env
%patch -P 0

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0313-12
- Prepare for Oreon 11 (RP1)
