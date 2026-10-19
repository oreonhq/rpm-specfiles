%global source0_hash b347189ab550ae5bd1a19d323cdfd8928039853c23aa5e33d7273ab8c750692a
%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%bcond_with gconf
%else
%bcond_without gconf
%endif
Summary:        Writes audio CD-Rs in disk-at-once (DAO) mode
Name:      cdrdao
Version:   1.2.6
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       http://cdrdao.sourceforge.net/
Source0:        https://github.com/cdrdao/cdrdao/archive/refs/tags/rel_1_2_5.tar.gz#/%{name}-%{version}.tar.gz
Patch:     21.patch
Patch1:    cdrdao-1.2.5-Fix-version-command.patch
Patch2:    cdrdao-1.2.5-gcc15.patch
%if %{with gconf}
%endif
Obsoletes: gcdmaster < 1.2.3-10
ExcludeArch: s390 s390x
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtkmm3.0-devel
BuildRequires:  lame-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
# /oreon:deps
%description
Cdrdao records audio CD-Rs in disk-at-once (DAO) mode, based on a
textual description of the CD contents. Recording in DAO mode writes
the complete disc (lead-in, one or more tracks, and lead-out) in a
single step. DAO allows full control over the length and the contents
of pre-gaps, the pause areas between tracks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-rel_1_2_5
%oreon_prep
%build

autoreconf -v -f -i -I.
%configure \
        --without-xdao \
        --without-scglib \
        --with-ogg-support \
        --with-mp3-support \
        --with-lame
find /usr/include/giomm-2.4 -name '*.h' -exec sed -i '/^using G.*Class = struct _/d' {} +
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-1
- Import
