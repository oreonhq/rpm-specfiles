%global source0_hash 3ada48199fa085c17f86b5e940194996b6350e19ae9fd40470096187e4bb8005
Name:           cups-x2go
Version:        3.0.1.4
Release:        1%{?dist}
Summary:        CUPS backend for printing from X2Go
License:        GPL-2.0-or-later
URL:            http://www.x2go.org/
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
Patch0:         cups-x2go-remove-old-setpdfwrite.patch
BuildArch:      noarch
Requires:       cups
Requires:       ghostscript
Requires:       openssh-clients
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - audio support
    - authentication by smartcard and USB stick

CUPS backend for printing from X2Go.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%install
mkdir -p %{buildroot}%{_prefix}/lib/cups/backend/
install -pm700 cups-x2go %{buildroot}%{_prefix}/lib/cups/backend/
mkdir -p %{buildroot}%{_sysconfdir}/cups/
cp -p cups-x2go.conf %{buildroot}%{_sysconfdir}/cups/
mkdir -p %{buildroot}%{_datadir}/ppd/cups-x2go/
cp -p CUPS-X2GO.ppd %{buildroot}%{_datadir}/ppd/cups-x2go/
mkdir -p %{buildroot}%{_datadir}/x2go/versions
cp -p VERSION.cups-x2go %{buildroot}%{_datadir}/x2go/versions/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
