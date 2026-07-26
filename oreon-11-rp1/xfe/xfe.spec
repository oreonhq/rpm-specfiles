%global source0_hash 5dba38d020e828da36491cad0f56991184b03bd9c89f0a58d2896b30c6faf3ea

%global	hash_thread1	2501673c
%global	hash_thread2	5d70

%global	main_version	2.1.5

%global	use_gcc_strict_sanitize	0

Name:		xfe
Version:	%{main_version}
Release:	1%{?dist}
Summary:	X File Explorer File Manager

# GPL-2.0-or-later:	README
# Zlib:	src/xfeutils.h
# MIT:	st/x.c
# SPDX confirmed
License:	GPL-2.0-or-later AND Zlib AND MIT
URL:		http://roland65.free.fr/xfe/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{main_version}.tar.xz
# Temporarily
# Use system-wide startup-notification: need discuss with upstream
Patch0:	xfe-2.0-use-system-libsn.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	fox-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrandr-devel
BuildRequires:	startup-notification-devel
BuildRequires:	/usr/bin/pkexec
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(x11-xcb)
# Patch0
BuildRequires:	autoconf
BuildRequires:	automake

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

%description
X File Explorer (xfe) is a lightweight file manager for X11, 
written using the FOX toolkit.

%package	theme
Summary:	Extra theme files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	theme
This package contains extra theme files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{main_version}
%patch -P0 -p1 -b .syssn

for f in \
	ChangeLog
do
	mv $f{,.iso}
	iconv -f ISO-8859-1 -t UTF-8 -o $f{,.iso}
	touch -r $f{.iso,}
	rm -f $f.iso
done

# Fix libreoffice related command name (bug 1788292)
sed -i.oo xferc.in \
	-e 's|lobase|oobase|g' \
	-e 's|localc|oocalc|g' \
	-e 's|lodraw|oodraw|g' \
	-e 's|loimpress|ooimpress|g' \
	-e 's|lomath|oomath|g' \
	-e 's|lowriter|oowriter|g' \
	%{nil}

# Patch0
autoreconf -fi
rm -rf libsn

%build
%set_build_flags

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined -fno-sanitize=vptr"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%configure \
	--bindir=%{_libexecdir}/%{name}
make %{?_smp_mflags}

%install
%make_install \
	INSTALL="install -p"

%find_lang %{name}

# Tweak too generic and short names
mkdir -p %{buildroot}%{_datadir}/%{name}/pixmaps
mkdir -p %{buildroot}%{_bindir}
for suffix in \
	a i e p w
do
	cat > %{buildroot}%{_bindir}/xfe-xf${suffix} <<EOF
#!/bin/sh
export PATH=%{_libexecdir}/%{name}:\$PATH
exec xf${suffix} \$@
EOF
	chmod 0755 %{buildroot}%{_bindir}/xfe-xf${suffix}

	mv %{buildroot}%{_datadir}/applications/{,xfe-}xf${suffix}.desktop
	# Modify desktop file
	sed -i \
		-e "\@^Exec=@s|xf${suffix}|xfe-xf${suffix}|" \
		%{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop
	desktop-file-validate %{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop

	mv %{buildroot}%{_mandir}/man1/{,xfe-}xf${suffix}.1
done

# Move configuration files
mkdir %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/xferc \
	%{buildroot}%{_sysconfdir}
ln -sf ../../../%{_sysconfdir}/xferc %{buildroot}%{_datadir}/%{name}/xferc

%files	-f %{name}.lang
%doc	AUTHORS
%doc	BUGS
%license	COPYING
%doc	ChangeLog
%doc	README
%doc	TODO

%config(noreplace)	%{_sysconfdir}/xferc
%{_datadir}/applications/xfe-xf*.desktop

%{_bindir}/xfe-xf*
%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/xf*

%dir	%{_datadir}/%{name}
%{_datadir}/%{name}/xferc

%dir	%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/icons/default-theme/
%{_datadir}/%{name}/icons/gnome*-theme/
%{_datadir}/%{name}/pixmaps/

%{_datadir}/icons/hicolor/*/apps/xf*.*

%{_datadir}/polkit-1/actions/org.xfe.root.policy

%{_mandir}/man1/xfe-xf*.1*

%files	theme
%{_datadir}/%{name}/icons/*-theme/
%exclude	%{_datadir}/%{name}/icons/default-theme/
%exclude	%{_datadir}/%{name}/icons/gnome*-theme/

%changelog
%autochangelog
