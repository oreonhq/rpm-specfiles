%global source0_hash 15bd73116f3bda9afc274bee97eff829b98f38b13043be32d7bb7f81af294715

%global pname   epgfixer
%global __provides_exclude_from ^%{vdr_plugindir}/
%global commit  354f28b0112ba27f08f6509243b410899f74b6ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20180416

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
Version:        0.3.1
Release:        45.%{gitdate}git%{shortcommit}%{?dist}
Summary:        VDR plugin for doing extra fixing of EPG data

License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-epgfixer
Source0:        https://github.com/vdr-projects/vdr-plugin-epgfixer/archive/%{commit}/%{name}-%{version}-git%{shortcommit}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  pcre-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
Epgfixer is a VDR plugin for doing extra fixing of EPG data. Features
include modifying EPG data using regular expressions, character set
conversions, blacklists, cloning EPG data, removing HTML tags, and
editing all settings through setup menu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-%{pname}-%{commit}

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" \
     LIBDIR=. LOCALEDIR=./locale VDRDIR=%{_libdir}/vdr

%install
%make_install
install -dm 755 %{buildroot}%{vdr_configdir}/plugins/%{pname}
install -pm 644 epgfixer/{blacklist,charset,epgclone,regexp}.conf \
    %{buildroot}%{vdr_configdir}/plugins/%{pname}
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-%{pname}*.so.%{vdr_apiversion}
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/
%defattr(-,root,root,-)

%changelog
%autochangelog
