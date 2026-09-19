%global source0_hash 83fc2726c500b3c1a980ee5a7e011bbeaf3153fabe125a8c0aa9e4ff8d32195b

Summary: A spam filter for Usenet news servers
Name: cleanfeed
Version: 20020501
Release: 38%{?dist}
# Confirmed with upstream, website
License: Artistic-2.0
URL: http://www.bofh.it/~md/cleanfeed/
Source0: http://www.bofh.it/~md/cleanfeed/cleanfeed-20020501.tgz
Patch0: cleanfeed-20020501-redhat.patch
Patch1: cleanfeed-20020501-ro.patch
BuildArch: noarch
BuildRequires: perl-generators
BuildRequires: sed

%description
Cleanfeed is an automatic spam filter for Usenet news servers and
routers (INN, Cyclone, Typhoon, Breeze and NNTPRelay).  Cleanfeed
looks for duplicated messages, repeated patterns, and known spamming
sites and domains.  It can be configured to block binary posts to
non-binary newsgroups, to cancel already-rejected articles, and to
reject some spamming from local users.

Install the cleanfeed package if you need a spam filter for a Usenet
news server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .rh
%patch -P1 -p1

# Create a sysusers.d config file
cat >cleanfeed.sysusers.conf <<EOF
u news - 'cleanfeed user' %{_sysconfdir}/news -
EOF

%build
sed '1 i #!/usr/bin/perl' cleanfeed > filter_innd.pl

%pre
%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/news
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/news/bin/filter
install -m 0644 cleanfeed.local.sample $RPM_BUILD_ROOT/%{_sysconfdir}/news/cleanfeed.local
install -m 0644 bad_* $RPM_BUILD_ROOT/%{_sysconfdir}/news/
install -m 0755 filter_innd.pl \
	$RPM_BUILD_ROOT/%{_datadir}/news/bin/filter/filter_innd.pl

install -m0644 -D cleanfeed.sysusers.conf %{buildroot}%{_sysusersdir}/cleanfeed.conf

%files
%license LICENSE
%doc CHANGES README HACKING TODO
%attr(-,news,news) %config(noreplace)  %{_sysconfdir}/news/cleanfeed.local
%attr(-,news,news) %config(noreplace)  %{_sysconfdir}/news/bad_*
%attr(755,news,news) %dir %{_datadir}/news/bin/filter
%attr(-,news,news) %{_datadir}/news/bin/filter/filter_innd.pl
%{_sysusersdir}/cleanfeed.conf

%changelog
%autochangelog
