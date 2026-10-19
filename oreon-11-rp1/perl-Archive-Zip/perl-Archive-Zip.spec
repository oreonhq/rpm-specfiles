%global source0_hash 984e185d785baf6129c6e75f8eb44411745ac00bf6122fb1c8e822a3861ec650
Name:           perl-Archive-Zip
Version:        1.68
Release:        1%{?dist}
Summary:        Perl library for accessing Zip archives
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND Info-ZIP
URL:            https://metacpan.org/release/Archive-Zip
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter)
Requires:       perl(File::Spec) >= 0.80
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(common\\)
Provides:       perl(Archive::Zip)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  unzip
BuildRequires:  zip
# /oreon:deps
%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.
Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.
Members can be added, removed, extracted, replaced, rearranged, and
enumerated.  They can also be renamed or have their dates, comments,
or other attributes queried or modified.  Their data can be compressed
or uncompressed as needed.  Members can be created from members in
existing Zip files, or from existing directories, files, or strings.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       unzip
Requires:       zip
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n Archive-Zip-%{version}
for F in examples/*.pl; do
    perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{$F})"
done

# Help generators to recognize Perl scripts
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t examples %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Archive-Zip-tests -f %{oreon_filedir}/perl-Archive-Zip-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.68-18
- Import
