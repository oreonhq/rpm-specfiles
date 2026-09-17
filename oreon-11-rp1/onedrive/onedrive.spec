%global source0_hash 05b0cb27559e71f8496d25fe6e15c5f4f4a2a1a1c629018f55a8ad35b33d020a

%global project abraunegg
%global repo onedrive

Name:           onedrive
Version:        2.5.10
Release:        2%{?dist}
Summary:        OneDrive Free Client written in D
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/%{project}/%{repo}
Source0:        %{url}/archive/v%{version}/%{repo}-v%{version}.tar.gz
BuildRequires: make
BuildRequires:  ldc
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  sqlite-devel
BuildRequires:  dbus-devel
BuildRequires:  systemd
Requires(preun): systemd
ExclusiveArch:  %{ldc_arches}

%description
Free CLI client for Microsoft OneDrive written in D.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %repo-%{version}
# sed -i 's|version ||g' Makefile
# sed -i '/chown/d' Makefile.in
sed -i 's/-o root -g users//g' Makefile.in
sed -i 's/-o root -g root//g' Makefile.in
# sed -i '/git/d' Makefile
sed -i "s|std\.c\.|core\.stdc\.|" src/sqlite.d
echo %{version} > version

%build
%configure --enable-notifications
export DFLAGS="%{_d_optflags}"
export PREFIX="%{_prefix}"
make DC=ldmd2 %{?_smp_mflags}

%install
%make_install \
    PREFIX="%{_prefix}"
chmod a-x %{buildroot}/%{_mandir}/man1/%{name}*

%preun
%systemd_user_preun %{name}.service
%systemd_preun %{name}@.service

%files
%{_bindir}/%{name}
%if 0%{?el8} || 0%{?el9} || 0%{?el10}
%doc readme.md LICENSE changelog.md
%{_unitdir}/%{name}.service
%else
%{_userunitdir}/%{name}.service
%endif
%{_unitdir}/%{name}@.service
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/icons/hicolor/scalable/places/onedrive.svg
%{_docdir}/%{name}
%config %{_sysconfdir}/logrotate.d/onedrive

%changelog
%autochangelog
