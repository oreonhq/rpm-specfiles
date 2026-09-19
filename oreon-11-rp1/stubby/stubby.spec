%global source0_hash 99291ab4f09bce3743000ed3ecbf58961648a35ca955889f1c41d36810cc4463

Name:           stubby
Version:        0.4.3
Release:        8%{?dist}
Summary:        Application that act as a local DNS Privacy stub resolver

License:        BSD-3-Clause
URL:            https://github.com/getdnsapi/stubby
Source0:        https://github.com/getdnsapi/stubby/archive/v%{version}/stubby-%{version}.tar.gz

Provides:       getdns-stubby = 1.7.0-1
Obsoletes:      getdns-stubby < 1.7.0-1
%{?systemd_requires}

Patch1:         stubby-0.3.1-dnssec-ta.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: cmake
BuildRequires: getdns-devel >= 0.7.0
BuildRequires: openssl-devel
BuildRequires: libyaml-devel
BuildRequires: systemd-rpm-macros

%description
Stubby is a local DNS Privacy stub resolver (using DNS-over-TLS).
Stubby encrypts DNS queries sent from a client machine to a
DNS Privacy resolver increasing end user privacy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install
find %{buildroot} -size 0 -delete
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 systemd/stubby.service %{buildroot}%{_unitdir}/stubby.service

%preun
%systemd_preun %{name}

%post
# systemd would replace it with symlink
if [ ! -L "%{_localstatedir}/cache/stubby" -a -d "%{_localstatedir}/cache/stubby" ]; then
       mv "%{_localstatedir}/cache/stubby"{,.rpmsave}
fi
%systemd_post %{name}

%postun
%systemd_postun_with_restart %{name}

%files
%{_bindir}/stubby
%config(noreplace) %{_sysconfdir}/stubby
%ghost %{_localstatedir}/cache/stubby
%{_unitdir}/stubby.service
%{_mandir}/man1/stubby.1.gz
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%license %{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/README.md

%changelog
%autochangelog
