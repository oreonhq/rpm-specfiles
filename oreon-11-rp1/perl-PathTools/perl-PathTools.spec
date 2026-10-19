%global source0_hash a558503aa6b1f8c727c0073339081a77888606aa701ada1ad62dd9d8c3f945a2
%global base_version 3.75
Name:           perl-PathTools
Version:        3.94
Release:        1%{?dist}
Summary:        PathTools Perl module (Cwd, File::Spec)
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND BSD-3-Clause
URL:            https://metacpan.org/release/PathTools
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/PathTools-3.75.tar.gz
Patch0:         PathTools-3.74-Disable-VMS-tests.patch
Patch1:         PathTools-3.75-Upgrade-to-3.78.patch
Patch2:         PathTools-3.78-Upgrade-to-3.80.patch
Patch3:         PathTools-3.80-Upgrade-to-3.84.patch
Patch4:         PathTools-3.84-Upgrade-to-3.89.patch
Patch5:         PathTools-3.89-Upgrade-to-3.91.patch
Patch6:         PathTools-3.91-Upgrade-to-3.94.patch
Requires:       perl(Carp)
Requires:       perl(Errno)
Requires:       perl(Scalar::Util)
Recommends:     perl(XSLoader)
%{?perl_default_filter}
Provides:       perl(File::Spec::Functions)
Provides:       perl(File::Spec::Unix)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is the combined distribution for the File::Spec and Cwd modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n PathTools-%{base_version}

# Do not distribute File::Spec::VMS as it works on VMS only (bug #973713)
rm lib/File/Spec/VMS.pm
#perl -i -ne 'print $_ unless m{^\Qlib/File/Spec/VMS.pm\E}' MANIFEST

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe "s#qr{blib}#qr{%{perl_vendorarch}}#" %{buildroot}%{_libexecdir}/%{name}/t/cwd.t
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

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PathTools-tests -f %{oreon_filedir}/perl-PathTools-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.94-521
- Prepare for Oreon 11 (RP1)
