%global source0_hash 3428569d284db2fb1e57fe2683a818be489311d0b0ca3d4d172d34638fa61eaf

%global pname   skinenigmang

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

Name:           vdr-%{pname}
Version:        0.1.5
Release:        11%{?dist}
Summary:        A skin for VDR based on the Enigma text2skin add on

License:        GPL-1.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-skinenigmang
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        http://andreas.vdr-developer.org/enigmang/download/skinenigmang-logos-xpm-hi-20070702.tgz
Source2:        %{name}.conf
Patch0:         %{name}-config.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  freetype-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
VDR plugin: %{pname} - %{summary}
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-skinenigmang-%{version} -a 1
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README
mv skinenigmang/HISTORY HISTORY.logos
mv skinenigmang/README README.logos

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" \
   HAVE_IMAGEMAGICK=GRAPHICS

%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_plugindir}
install -pm 755 libvdr-%{pname}.so \
    $RPM_BUILD_ROOT%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}

# skinenigmang.conf
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

# themes
install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/themes
install -pm 644 themes/*.theme $RPM_BUILD_ROOT%{vdr_vardir}/themes

# flags,icons
install -dm 755 $RPM_BUILD_ROOT%{vdr_resdir}
cp -a skinenigmang/{flags,icons} $RPM_BUILD_ROOT%{vdr_resdir}

%files
%doc HISTORY* README*
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/EnigmaNG-*.theme
%{vdr_resdir}/flags
%{vdr_resdir}/icons

%changelog
%autochangelog
