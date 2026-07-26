%global source0_hash 677e3dd52f559992c72be932d958587b5f731a1a295bcee37be878ed3f585926

%bcond_with bootstrap

%global public_key RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3

Name:           minisign
Version:        0.12
Release:        3%{?dist}
Summary:        A dead simple tool to sign files and verify digital signatures
License:        ISC
URL:            https://github.com/jedisct1/minisign
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.minisig

BuildRequires:  libsodium-devel
BuildRequires:  cmake
BuildRequires:  gcc
%if %{without bootstrap}
BuildRequires:  minisign
%endif

%description
Minisign is a dead simple tool to sign files and verify signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{without bootstrap}
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%endif

%autosetup -c

%build
%cmake -DCMAKE_STRIP=0 .
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
