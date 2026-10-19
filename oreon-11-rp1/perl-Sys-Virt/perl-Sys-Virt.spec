%global source0_hash b9621a52478e551c33ccb2f2a471d844ac6949cfa9156dc2e32cbd5d3bb81fa3
Name:           perl-Sys-Virt
Version:        12.7.0
Release:        1%{?dist}
Summary:        Represent and manage a libvirt hypervisor connection
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Virt
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Sys-Virt-v%{version}.tar.gz
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%endif
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libvirt-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
The Sys::Virt module provides a Perl XS binding to the libvirt virtual
machine management APIs. This allows machines running within arbitrary
virtualization containers to be managed with a consistent API.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n Sys-Virt-v%{version}

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/*-pod*.t
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/015-changes.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Sys-Virt-tests -f %{oreon_filedir}/perl-Sys-Virt-tests.list

%changelog

%autochangelog
