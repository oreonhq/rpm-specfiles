%global source0_hash 79db1b4d9fcfafe5cb6a30eb29174f912f1b2c04a644bd5fe5075bccad10eb97
Name:           gerbera
Version:        3.3.0
Release:        1%{?dist}
Summary:        UPnP Media Server
License:        GPL-2.0-only AND MIT AND OFL-1.1
Url:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        config.xml
Source2:        gerbera-sysusers.conf
%{?systemd_ordering}
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  duktape-devel
BuildRequires:  exiv2-devel
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libebml-devel
BuildRequires:  libexif-devel
BuildRequires:  libicu-devel
BuildRequires:  libmatroska-devel
BuildRequires:  libupnp-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  pugixml-devel
BuildRequires:  spdlog-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  taglib-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post gerbera.service
%preun

%systemd_preun gerbera.service
%postun

%systemd_postun_with_restart gerbera.service
%files -f %{oreon_filedir}/main.list
%files -n gerbera-data -f %{oreon_filedir}/gerbera-data.list

%changelog

%autochangelog
