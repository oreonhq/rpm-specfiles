%global source0_hash ee0f80775a69ae8af360d8ef33ea66fd60ed720cef6e793afdacf748dad4caec

Name:           cups-x2go
Version:        3.0.1.3
Release:        25%{?dist}
Summary:        CUPS backend for printing from X2Go

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.x2go.org/
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# removes old '.setpdfwrite' in ghostscript calls (#1968351)
Patch0:         cups-x2go-remove-old-setpdfwrite.patch

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       cups
Requires:       ghostscript
Requires:       openssh-clients

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
# The cups-x2go backends wants root permissions. So give it to them.
# http://www.cups.org/documentation.php/doc-1.4/man-backend.html says:
# “Backends without world execute permissions are run as the root user.
# Otherwise, the backend is run using the unprivileged user account,
# typically "lp".”
install -pm700 cups-x2go %{buildroot}%{_prefix}/lib/cups/backend/
mkdir -p %{buildroot}%{_sysconfdir}/cups/
cp -p cups-x2go.conf %{buildroot}%{_sysconfdir}/cups/
mkdir -p %{buildroot}%{_datadir}/ppd/cups-x2go/
cp -p CUPS-X2GO.ppd %{buildroot}%{_datadir}/ppd/cups-x2go/
mkdir -p %{buildroot}%{_datadir}/x2go/versions
cp -p VERSION.cups-x2go %{buildroot}%{_datadir}/x2go/versions/

%files
%doc ChangeLog COPYING README.txt
%{_prefix}/lib/cups/backend/cups-x2go
%config(noreplace) %{_sysconfdir}/cups/cups-x2go.conf
%{_datadir}/ppd/cups-x2go/
%{_datadir}/x2go/

%changelog
%autochangelog
