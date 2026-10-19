%global source0_hash c4631c6b5a11527cdc3cb7872fc23b7f2b25c2b021d596be410dadb40315f166
Name:           links
Version:        2.30
Release:        1%{?dist}
Epoch:          1
Summary:        Web browser running in both graphics and text mode
License:        GPL-2.0-or-later
URL:            http://links.twibright.com/
Source0:        http://links.twibright.com/download/%{name}-%{version}.tar.bz2
Source1:        links.desktop
Patch0:         links-configure-c99.patch
%if %with svgalib
%endif
Requires(preun): %{_sbindir}/alternatives
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
Requires(post): coreutils
Requires(postun): coreutils
Provides:       webclient
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gpm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libevent-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Links is a web browser capable of running in either graphics or text mode.
It provides a pull-down menu system, renders complex pages, has partial HTML
4.0 support (including tables, frames and support for multiple character sets
and UTF-8), supports color and monochrome terminals and allows horizontal
scrolling.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
touch %{buildroot}%{_bindir}/links
touch %{buildroot}%{_mandir}/man1/links.1.gz
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
