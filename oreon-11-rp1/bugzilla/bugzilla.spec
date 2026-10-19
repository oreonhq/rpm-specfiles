%global source0_hash e416005f8c3b3f3181660f4e00b03c71e015cac4108862ff33f0f6a8a4daa532
%define bzinstallprefix %{_datadir}
%define bzdatadir %{_sharedstatedir}/bugzilla
Summary:        Bug tracking system
URL: https://www.bugzilla.org/
Name: bugzilla
Version: 5.2
Release:        1%{?dist}
License: LicenseRef-Callaway-MPLv1.1
Source0:        https://github.com/bugzilla/bugzilla/archive/release-%{version}.tar.gz
Source1: bugzilla-httpd-conf
Source2: README.fedora.bugzilla
Source3: bugzilla.cron-daily
Patch0: bugzilla-rw-paths.patch
Patch1: bugzilla-dnf.patch
Patch2: bugzilla-1438957-concatenate-assets.patch
Patch3: bugzilla-1855962-non-html-mail.patch
Patch4: bugzilla-2180465-sphinx-build.patch
BuildArch: noarch
Requires: patchutils
Requires: perl(CGI) >= 3.51
Requires: perl(Digest::SHA)
Requires: perl(Date::Format) >= 2.23
Requires: perl(DateTime) >= 0.75
Requires: perl(DateTime::TimeZone) >= 1.64
Requires: perl(DBI) >= 1.614
Requires: perl(ExtUtils::MM)
Requires: perl(Template) >= 2.24
Requires: perl(Email::Sender) >= 1.300011
Requires: perl(Email::MIME) >= 1.904
Requires: perl(URI) >= 1.55
Requires: perl(List::MoreUtils) >= 0.32
Requires: perl(Math::Random::ISAAC) >= 1.0.1
Requires: perl(File::Slurp) >= 9999.13
Requires: perl(JSON::XS) >= 2.01
Requires: perl(Locale::Language)
Requires: webserver
Requires: which
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
# /oreon:deps
%package doc
Summary: Bugzilla documentation
%package doc-build
Summary: Tools to generate the Bugzilla documentation
%package contrib
Summary: Bugzilla contributed scripts
BuildRequires: python3-devel
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(sanitycheck.cgi\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Apache2::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(ModPerl::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Config\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::Radius\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::LDAP
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Oracle\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Pg\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::db\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::st\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Chart::Lines\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(GD::Graph\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Template::Plugin::GD::Image\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::MIME::Attachment::Stripper\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::Reply\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::FormatText::WithLinks\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Encode
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::MimeInfo::Magic\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::Scalar\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TheSchwartz\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Daemon::Generic\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::SASL\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::SMTP::SSL\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(MIME::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Twig\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LWP::UserAgent\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Scrubber\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Cache::Memcached\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Copy::Recursive\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Which\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XMLRPC::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Message\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Taint\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::BmpConvert\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Auth::Login\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Auth::Verify\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Config\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::WebService\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::OldBugMove\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::OldBugMove::Params\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Voting\\)$
%description
Bugzilla is a popular bug tracking system used by multiple open source projects
It requires a database engine installed - either MySQL, PostgreSQL or Oracle.
Without one of these database engines (local or remote), Bugzilla will not work
- see the Release Notes for details.

%description doc
Documentation distributed with the Bugzilla bug tracking system

%description doc-build
Tools to generate the documentation distributed with Bugzilla

%description contrib
Contributed scripts and functions for Bugzilla

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-release-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

# Deal with changing /usr/local paths here instead of via patches
/usr/bin/perl -pi -e 's|/usr/local/bin/python\b|%{__python3}|' contrib/*.py
/usr/bin/rm -rf contrib/bugzilla-submit

grep -rl '/usr/lib/sendmail\b' contrib docs \
| xargs /usr/bin/perl -pi -e 's|/usr/lib/sendmail\b|%{_sbindir}/sendmail|'

%build

docs/makedocs.pl
for file in `find -type f -perm /111`; do
  if head -1 $file | grep -E -v '^\#!' &>/dev/null; then
    chmod a-x $file
  fi
done
for file in `find -type f -perm /664`; do
  if head -1 $file | grep -E '^\#!' &>/dev/null; then
    chmod a+x $file
  fi
done
%install
mkdir -p %{buildroot}%{bzinstallprefix}/bugzilla
rm Build.PL MANIFEST.SKIP
cp -pr * %{buildroot}%{bzinstallprefix}/bugzilla
echo "0-59/15 * * * * apache cd %{bzinstallprefix}/bugzilla && env LANG=C %{bzinstallprefix}/bugzilla/whine.pl" > %{buildroot}%{bzinstallprefix}/bugzilla/cron.whine
rm -f %{buildroot}%{bzinstallprefix}/bugzilla/README \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/TODO \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/en/Makefile \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/en/make.bat
cp %{SOURCE2} ./README.fedora
mkdir -p %{buildroot}%{bzdatadir}/assets
mkdir -p %{buildroot}%{_sysconfdir}/bugzilla
install -m 0644 -D -p %{SOURCE1}  %{buildroot}%{_sysconfdir}/httpd/conf.d/bugzilla.conf
install -m 0755 -D -p %{SOURCE3}  %{buildroot}%{bzinstallprefix}/bugzilla/cron.daily
ln -s ../../..%{bzdatadir}/assets %{buildroot}%{bzinstallprefix}/bugzilla/assets
%oreon_autofiles bugzilla-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bugzilla-doc-build usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bugzilla-contrib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

(pushd %{bzinstallprefix}/bugzilla > /dev/null
[ -f /etc/bugzilla/localconfig ] || ./checksetup.pl > /dev/null
popd > /dev/null)
%files -f %{oreon_filedir}/main.list
%files -n bugzilla-doc -f %{oreon_filedir}/bugzilla-doc.list
%files -n bugzilla-doc-build -f %{oreon_filedir}/bugzilla-doc-build.list
%files -n bugzilla-contrib -f %{oreon_filedir}/bugzilla-contrib.list

%changelog

%autochangelog
