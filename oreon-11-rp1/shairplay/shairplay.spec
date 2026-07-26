%global source0_hash 7e2b013ffe75ea2f13fb12b1aa38b8e2e8b1899ac292d57f05d7b352a3a181cf

%global commit 096b61ad14c90169f438e690d096e3fcf87e504e
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20180824

Name:           shairplay
Version:        0.9.0
Release:        29.%{commit_date}git%{short_commit}%{?dist}
Summary:        Apple AirPlay and RAOP protocol server

# Automatically converted from old format: MIT and BSD and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/juhovh/%{name}/
Source0:        %{url}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# Shairplay service file, taken from Arch Linux (see
# https://github.com/archlinux/svntogit-community/blob/packages/shairplay/trunk/shairplay.service)
Source1:        %{name}.service
Source2:        airtv.desktop
Source3:        airtv.metainfo.xml
# Fix dns_sd library load
Patch0:         %{name}-0.9.0-dns_sd.patch
# Load airport.key from /etc/ instead of the current directory
Patch1:         %{name}-0.9.0-key_path.patch
# Fix AirTV build
Patch2:         %{name}-0.9.0-AirTV_build.patch

BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  phonon-devel
BuildRequires:  pkgconfig(ao)
BuildRequires:  qt-devel
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       avahi%{?_isa}
Requires:       avahi-compat-libdns_sd%{?_isa}
Requires(pre):  shadow-utils
%{?systemd_requires}

%description
Free portable AirPlay server implementation similar to ShairPort. Currently only
AirPort Express emulation is supported.

%package libs
Summary:        Libraries for %{name}

%description libs
The %{name}-libs package contains the runtime shared libraries for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libao-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n airtv
Summary:        Qt GUI to start a RAOP server
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       avahi-compat-libdns_sd%{?_isa}

%description -n airtv
AirTV Qt is a GUI to start a RAOP server. Once started, AirTV will add an icon
to the system tray using which you can stop the server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p0

%build
[ -f configure ] || ./autogen.sh
%configure \
    --disable-static \
    --with-playfair
# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

# Build AirTV
pushd AirTV-Qt/
%{qmake_qt4}
%make_build
popd

%install
%make_install
find $RPM_BUILD_ROOT -name "*.la" -delete

install -Dpm 0644 airport.key $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/airport.key

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

# Install AirTV
pushd AirTV-Qt/
install -Dpm 0755 AirTV $RPM_BUILD_ROOT%{_bindir}/AirTV
desktop-file-install \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
    %{SOURCE2}
install -Dpm 0644 images/airtv.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/airtv.svg
install -Dpm 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_metainfodir}/airtv.metainfo.xml

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/airtv.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/airtv.metainfo.xml

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/airport.key

%files libs
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files -n airtv
%{_bindir}/AirTV
%{_datadir}/applications/airtv.desktop
%{_datadir}/icons/hicolor/*/apps/airtv.*
%{_metainfodir}/airtv.metainfo.xml

%changelog
%autochangelog
