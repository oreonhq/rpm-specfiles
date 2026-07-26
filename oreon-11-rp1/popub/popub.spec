%global source0_hash 89031f9360735735d61f250876991e23ba36611cdd3495fa55977439b569274e

%global reponame popub
%global commit 6ffa11c634c1aa877d3f4b79ada19b8e6a92dae9
%global commitdate 20171007
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif

Name:    %{reponame}
Version: 0
Release: 0.28.%{commitdate}git%{shortcommit}%{?dist}
Summary: Publish a service from localhost onto your server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL:     https://github.com/m13253/%{name}
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires: make
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%{?systemd_requires}
BuildRequires: systemd

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if ! 0%{?gotest:1}
%define gotest() go test -ldflags "${LDFLAGS:-}" %{?**}
%endif

%description
%{summary}.

%package local
Summary: Publish a service from localhost onto your server - client side
Provides: portpub-local%{?_isa} = %{version}-%{release}
Obsoletes: portpub-local <= 0-0.2

%description local
%{summary}.
Local side package.

%package relay
Summary: Publish a service from localhost onto your server - server side
Provides: portpub-relay%{?_isa} = %{version}-%{release}
Obsoletes: portpub-relay <= 0-0.2

%description relay
%{summary}.
Server side package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build
cd %{reponame}-local
%gobuild -o %{reponame}-local

cd ../%{reponame}-relay
%gobuild -o %{reponame}-relay

%install
sed -i '/daemon-reload/d' systemd/Makefile
%make_install PREFIX=%{_prefix}

%post local
%systemd_post %{name}-local@.service

%preun local
%systemd_preun %{name}-local@.service

%postun local
%systemd_postun_with_restart %{name}-local@.service

%post relay
%systemd_post %{name}-relay@.service

%preun relay
%systemd_preun %{name}-relay@.service

%postun relay
%systemd_postun_with_restart %{name}-relay@.service

%files local
%doc README.md
%license COPYING
%{_bindir}/%{name}-local
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/local
%{_unitdir}/%{name}-local@.service

%files relay
%doc README.md
%license COPYING
%{_bindir}/%{name}-relay
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/relay
%{_unitdir}/%{name}-relay@.service

%changelog
%autochangelog
