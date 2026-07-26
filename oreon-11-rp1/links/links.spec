%global source0_hash 4b4f07d0e6261118d1365a5a5bfa31e1eafdbd280cfae6f0e9eedfea51a2f424

# There's no svgalib in RHEL or on non-x86 platforms
%if 0%{?rhel} && 0%{?rhel} < 7
%ifarch %{ix86} x86_64
%bcond_without svgalib
%else
%bcond_with svgalib
%endif
%bcond_with svgalib
%endif

Name:           links
Version:        2.20.2
Release:        18%{?dist}
Epoch:          1
Summary:        Web browser running in both graphics and text mode
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://links.twibright.com/
Source0:        http://links.twibright.com/download/%{name}-%{version}.tar.bz2
Source1:        links.desktop
Patch0:         links-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gpm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  autoconf automake
BuildRequires:  openssl-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libevent-devel
%if %with svgalib
BuildRequires:  svgalib-devel
%endif

Requires(preun): %{_sbindir}/alternatives
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
Requires(post): coreutils
Requires(postun): coreutils

Provides:       webclient

%description
Links is a web browser capable of running in either graphics or text mode.
It provides a pull-down menu system, renders complex pages, has partial HTML
4.0 support (including tables, frames and support for multiple character sets
and UTF-8), supports color and monochrome terminals and allows horizontal
scrolling.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
iconv -f ISO-8859-1 -t UTF-8 AUTHORS >converted.AUTHORS
touch -r AUTHORS converted.AUTHORS
mv converted.AUTHORS AUTHORS

%configure --enable-graphics --with-ssl
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}
mv %{buildroot}/%{_bindir}/links $RPM_BUILD_ROOT/%{_bindir}/links2
mv %{buildroot}/%{_mandir}/man1/links.1 $RPM_BUILD_ROOT/%{_mandir}/man1/links2.1
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
install -D -p Links_logo.png %{buildroot}/%{_datadir}/pixmaps/links.png

# Alternatives cruft
touch %{buildroot}%{_bindir}/links
touch %{buildroot}%{_mandir}/man1/links.1.gz

%postun
[ $1 = 0 ] && exit 0
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0

%preun
[ $1 = 0 ] || exit 0
%{_sbindir}/alternatives --remove links %{_bindir}/links2

%post
%{_sbindir}/alternatives \
        --install %{_bindir}/links links %{_bindir}/links2 80 \
        --slave %{_mandir}/man1/links.1.gz links-man %{_mandir}/man1/links2.1.gz
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0

%files
%doc doc/* AUTHORS KEYS README COPYING
%{_bindir}/links2
%{_mandir}/man1/links2.1*
%{_datadir}/pixmaps/links.png
%{_datadir}/applications/links.desktop
%ghost %verify(not md5 size mtime) %{_bindir}/links
%ghost %verify(not md5 size mtime) %{_mandir}/man1/links.1.gz

%changelog
%autochangelog
