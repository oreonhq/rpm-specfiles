%global source0_hash c524955a0c891d91623339baca5c2ea880cccfe1d47bcc324f62ec4959db0715
Name:               sshuttle
Version:            1.3.2
Release:        1%{?dist}
Summary:        Transparent Proxy VPN
Source0:        https://github.com/sshuttle/sshuttle/archive/refs/tags/v%{version}.tar.gz
URL:                https://github.com/%{name}/%{name}
License:            LGPL-2.0-or-later
BuildArch:          noarch
Requires:           iptables
Requires:           openssh-clients
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sshuttle = %{version}-%{release}
# /oreon:deps
%description
Transparent proxy server that works as a poor man's VPN. Forwards over ssh.
Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs
make man
make info
popd
%install
%pyproject_install
pushd docs
mkdir -p %{buildroot}/%{_mandir}/man1
mv _build/man/%{name}.1 %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_infodir}
mv _build/texinfo/%{name}.info %{buildroot}/%{_infodir}
popd
%oreon_autofiles main

%check

%files

%changelog

%autochangelog
