%global source0_hash none

# package notes require setting RPM-specific environment variables,
# incompatible with flatpak-builder
%undefine _package_note_flags

Name:           flatpak-runtime-config
Version:        42
Release:        %autorelease
Summary:        Configuration files that live inside the flatpak runtime
Source1:        50-flatpak.conf
Source2:        sitecustomize.py
Source3:        defaults.json.in
Source4:        org.fedoraproject.Platform.appdata.xml
Source5:        org.fedoraproject.Sdk.appdata.xml
Source6:        org.fedoraproject.KDE5Platform.appdata.xml
Source7:        org.fedoraproject.KDE5Sdk.appdata.xml
Source8:        org.fedoraproject.KDE6Platform.appdata.xml
Source9:        org.fedoraproject.KDE6Sdk.appdata.xml
Source10:       05-flatpak-fontpath.conf

License:        MIT

BuildRequires:  python3
BuildRequires:  python3-rpm-macros

Requires:       findutils
Requires:       fontpackages-filesystem

%if 0%{?fedora}
Suggests:       fedora-release-flatpak
%endif

%description
This package includes configuration files that are installed into the flatpak
runtime filesystem during the runtime creation process; it is also installed
into the build root when building RPMs. It contains all configuration
files that need to be different when executing a flatpak.

%prep

%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/cache/fontconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d -p -m 0644 %{SOURCE1}
install -t $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d -p -m 0644 %{SOURCE10}

# usercustomize.py to set up Python paths
for d in %{python3_sitelib} ; do
    mkdir -p $RPM_BUILD_ROOT/$d
    install -t $RPM_BUILD_ROOT/$d -m 0644 %{SOURCE2}
done

# Install appdata for both the Platform and the Sdk
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE4}
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE5}
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE6}
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE7}
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE8}
install -t $RPM_BUILD_ROOT%{_datadir}/metainfo -p -m 0644 %{SOURCE9}

# Install flatpak-builder config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/flatpak-builder
sed -e 's|%%{_libdir}|%{_libdir}|' \
    -e 's|%%{_lib}|%{_lib}|' \
    -e 's|%%{build_cflags}|%{build_cflags}|' \
    -e 's|%%{build_cxxflags}|%{build_cxxflags}|' \
    -e 's|%%{build_ldflags}|%{build_ldflags}|' \
    %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/flatpak-builder/defaults.json

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/app.conf <<_EOF
include /run/flatpak/ld.so.conf.d/app-*.conf
include /app/etc/ld.so.conf
include /app/etc/ld.so.conf.d/*.conf
/app/%{_lib}
%if "%{_lib}" != "lib"
/app/lib
%endif
include /run/flatpak/ld.so.conf.d/runtime-*.conf
_EOF

# We duplicate selected file triggers from packages in the runtime, to
# extend them to cover /app as well. Some other functions that RPM file
# triggers normally provide are handled by flatpak triggers - in particular
# calling update-desktop-database and gtk-update-icon-cache.

# The ldconfig scriplets have a limited function since symlinks are supposed
# to be packaged, and a ld.so.cache that handles both /app and /usr is
# maintained by flatpak. But occasionally a symlink is missed in packaging,
# and this will make sure it is created install time, as it would be
# system-wide.

%post -p /sbin/ldconfig

%transfiletriggerin -P 1999999 -- /app/lib /app/lib64 /app/etc/ld.so.conf.d
/sbin/ldconfig

%transfiletriggerin -P 99999 -- /app/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders /usr/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders-%{__isa_bits} > /usr/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders.cache
if [ -d /app/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders ]; then
    GDK_PIXBUF_MODULEDIR=/app/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders/ \
        gdk-pixbuf-query-loaders-%{__isa_bits} >> /usr/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders.cache
    cp /usr/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders.cache /app/%{_lib}/gdk-pixbuf-2.0/2.10.0/loaders.cache
fi

%transfiletriggerin -- /app/share/glib-2.0/schemas
glib-compile-schemas /app/share/glib-2.0/schemas &> /dev/null || :

%transfiletriggerin -- /app/share/fonts
HOME=/root /usr/bin/fc-cache -s

%transfiletriggerin -- /app/share/java
for d in `find /app/share/java -type d`; do mkdir -p /usr${d#/app}; done
for f in `find /app/share/java ! -type d`; do ln -s $f /usr${f#/app}; done

%transfiletriggerin -P 1 -- /app
for l in `find /app -type l`; do \
  case `readlink $l` in /etc/alternatives/*) ln -fns `readlink -f $l` $l ;; esac \
done

%files
%dir %{_prefix}/cache
%dir %{_prefix}/cache/fontconfig
%{python3_sitelib}
%{_datadir}/metainfo/*.appdata.xml
%{_sysconfdir}/flatpak-builder/
%{_sysconfdir}/fonts/conf.d/*
%{_sysconfdir}/ld.so.conf.d/app.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 42-1
- Prepare for Oreon 11 (RP1)
