%global base_version 3.75

Name:           perl-PathTools
Version:        3.94
Release:        521%{?dist}
Summary:        PathTools Perl module (Cwd, File::Spec)
# Cwd.xs:                   BSD-3-Clause
# other files:              GPL-1.0-or-later OR Artistic-1.0-Perl
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND BSD-3-Clause
URL:            https://metacpan.org/release/PathTools
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/PathTools-%{base_version}.tar.gz
# Disable VMS tests (bug #973713)
Patch0:         PathTools-3.74-Disable-VMS-tests.patch
# Unbundled from perl 5.29.10
Patch1:         PathTools-3.75-Upgrade-to-3.78.patch
# Unbundled from perl 5.34.0
Patch2:         PathTools-3.78-Upgrade-to-3.80.patch
# Unbundled from perl 5.35.11
Patch3:         PathTools-3.80-Upgrade-to-3.84.patch
# Unbundled from perl 5.37.11
Patch4:         PathTools-3.84-Upgrade-to-3.89.patch
# Unbundled from perl 5.40.1
Patch5:         PathTools-3.89-Upgrade-to-3.91.patch
# Unbundled from perl 5.42.0
Patch6:         PathTools-3.91-Upgrade-to-3.94.patch
# oreon url source checksums begin
%global source0_sha256 a558503aa6b1f8c727c0073339081a77888606aa701ada1ad62dd9d8c3f945a2
%global source0_file PathTools-3.75.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
# File::Basename not needed because of removed File::Spec::VMS
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Optional run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(Errno)
Requires:       perl(Scalar::Util)
# XSLoader is optional only because miniperl does not support XS. With perl we
# almost certainly want it.
Recommends:     perl(XSLoader)

%{?perl_default_filter}

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/PathTools-3.75.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a558503aa6b1f8c727c0073339081a77888606aa701ada1ad62dd9d8c3f945a2" || { echo "oreon: Source0 SHA256 mismatch for PathTools-3.75.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe "s#qr{blib}#qr{%{perl_vendorarch}}#" %{buildroot}%{_libexecdir}/%{name}/t/cwd.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/File/
%{_mandir}/man3/Cwd*
%{_mandir}/man3/File::Spec*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.94-521
- Prepare for Oreon 11 (RP1)
