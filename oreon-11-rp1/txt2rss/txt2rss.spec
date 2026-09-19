%global source0_hash f5f079f74fa93a8e95e644d4c88a1821d67ce0cdc183c9e107461e59736fb6ee

Name:           txt2rss
Version:        0.1
Release:        35%{?dist}
Summary:        Convert from txt to rss

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
# Project hosting has been dropped and is no longer maintained
# URL:            http://code.google.com/p/%{name}/
Source0:        %{name}-01.tar.bz2
Source1:        txt2rss.1
Patch0:         txt2rss-license-block.patch
Patch1:         txt2rss-conf-path.patch
BuildArch:      noarch

%description
txt2rss is a shell script that parses a simple txt file (in a simple
format) and convert it to RSS feed file. Simple to use and intuitive,
you need to set up a config file with parameter like webmaster's name,
link of the site and others, after you just call the script with
options like <input file> and a <output file>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}
%patch -P0 -p0 -b .license-block
%patch -P1 -p0 -b .conf-path

%build
# Empty build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc news.txt feed.css
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

%changelog
%autochangelog
