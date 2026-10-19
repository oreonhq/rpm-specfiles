%global source0_hash 04f806ecdfb7f658f75c59b1ab8616acc7335e08cadf785198ee2ee2304a3d02
%global SHA1         b1ab8b5d1748b0174fb7014651f0f91de3b4c05a
%global SHA1SHORT    b1ab8b5
Name:           gitweb-caching
Version:        1.6.5.2
Release:        1%{?dist}
Summary:        Simple web interface to git repositories w/ caching support
License:        GPL-2.0-only
URL:            http://git.kernel.org/?p=git/warthog9/gitweb.git;a=summary
Source0:        gitweb-%{SHA1}.tar.gz
Source1:        gitweb-%{SHA1}.tar.gz.asc
Source2:        gitweb-caching.conf.httpd
Patch0:         gitweb-caching-1.6-gitweb-home-link.patch
Patch1:         gitweb-caching-fix-base-bin-path.patch
Patch2:         gitweb-caching-default-cache-dir.patch
Patch3:         gitweb-caching-disable-version-matching.patch
BuildArch:      noarch
Requires:       git
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
