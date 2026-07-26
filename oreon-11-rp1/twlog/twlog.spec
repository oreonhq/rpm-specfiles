%global source0_hash 22b5ad56f08724483b84631a0455d23506932e316077f20369eb5f8070def005

# https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:		twlog
Version:	3.4
Release:	15%{?dist}
Summary:	Records basic ham radio log information
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

URL:		http://wa0eir.bcts.info/twlog.html

Source0:	http://wa0eir.bcts.info/src/%{name}-%{version}.src.tar.gz
# Wrapper script to install user defaults
Source1:	%{name}.sh.in

# .desktop patch
Patch0:		%{name}-%{version}.desktop.patch
Patch1:		twlog-configure-c99.patch

BuildRequires:	desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:	xbae-devel

%description
Twlog records basic Ham log information. It was written
for day to day logging, not contesting. There are no dupe
checks or contest related features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Set perms on source file
chmod 644 ./src/adif.c

%build
%configure
%make_build

%install
%make_install

# Install provided icon
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
install -p -D -m 0644 ./src/icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/	\
	%{buildroot}/%{_datadir}/applications/%{name}.desktop

# Move original binary to libexecdir
mkdir -p %{buildroot}/%{_libexecdir}/
mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_libexecdir}/%{name}-bin

# Install wrapper script installs needed files in users home directory.
install -p -D -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}

# Twlog default settings
mkdir -p %{buildroot}/%{_datadir}/X11/app-defaults/
install -p -D -m 0644 ./src/Twlog %{buildroot}/%{_datadir}/X11/app-defaults/Twlog

%files
%doc AUTHORS NEWS README TODO ChangeLog THANKS
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/%{name}-bin
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/X11/app-defaults/Twlog
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
