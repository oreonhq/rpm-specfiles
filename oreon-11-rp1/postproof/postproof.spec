%global source0_hash 0c7b7a1387a6588726e02b19eccc3f2666e38320b0bd03c35356dc4174eaedf3

%global commit      65bcbbb9d2cf9e44e71d9cfa3bd4e4eddd32ec38
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       postproof
Version:    0
Release:    0.26.20150331git65bcbbb9%{?dist}
Summary:    Mail abuse incident tool

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:    LGPL-3.0-only
URL:        https://github.com/sys4/%{name}
Source0:    https://github.com/sys4/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:  noarch

Requires:   postfix

%description
Collect messages from a Postfix mail queue and preserve them as incident.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
