%global source0_hash c46fb01eaa233f59f831b586190506d347394e35496a84f773216dbdd038b6c8
Name:           perl-YAML-PP-LibYAML
Version:        0.005
Release:        1%{?dist}
Summary:        Faster parsing for YAML::PP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/YAML-PP-LibYAML
Source0:        http://www.cpan.org/authors/id/T/TI/TINITA/YAML-PP-LibYAML-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(YAML::PP) >= 0.025
Requires:       perl(YAML::LibYAML::API::XS) >= 0.011
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(YAML::PP\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(YAML::LibYAML::API::XS)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::LibYAML::API::XS)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(YAML::PP::Common)
BuildRequires:  perl(YAML::PP::Emitter)
BuildRequires:  perl(YAML::PP::Parser)
BuildRequires:  perl(YAML::PP::Reader)
BuildRequires:  perl(YAML::PP::Writer)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
YAML::PP::LibYAML is a subclass of YAML::PP. Instead of using
YAML::PP::Parser as a the backend parser, it uses YAML::PP::LibYAML::Parser
which calls YAML::LibYAML::API, an XS wrapper around the C libyaml.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(blib)
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n YAML-PP-LibYAML-%{version}

# Help file to recognise the Perl scripts
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{\$Bin/data/simple.yaml.out}{/tmp/simple.yaml.out}' %{buildroot}/%{_libexecdir}/%{name}/t/10.basic.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-YAML-PP-LibYAML-tests -f %{oreon_filedir}/perl-YAML-PP-LibYAML-tests.list

%changelog

%autochangelog
