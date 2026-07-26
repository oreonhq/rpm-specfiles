%global source0_hash affe6adacf1671e53c630e9872cbd5462957faff68a72f108dadd491e68271bc

Name:           perl-Web-Paste-Simple
Version:        0.002
Release:        34%{?dist}
Summary:        Simple PSGI-based pastebin-like web site
# CONTRIBUTING:             GPL-1.0-or-later OR Artistic-1.0-Perl OR CC-BY-SA-2.0-UK
# lib/Web/Paste/Simple.pm   GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR CC-BY-SA-2.0-UK)
URL:            https://metacpan.org/release/Web-Paste-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/Web/Web-Paste-Simple-%{version}.tar.gz
Source1:        web-paste-simple.service
# We don't like /usr/bin/env in shellbangs
Patch0:         Web-Paste-Simple-0.002-Do-not-use-usr-bin-env.patch
# Allow to redefine path to the storage
Patch1:         Web-Paste-Simple-0.002-Configure-storage-path-from-environment.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# Run-time:
BuildRequires:  perl(aliased)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Moo) >= 1.000000
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Text::Template)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(Moo) >= 1.000000

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moo|Test::More)\\)$

%description
Web::Paste::Simple is a lightweight PSGI application for operating
a pastebin-like web site. It provides syntax highlighting via the CodeMirror
JavaScript library. It should be fast enough for deployment via CGI.

%package server
Summary:        Simple pastebin-like web server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# unit directory ownership
Requires:       systemd
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):  shadow-utils
%endif

%description server
This is web-paste-simple daemon for Web::Paste::Simple web service.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.61

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%global storage %{_sharedstatedir}/webpastesimple

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Web-Paste-Simple-%{version}
# Set storage path for the daemon
sed -e '/^ExecStart=/iEnvironment=WEB_PASTE_SIMPLE_STORAGE=%{storage}' \
    < %{SOURCE1} > web-paste-simple.service

# Create a sysusers.d config file
cat >perl-Web-Paste-Simple-server.sysusers <<EOF
u webpastesimple - 'web-paste-simple daemon' %{storage} -
EOF

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Daemon
install -d %{buildroot}%{_unitdir}
install -m 0644 web-paste-simple.service %{buildroot}%{_unitdir}
install -d %{buildroot}%{storage}
install -m0644 -D perl-Web-Paste-Simple-server.sysusers %{buildroot}%{_sysusersdir}/perl-Web-Paste-Simple-server.conf

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%post server
%systemd_post apache-httpd.service

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre server
getent group webpastesimple >/dev/null || groupadd -r webpastesimple
getent passwd webpastesimple >/dev/null || \
    useradd -r -g webpastesimple -d %{storage} -s /sbin/nologin \
        -c "web-paste-simple daemon" webpastesimple
exit 0
%endif

%preun server
%systemd_preun apache-httpd.service

%postun server
%systemd_postun_with_restart apache-httpd.service 

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%dir %{perl_vendorlib}/Web
%dir %{perl_vendorlib}/Web/Paste
%{perl_vendorlib}/Web/Paste/Simple.pm
%{_mandir}/man3/Web::Paste::Simple.*

%files server
%{_bindir}/web-paste-simple.psgi
%{_unitdir}/web-paste-simple.service
%dir %attr(750, webpastesimple, webpastesimple) %{storage}
%{_sysusersdir}/perl-Web-Paste-Simple-server.conf

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
