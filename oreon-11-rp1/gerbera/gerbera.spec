%global source0_hash c55ec5cddc952e2563586ac76014be072c9dedb5094c6675889afa90b8df23e2

Name:           gerbera
Version:        3.2.0
Release:        1%{?dist}
Summary:        UPnP Media Server
License:        GPL-2.0-only AND MIT AND OFL-1.1
Url:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        config.xml
Source2:        gerbera-sysusers.conf

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libupnp-devel
BuildRequires:  libuuid-devel
BuildRequires:  sqlite-devel
BuildRequires:  duktape-devel
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  file-devel
BuildRequires:  libexif-devel
BuildRequires:  exiv2-devel
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  libebml-devel
BuildRequires:  libmatroska-devel
BuildRequires:  spdlog-devel
BuildRequires:  pugixml-devel
BuildRequires:  mariadb-connector-c-devel
%{?systemd_ordering}
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  jsoncpp-devel
BuildRequires:  libicu-devel
Requires:       %{name}-data = %{version}-%{release}

%description
Gerbera is a UPnP media server which allows you to stream your digital
media through your home network and consume it on a variety of UPnP
compatible devices.

%package data
Summary:        Data files for Gerbera
BuildArch:      noarch

%description data
Data files for the Gerbera media server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake \
    -DWITH_JS=1 \
    -DWITH_MYSQL=1 \
    -DWITH_CURL=1 \
    -DWITH_TAGLIB=1 \
    -DWITH_MAGIC=1 \
    -DWITH_AVCODEC=0 \
    -DWITH_EXIF=1 \
    -DWITH_EXIV2=1 \
    -DWITH_FFMPEGTHUMBNAILER=0 \
    -DWITH_INOTIFY=1 \
    -DWITH_SYSTEMD=1 \
    -DUPNP_HAS_IPV6=1 \
    -DUPNP_HAS_REUSEADDR=1 \
    -DWITH_ZIP=0

%cmake_build

%install
install -p -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gerbera/config.xml
install -p -D -m0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/gerbera.conf

%cmake_install

# make all files under %%_sysconfdir/gerbera owned by
# this package
mkdir -p %{buildroot}%{_sysconfdir}/gerbera
touch %{buildroot}%{_sysconfdir}/gerbera/{gerbera.db,gerbera.html}
mkdir -p %{buildroot}%{_localstatedir}/log/gerbera
touch %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p  %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << 'EOF'
/var/log/gerbera/gerbera {
create 644 gerbera gerbera
      monthly
      compress
      missingok
}
EOF

%post
%systemd_post gerbera.service

%preun
%systemd_preun gerbera.service

%postun
%systemd_postun_with_restart gerbera.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md
%attr(-,gerbera,gerbera)%dir %{_sysconfdir}/%{name}/
%attr(-,gerbera,gerbera)%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(-,gerbera,gerbera) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/logrotate.d
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/gerbera.service
%{_sysusersdir}/gerbera.conf
%{bash_completions_dir}/gerbera

%files data
%{_datadir}/%{name}/
%config(noreplace) %{_datadir}/%{name}/js/import.js
%config(noreplace) %{_datadir}/%{name}/js/playlists.js
%config(noreplace) %{_datadir}/%{name}/js/common.js

%changelog
%autochangelog
