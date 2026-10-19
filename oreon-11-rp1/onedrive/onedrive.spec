%global source0_hash 7a9cfbf1cc20c8e157dd028e819ec14b9893c158494b9744708ace975076f995
%global project abraunegg
%global repo onedrive
Name:           onedrive
Version:        2.5.11
Release:        1%{?dist}
Summary:        OneDrive Free Client written in D
License:        GPL-3.0-only
URL:            https://github.com/%{project}/%{repo}
Source0:        https://github.com/%{project}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires(preun): systemd
ExclusiveArch:  %{ldc_arches}
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  ldc
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  make
BuildRequires:  sqlite-devel
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%preun

%systemd_user_preun %{name}.service
%systemd_preun %{name}@.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
