%global source0_hash 946a9d4506f97393314546557c13efb346f228e70d6c50aca06f65061584b2fb

# Perform optional tests
%bcond_without perl_Locale_Maketext_Gettext_enables_optional_test

Name:           perl-Locale-Maketext-Gettext
Version:        1.32
Release:        16%{?dist}
Summary:        Joins the gettext and Maketext frameworks
# README.md:            GPL+ or Artistic
# t/02-big-endian.t:    "the same terms as Perl" and "the same license as the commonlib package"
#                       (The "commonlib" text is a few-line excerpt.)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Maketext-Gettext
Source0:        https://cpan.metacpan.org/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-%{version}.tar.gz
# Convert getext parameters to maketext parameters (CPAN RT#97771)
Patch0:         gettexttomakettext.patch
BuildArch:      noarch
BuildRequires:  coreutils
# diffutils for cmp
BuildRequires:  diffutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Locale::Maketext)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
%if %{with perl_Locale_Maketext_Gettext_enables_optional_test}
# Optional tests:
# Module::Signature not used
# Socket not used
BuildRequires:  perl(Test::Pod) >= 1.00
%endif

# Filter private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(T_L10N

%description
Locale::Maketext::Gettext joins the GNU gettext and Maketext frameworks. It
is a subclass of Locale::Maketext(3) that follows the way GNU gettext
works. It works seamlessly, both in the sense of GNU gettext and Maketext.
As a result, you enjoy both their advantages, and get rid of both their
problems, too.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Locale-Maketext-Gettext-%{version}
# Remove unsed tests
for F in t/00-signature.t \
%if !%{with perl_Locale_Maketext_Gettext_enables_optional_test}
    t/99-pod.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Sym-link identical files
if cmp t/locale/C/LC_MESSAGES/test.mo t/locale/en/LC_MESSAGES/test.mo; then
    rm t/locale/en/LC_MESSAGES/test.mo
    ln -s ../../C/LC_MESSAGES/test.mo t/locale/en/LC_MESSAGES/test.mo
fi

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Locale_Maketext_Gettext_enables_optional_test}
    rm %{buildroot}%{_libexecdir}/%{name}/t/99-pod.t
%endif
mkdir -p %{buildroot}%{_libexecdir}/%{name}/blib/script
ln -s \
    $(realpath --relative-to %{buildroot}%{_libexecdir}/%{name}/blib/script \
        %{buildroot}%{_bindir}/maketext) \
    %{buildroot}%{_libexecdir}/%{name}/blib/script/maketext
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/12-cache.t and others write into CWD.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license Artistic
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/maketext
%{_mandir}/man1/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
