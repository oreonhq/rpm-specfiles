%global source0_hash 972ee45ec926d72b6444412c8edf873bc6db0b32ca5df42f2d5d815887a9fee4
Summary:        Network performance tool with modelling and replay support
Name:          uperf
Version:       1.0.8
Release:        1%{?dist}
License:       GPL-3.0-only
URL:           http://www.uperf.org/
Source0:        https://github.com/uperf/uperf/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Network performance tool that supports modelling and replay of various
networking patterns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
chmod 0644 workloads/{tcp-change-cc.xml,sctp-over-udp.xml,tcp-freebsd-change-stack.xml}

%build

autoreconf --install
%configure           \
    --enable-cpc     \
    --enable-netstat \
    --enable-udp     \
    --enable-sctp    \
    --enable-ssl
%make_build
%install
%make_install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/%{name}
install -p -m 0644 {server,client}.pem %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/doc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
