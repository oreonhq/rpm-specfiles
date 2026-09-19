%global source0_hash 025b785891f3dc536827eaffaccd56b7d90455a310146180ee168a3cb0501577

Summary:        A fast and lightweight vim like web browser
Name:           vimb
License:        GPL-3.0-only

Version:        3.7.0
Release:        6%{?dist}

URL:            https://fanglingsu.github.io/vimb/
Source0:        https://github.com/fanglingsu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Vimb is a fast and lightweight vim like web browser based on the webkit
web browser engine and the GTK toolkit. Vimb is modal like the great vim
editor and also easily configurable during runtime. Vimb is mostly
keyboard driven and does not distract you from your daily work.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
sed -i 's/EXTLDFLAGS  =/EXTLDFLAGS  = ${LDFLAGS} /g' config.mk
%make_build DOTDESKTOPPREFIX=%{_datadir}/applications \
            EXTENSIONDIR=%{_libdir}/vimb

%install
%make_install PREFIX=%{_prefix} \
              LIBDIR=%{buildroot}/%{_libdir}/%{name} \
              EXTENSIONDIR=%{buildroot}/%{_libdir}/%{name}

strip --strip-unneeded %{buildroot}/%{_libdir}/%{name}/webext_main.so

%check
make test
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files 
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/webext_main.so
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
