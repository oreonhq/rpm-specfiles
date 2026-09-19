%global source0_hash ee0ac7a794222d370da245c9dfac7010d2b6e4e77f33816ce84069895355e95e

Name:           uberftp
Version:        2.9.1
Release:        8%{?dist}
Summary:        GridFTP-enabled ftp client

License:        NCSA
URL:            https://gridcf.org/
Source0:        https://repo.gridcf.org/uberftp/sources/uberftp-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  globus-gssapi-gsi-devel

%description
UberFTP is the first interactive, GridFTP-enabled ftp client.
It supports GSI authentication, parallel data channels and
third party transfers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/uberftp
%{_mandir}/man1/uberftp.1*
%doc Changelog.mssftp ChangeLog
%license COPYING

%changelog
%autochangelog
