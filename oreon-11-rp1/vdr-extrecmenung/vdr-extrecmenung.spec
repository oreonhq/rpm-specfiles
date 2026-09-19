%global source0_hash 869da9f73cfce4814f9bc8eb782684d7a8ad52ae4ad85f3f4817bf73d6e2ca5f

%global pname   extrecmenung
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

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
Version:        2.0.15
Release:        6%{?dist}
Summary:        Powerful next generation recordings menu replacement plugin for VDR

License:        GPL-2.0-or-later
URL:            https://gitlab.com/kamel5/extrecmenung
Source0:        %{url}/-/archive/v%{version}/%{pname}-v%{version}.tar.bz2
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin provides a powerful replacement for VDR's default
recordings menu entry.  It looks like the standard recordings menu, but
adds several functions, such as additional commands for "rename" and "move"
This is the next generation version based on the original "extrecmenu"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-v%{version}
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build AUTOCONFIG=0

%install
%make_install

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license COPYING
%doc HISTORY
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/*.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
%autochangelog
