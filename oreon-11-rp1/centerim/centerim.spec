%global source1_hash b3a68ed2d6a4318242572a9f72246aa1a3f911db9240f15cb98367c0a2b315b6
%global source0_hash b3a68ed2d6a4318242572a9f72246aa1a3f911db9240f15cb98367c0a2b315b6
Name:           centerim
Version:        4.22.10
Release:        50%{?dist}
Epoch:          1
Summary:        Text mode menu- and window-driven IM
License:        GPL-2.0-or-later
URL:            http://www.centerim.org/
Source0:        http://www.centerim.org/download/releases/%{name}-%{version}.tar.gz
Source1:        http://www.centerim.org/images/b/b5/Centerim_b.svg
Source2:        centerim.desktop
Patch0:         centerim-4.22.6-url-escape-fedora.patch
Patch1:         centerim-gcc46.patch
Patch2:         centerim-double-slash.patch
Patch3:         centerim-c99.patch
Requires:       xdg-utils
Provides:       centericq = 4.21.0
Obsoletes:      centericq <= 4.21.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gpgme-devel
BuildRequires:  libjpeg-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
CenterIM is a text mode menu- and window-driven IM interface that supports
the ICQ2000, Yahoo!, MSN, AIM TOC, IRC, Gadu-Gadu and Jabber protocols.
Internal RSS reader and a client for LiveJournal are provided.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .url-escape-fedora
%patch -P1 -p1 -b .gcc46
%patch -P2 -p1 -b .dblslash
%patch -P3 -p1 -b .c99

iconv -f iso8859-1 -t utf8 ChangeLog >ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoreconf -vfi
autoconf
%configure \
        --with-ssl \
        --disable-rpath \
        --enable-locales-fix
%make_build
%check

make check
%install
%make_install
%find_lang %{name}
rm %{buildroot}%{_bindir}/CenterIMLog2HTML.py
find %{buildroot} -type f -name "*.la" -delete
install -d %{buildroot}%{_datadir}/icons
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
