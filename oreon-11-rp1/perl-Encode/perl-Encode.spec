%global source0_hash e4ff0be00ef14c42754c9db2fee41a053e9d4613db6405e98cd0e0e5be740362
%global cpan_version 3.24
Name:           perl-Encode
Epoch:          4
Version:        %{cpan_version}
Release:        1%{?dist}
Summary:        Character encodings in Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
URL:            https://metacpan.org/release/Encode
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-3.24.tar.gz
Requires:       perl(parent) >= 0.221
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Encode::ConfigLocal|MY)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exporter|parent)\\)$
Provides:       perl(Encode::CJKConstants)
Provides:       perl(Encode::Encoding)
Provides:       perl(Encode::JP::JIS7)
Provides:       perl(Encode::MIME::Header)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

%package -n perl-encoding
Summary:        Write your Perl script in non-ASCII or non-UTF-8
Version:        3.00
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(Carp)
Requires:       perl(Filter::Util::Call)
Suggests:       perl(PerlIO::encoding)
Requires:       perl(utf8)
Conflicts:      perl-Encode < 2:2.64-2
%description -n perl-encoding
With the encoding pragma, you can write your Perl script in any encoding you
like (so long as the Encode module supports it) and still enjoy Unicode
support.

However, this encoding module is deprecated under perl 5.18. It uses
a mechanism provided by perl that is deprecated under 5.18 and higher, and may
be removed in a future version.

The easiest and the best alternative is to write your script in UTF-8.

# To mirror files from perl-devel (bug #456534)
# Keep architecture specific because files go into vendorarch
%package devel
Summary:        Perl Encode Module Generator
Version:        %{cpan_version}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl)
Requires:       %{name}%{?_isa} = %{epoch}:%{cpan_version}-%{release}
Recommends:     perl-devel%{?_isa}
Requires:       perl(Encode)
%description devel
enc2xs builds a Perl extension for use by Encode from either Unicode Character
Mapping files (.ucm) or Tcl Encoding Files (.enc). You can use enc2xs to add
your own encoding to perl. No knowledge of XS is necessary.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mod_EUCJP\\)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Encode-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{catdir\(\$blib, }{catdir("/usr", }' %{buildroot}%{_libexecdir}/%{name}/t/piconv.t
perl -i -pe 's{, "-Mblib=\$blib"}{}' %{buildroot}%{_libexecdir}/%{name}/t/piconv.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/piconv %{buildroot}%{_libexecdir}/%{name}/bin
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
%oreon_autofiles perl-encoding usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING ENC2XS_NO_COMMENTS ENC2XS_VERBOSE MAKEFLAGS PERL_CORE \
    PERL_ENCODING PERL_ENCODE_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-encoding -f %{oreon_filedir}/perl-encoding.list
%files -n perl-Encode-devel -f %{oreon_filedir}/perl-Encode-devel.list
%files -n perl-Encode-tests -f %{oreon_filedir}/perl-Encode-tests.list

%changelog

%autochangelog
