%global source0_hash 7bfb51ea6178d7b477e608fb78b18ee9db05676530d857758e22e4abe453a7c3

%global pname   epgsearch
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

%global commit0  76d2b108bf17fde2a98e021c8bbfecb1a9a7e92e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20220201

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
Version:        2.4.6
Release:        1%{?dist}
# Release:        0.12.%%{gitdate}git%%{shortcommit0}%%{?dist}
Summary:        Powerful schedules menu replacement plugin for VDR

License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-epgsearch
Source0:        https://github.com/vdr-projects/vdr-plugin-epgsearch/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:        %%url/archive/%%{commit0}/%%{name}-%%{commit0}.tar.gz#/%%{name}-%%{shortcommit0}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}-epgsearchonly.conf
Source3:        %{name}-conflictcheckonly.conf
Source4:        %{name}-quickepgsearch.conf
Source5:        %{name}-epgsearchmenu.conf
# Fedora specific, no need to send upstream
Patch0:         %{name}-2.4.0-fedora.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  perl-Pod-Checker
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin provides a powerful replacement for VDR's default
schedules menu entry.  It looks like the standard schedules menu, but
adds several functions, such as additional commands for EPG entries,
reusable queries which can be used as dynamic "search timers" etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n vdr-plugin-%{pname}-%{version}
#%%setup -qn vdr-plugin-%{pname}-%%{commit0}
sed -e 's|__VARDIR__|%{vdr_vardir}|g' %{PATCH0} | %{__patch} -p1 --fuzz=0
for f in scripts/epgsearchcmds-french.conf conf/epgsearchcats.conf-tvm2vdr* ; do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f ; mv $f.utf8 $f
done

chmod -x scripts/*

%build
%make_build AUTOCONFIG=0

%install
%make_install
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/epgsearchonly.conf
install -Dpm 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/conflictcheckonly.conf
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/quickepgsearch.conf

install -pm 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchmenu.conf
rm $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchcats.conf-* \
  $RPM_BUILD_ROOT%{vdr_configdir}/plugins/epgsearch/epgsearchupdmail-html.templ

install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/epgsearch

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license COPYING
%doc HISTORY conf/ scripts/
%lang(de) %doc HISTORY
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/*.conf
%{_bindir}/createcats
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{_mandir}/man[145]/*.[145]*
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{vdr_configdir}/plugins/epgsearch/
%config(noreplace) %{vdr_vardir}/epgsearch/
%defattr(-,root,root,-)

%changelog
%autochangelog
