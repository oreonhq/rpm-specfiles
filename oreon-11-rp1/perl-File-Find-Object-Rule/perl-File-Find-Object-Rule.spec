%if ! (0%{?rhel})
%{bcond_without perl_File_Find_Object_Rule_enables_optional_test}
%else
%{bcond_with perl_File_Find_Object_Rule_enables_optional_test}
%endif

Name:           perl-File-Find-Object-Rule
Version:        0.0313
Release:        12%{?dist}
Summary:        Alternative interface to File::Find::Object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Object-Rule
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-Rule-0.0313.tar.gz

Patch0:         File-Find-Object-Rule-0.0310-shellbang.patch
# oreon url source checksums begin
%global source0_sha256 81940f299d6487248fbf30d8f1fb7df6c6a34b3df9440a5621b135c8e34fcff2
%global source0_file File-Find-Object-Rule-0.0313.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.28
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find::Object)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Script Runtime
BuildRequires:  perl(File::Spec::Functions)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
File::Find::Object::Rule is a friendlier interface to File::Find::Object. It 
allows you to build rules that specify the desired files and directories.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Find-Object-Rule-0.0313.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "81940f299d6487248fbf30d8f1fb7df6c6a34b3df9440a5621b135c8e34fcff2" || { echo "oreon: Source0 SHA256 mismatch for File-Find-Object-Rule-0.0313.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -qn File-Find-Object-Rule-%{version}

# Avoid use of /usr/bin/env
%patch -P 0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes Changes.F-F-R README
%{_bindir}/findorule
%{perl_vendorlib}/File/
%{_mandir}/man1/findorule.1*
%{_mandir}/man3/File::Find::Object::Rule.3*
%{_mandir}/man3/File::Find::Object::Rule::Extending.3*
%{_mandir}/man3/File::Find::Object::Rule::Procedural.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0313-12
- Prepare for Oreon 11 (RP1)
