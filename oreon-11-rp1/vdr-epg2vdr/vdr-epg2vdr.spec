%global source0_hash 651798b21c6a235cf03e7547feeee7f02819ebe11d8cc2f694a2ea2ab46e0248

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-epg2vdr
Version:        1.2.17
Release:        12%{?dist}
Summary:        A plugin to retrieve EPG data from a mysql database into VDR

License:        GPL-1.0-or-later
URL:            https://github.com/horchi/vdr-plugin-epg2vdr
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  imlib2-devel
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  python3-devel
BuildRequires:  jansson-devel
BuildRequires:  libarchive-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
This plugin is used to retrieve EPG data into the VDR. The EPG data 
was loaded from a mysql database. 

 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-epg2vdr-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README
# disable AUX patch
sed -i -e 's|WITH_AUX_PATCH = 1|#WITH_AUX_PATCH = 1|' Make.config

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
%make_install
# fix the perm
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY* README*
%config(noreplace) %{vdr_configdir}/plugins/epg2vdr/epg.dat
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
%autochangelog
