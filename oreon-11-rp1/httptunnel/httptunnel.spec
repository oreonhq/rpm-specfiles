%global source0_hash dff8dcf76e7176018958429f4251dd6b8d7393b03c19fa98d6e695aaf7295e79

Name:           httptunnel
Version:        3.3
Release:        36%{?dist}
Summary:        Tunnels a data stream in HTTP requests

License:        GPLv2
URL:            http://www.nocrew.org/software/httptunnel.html
#use debian repackage tarball, it doesn't include non-free documentation files
Source0:        http://ftp.de.debian.org/debian/pool/main/h/httptunnel/httptunnel_%{version}+dfsg.orig.tar.gz
Patch0:         httptunnel-configure-c99.patch
Patch1:         httptunnel-headers-c99.patch
BuildRequires:  gcc
BuildRequires: make

%description
HTTPTunnel creates a bidirectional virtual data stream tunnelled in
HTTP requests. The requests can be sent via a HTTP proxy if so desired.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode AUTHORS iso-8859-15
recode ChangeLog iso-8859-15

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING DISCLAIMER FAQ HACKING NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
