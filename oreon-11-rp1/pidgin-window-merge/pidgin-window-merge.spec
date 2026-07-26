%global source0_hash e890c829f8f074ca0bbf32a0bd3c9b8008802f2795d6f40a19756379e2ce6531

Name:		pidgin-window-merge
Version:	0.3
Release:	28%{?dist}
Summary:	Pidgin plugin for single window mode

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/dm0-/window_merge
Source0:	https://github.com/downloads/dm0-/window_merge/window_merge-0.3.tar.gz	

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	pidgin-devel
BuildRequires:	libappstream-glib
Requires:	pidgin

%global	pname	window_merge

%description
Enabling this plugin will allow conversations to be attached to the Buddy List
window.  Preferences are available to customize the plugin's panel layout.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} plugindir=%{_libdir}/pidgin
rm -f %{buildroot}%{_libdir}/pidgin/%{pname}.la

mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2015 Jiri Eischmann <eischmann@redhat.com> 
-->
<component type="addon"><id>pidgin-window-merge</id><extends>pidgin.desktop</extends><name>Window Merge</name><summary>A plugin that merges the contact list and chat windows into a single window</summary><url type="homepage">https://github.com/dm0-/window_merge</url><metadata_license>GFDL-1.3</metadata_license><project_license>GPL-3.0</project_license><updatecontact>eischmann_at_redhat.com</updatecontact></component>
EOF

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/pidgin-window-merge.metainfo.xml

%files
%{_libdir}/pidgin/%{pname}.so
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%license COPYING

#AppData
%{_datadir}/appdata/pidgin-window-merge.metainfo.xml

%changelog
%autochangelog
