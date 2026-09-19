%global source0_hash 04f806ecdfb7f658f75c59b1ab8616acc7335e08cadf785198ee2ee2304a3d02

# Pass --without docs to rpmbuild if you don't want the documentation

%global SHA1         b1ab8b5d1748b0174fb7014651f0f91de3b4c05a
%global SHA1SHORT    b1ab8b5

Name:           gitweb-caching
Version:        1.6.5.2
Release:        38.%{SHA1SHORT}%{?dist}
Summary:        Simple web interface to git repositories w/ caching support
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://git.kernel.org/?p=git/warthog9/gitweb.git;a=summary
# Tarball is generated from a snapshot of the SHA1 sum above.
# http://git.kernel.org/?p=git/warthog9/gitweb.git;a=snapshot;h=%{SHA1};sf=tgz
#
# NOTE: When downloading a snapshot in this manor (or really anytime git archive
#       is used) the sha1sum of this and any subsequent run is going to be
#       minutely different (the timestamp in the tarball will be current time)
#       because each time it is requested gitweb (and gitweb-caching) is going
#       to completely regenerate the file for download, and thus things like
#       the md5um / sha1sum of the tarball that's present in the RPM here and
#       what could be downloaded to "verify" that things match - won't.
#
#       With that said git already gives us a point of cryptographic integrity
#       internally, and the SHA1 is included here in full so if one cared
#       the individual files would be verified in the tarball vs. what is 
#       present in the repository.  Also to help make verification faster / 
#       easier I, John 'Warthog9' Hawley, am going to GPG sign the tarballs 
#       present so that the chain of trust becomes me claiming the tarball
#       was created by snagging the snapshot from the URL below and if 
#       additional verification is needed please confirm the files via a git
#       checkout of the sha1 above and doing a file by file comparison of the
#       two.
#
# NOTE: When using something like wget or curl to download the snapshot URL
#       this will likely end up in an unexpected state.  The caching, currently,
#       assumes that the client attempting to make use of it will actually
#       interpret the html passed back to it.  During cache generation an interim
#       page is displayed containing "Generating..." as a wait page.  At the end
#       of the page load a meta tag forces an immediate refresh of the page and
#       the actual intended data is shown.  However if your using the
#       aforementioned clients, they do not interpret the data downloaded and thus
#       do not 'refresh' to get the actual data intended.  In those cases the easiest
#       thing to do is to run wget until the data intended does download, or 
#       use an actual webbrowser on the same link.
Source0:        gitweb-%{SHA1}.tar.gz
Source1:        gitweb-%{SHA1}.tar.gz.asc
Source2:        gitweb-caching.conf.httpd
Patch0:         gitweb-caching-1.6-gitweb-home-link.patch
Patch1:         gitweb-caching-fix-base-bin-path.patch
Patch2:         gitweb-caching-default-cache-dir.patch
Patch3:         gitweb-caching-disable-version-matching.patch

BuildArch:      noarch
BuildRequires:      perl-generators
BuildRequires: make
Requires:       git

%description
Simple web interface to track changes in git repositories
w/ caching from John 'Warthog9' Hawley from kernel.org

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n gitweb-%{SHA1SHORT} -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
make %{_smp_mflags} V=1 NO_CURL=1 gitweb/gitweb.cgi gitweb/gitweb_defaults.pl

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_var}/www/gitweb-caching
install -pm 644 gitweb/*.png gitweb/*.css gitweb/gitweb_defaults.pl gitweb/cache.pm $RPM_BUILD_ROOT%{_var}/www/%{name}
install -pm 755 gitweb/gitweb.cgi $RPM_BUILD_ROOT%{_var}/www/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -pm 0755 --directory $RPM_BUILD_ROOT%{_var}/cache/gitweb-caching
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

%files
%doc gitweb/README COPYING
%{_var}/www/%{name}/
%config(noreplace)%{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0755, apache, apache) %{_var}/cache/gitweb-caching

%changelog
%autochangelog
