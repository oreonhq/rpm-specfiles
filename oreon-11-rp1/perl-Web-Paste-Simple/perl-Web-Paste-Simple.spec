%global source0_hash affe6adacf1671e53c630e9872cbd5462957faff68a72f108dadd491e68271bc
Name:           perl-Web-Paste-Simple
Version:        0.002
Release:        1%{?dist}
Summary:        Simple PSGI-based pastebin-like web site
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR CC-BY-SA-2.0-UK)
URL:            https://metacpan.org/release/Web-Paste-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/Web/Web-Paste-Simple-%{version}.tar.gz
Source1:        web-paste-simple.service
Patch0:         Web-Paste-Simple-0.002-Do-not-use-usr-bin-env.patch
Patch1:         Web-Paste-Simple-0.002-Configure-storage-path-from-environment.patch
BuildArch:      noarch
Requires:       perl(Moo) >= 1.000000
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moo|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(aliased)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Web::Paste::Simple is a lightweight PSGI application for operating
a pastebin-like web site. It provides syntax highlighting via the CodeMirror
JavaScript library. It should be fast enough for deployment via CGI.

%package server
Summary:        Simple pastebin-like web server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       systemd
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
install -d %{buildroot}%{_unitdir}
install -m 0644 web-paste-simple.service %{buildroot}%{_unitdir}
install -d %{buildroot}%{storage}
install -m0644 -D perl-Web-Paste-Simple-server.sysusers %{buildroot}%{_sysusersdir}/perl-Web-Paste-Simple-server.conf
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%post server

%systemd_post apache-httpd.service
%preun server

%systemd_preun apache-httpd.service
%postun server

%systemd_postun_with_restart apache-httpd.service 
%files -f %{oreon_filedir}/main.list
%files -n perl-Web-Paste-Simple-server -f %{oreon_filedir}/perl-Web-Paste-Simple-server.list
%files -n perl-Web-Paste-Simple-tests -f %{oreon_filedir}/perl-Web-Paste-Simple-tests.list

%changelog

%autochangelog
