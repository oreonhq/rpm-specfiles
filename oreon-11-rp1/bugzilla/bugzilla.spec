%global source0_hash 7ca5ca26242ff5781c2c58933a357948885b19f6d20416fc25171e65cb7df810

%define bzinstallprefix %{_datadir}
%define bzdatadir %{_sharedstatedir}/bugzilla

Summary: Bug tracking system
URL: https://www.bugzilla.org/
Name: bugzilla
Version: 5.0.6
Release: 27%{?dist}
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License: LicenseRef-Callaway-MPLv1.1
Source0: https://github.com/bugzilla/bugzilla/archive/release-%{version}.tar.gz
Source1: bugzilla-httpd-conf
Source2: README.fedora.bugzilla
Source3: bugzilla.cron-daily
Patch0: bugzilla-rw-paths.patch
Patch1: bugzilla-dnf.patch
Patch2: bugzilla-1438957-concatenate-assets.patch
# https://bug1657496.bmoattachments.org/attachment.cgi?id=9169528
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

# for building docs
BuildRequires: latexmk
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Which)
BuildRequires: perl(lib)
BuildRequires: perl(Memoize)
BuildRequires: perl(parent)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: python3-sphinx
BuildRequires: texlive-collection-latexrecommended
BuildRequires: texlive-collection-basic
BuildRequires: tex(fncychap.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(tgtermes.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(wrapfig.sty)
BuildRequires: tex(capt-of.sty)
BuildRequires: tex(eqparbox.sty)
BuildRequires: tex(needspace.sty)
BuildRequires: tex(tabulary.sty)
BuildRequires: tex(upquote.sty)

%package doc
Summary: Bugzilla documentation

%package doc-build
Summary: Tools to generate the Bugzilla documentation

%package contrib
Summary: Bugzilla contributed scripts
BuildRequires: python3-devel

%{?perl_default_filter}

# Remove private modules from the requires stream
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(sanitycheck.cgi\\)$

# Remove all optional modules from the requires stream
# mod_perl modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Apache2::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(ModPerl::
# installation of optional modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Config\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN\\)$
# authentification modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::Radius\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::LDAP
# database modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Oracle\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Pg\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::db\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::st\\)$
# graphical reports and charts
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Chart::Lines\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(GD::Graph\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Template::Plugin::GD::Image\\)$
# inbound email modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::MIME::Attachment::Stripper\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::Reply\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::FormatText::WithLinks\\)$
# automatic charset detection for text attachments
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Encode
# sniff MIME type of attachments
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::MimeInfo::Magic\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::Scalar\\)$
# mail queueing
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TheSchwartz\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Daemon::Generic\\)$
# smtp security
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::SASL\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::SMTP::SSL\\)$
# bug moving modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(MIME::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Twig\\)$
# update notifications
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LWP::UserAgent\\)$
# use html in product and group descriptions
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Scrubber\\)$
# memcached support
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Cache::Memcached\\)$
# documentation
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Copy::Recursive\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Which\\)$
# xml-rpc and json-rpc modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XMLRPC::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Message\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Taint\\)$
# extension modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)$

# and remove the extensions from the provides stream
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
# Build docs
docs/makedocs.pl --with-pdf
# Remove the execute bit from files that don't start with #!
for file in `find -type f -perm /111`; do
  if head -1 $file | grep -E -v '^\#!' &>/dev/null; then
    chmod a-x $file
  fi
done
# Ensure shebang shell scripts have executable bit set
for file in `find -type f -perm /664`; do
  if head -1 $file | grep -E '^\#!' &>/dev/null; then
    chmod a+x $file
  fi
done

%install
mkdir -p %{buildroot}%{bzinstallprefix}/bugzilla
# these files are only used for testing Bugzilla code
# see https://bugzilla.mozilla.org/show_bug.cgi?id=995209
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

%post
(pushd %{bzinstallprefix}/bugzilla > /dev/null
[ -f /etc/bugzilla/localconfig ] || ./checksetup.pl > /dev/null
popd > /dev/null)

%files
%defattr(-,root,apache,-)
%dir %{bzinstallprefix}/bugzilla
%{bzinstallprefix}/bugzilla/LICENSE
%{bzinstallprefix}/bugzilla/*.cgi
%{bzinstallprefix}/bugzilla/*.json
%{bzinstallprefix}/bugzilla/*.pl
%{bzinstallprefix}/bugzilla/Bugzilla.pm
%{bzinstallprefix}/bugzilla/robots.txt
%{bzinstallprefix}/bugzilla/Bugzilla
%{bzinstallprefix}/bugzilla/extensions
%{bzinstallprefix}/bugzilla/images
%{bzinstallprefix}/bugzilla/js
%{bzinstallprefix}/bugzilla/lib
%{bzinstallprefix}/bugzilla/skins
%{bzinstallprefix}/bugzilla/t
%{bzinstallprefix}/bugzilla/xt
%{bzinstallprefix}/bugzilla/template
%{bzinstallprefix}/bugzilla/cron.daily
%{bzinstallprefix}/bugzilla/cron.whine
%{bzinstallprefix}/bugzilla/contrib/README
%{bzinstallprefix}/bugzilla/assets
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bugzilla.conf
%attr(770,root,apache) %dir %{bzdatadir}
%attr(770,root,apache) %dir %{bzdatadir}/assets
%attr(750,root,apache) %dir %{_sysconfdir}/bugzilla
%defattr(-,root,root,-)
%doc README
%doc README.fedora

%files doc
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/docs/en/html
%{bzinstallprefix}/bugzilla/docs/en/images
%{bzinstallprefix}/bugzilla/docs/en/pdf
%{bzinstallprefix}/bugzilla/docs/en/txt
%{bzinstallprefix}/bugzilla/docs/en/rst
%{bzinstallprefix}/bugzilla/docs/style.css

%files doc-build
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/docs/makedocs.pl
%{bzinstallprefix}/bugzilla/docs/lib

%files contrib
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/contrib/bugzilla-queue.rhel
%{bzinstallprefix}/bugzilla/contrib/bugzilla-queue.suse
%{bzinstallprefix}/bugzilla/contrib/bzdbcopy.pl
%{bzinstallprefix}/bugzilla/contrib/bz_webservice_demo.pl
%{bzinstallprefix}/bugzilla/contrib/cmdline
%{bzinstallprefix}/bugzilla/contrib/console.pl
%{bzinstallprefix}/bugzilla/contrib/convert-workflow.pl
%{bzinstallprefix}/bugzilla/contrib/extension-convert.pl
%{bzinstallprefix}/bugzilla/contrib/fixperms.pl
%{bzinstallprefix}/bugzilla/contrib/jb2bz.py*
%{bzinstallprefix}/bugzilla/contrib/merge-users.pl
%{bzinstallprefix}/bugzilla/contrib/mysqld-watcher.pl
%{bzinstallprefix}/bugzilla/contrib/new-yui.sh
%{bzinstallprefix}/bugzilla/contrib/perl-fmt
%{bzinstallprefix}/bugzilla/contrib/recode.pl
%{bzinstallprefix}/bugzilla/contrib/sendbugmail.pl
%{bzinstallprefix}/bugzilla/contrib/sendunsentbugmail.pl
%{bzinstallprefix}/bugzilla/contrib/syncLDAP.pl
%{bzinstallprefix}/bugzilla/contrib/Bugzilla.pm

%changelog
%autochangelog
