%global source0_hash 89031f9360735735d61f250876991e23ba36611cdd3495fa55977439b569274e
%global reponame popub
%global commit 6ffa11c634c1aa877d3f4b79ada19b8e6a92dae9
%global commitdate 20171007
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif
Name:    %{reponame}
Version: 5.0.1
Release:        1%{?dist}
Summary:        Publish a service from localhost onto your server
License: GPL-3.0-or-later
URL:     https://github.com/m13253/%{name}
Source0:        https://github.com/m13253/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
%{?systemd_requires}
%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif
%if ! 0%{?gotest:1}
%define gotest() go test -ldflags "${LDFLAGS:-}" %{?**}
%endif
# oreon:deps
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n popub-local -f %{oreon_filedir}/popub-local.list
%files -n popub-relay -f %{oreon_filedir}/popub-relay.list

%changelog

%autochangelog
