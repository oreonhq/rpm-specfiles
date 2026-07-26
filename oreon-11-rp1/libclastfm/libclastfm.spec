%global source0_hash 84a8d62324e3d80b56f3d0e4a8b5ac69a8d76294740747282b413102efee7a4a

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=767838

%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev 968af0ab84e6f8b7658371c778fc8ad2714db68e
%global git_date 20120314
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

# Source0 was generated as follows: 
# git clone git://liblastfm.git.sourceforge.net/gitroot/liblastfm/liblastfm
# cd %%{name}
# git archive --format=tar --prefix=%{name}/ %%{git_short} | bzip2 > %%{name}-%%{?git_version}.tar.bz2

Name:           libclastfm
Version:        0.5
Release:        0.30%{?git_version:.%{?git_version}}%{?dist}
Summary:        Unofficial C-API for the Last.fm web service

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://liblastfm.sourceforge.net/
Source0:        %{name}-%{?git_version}.tar.bz2

BuildRequires:  libtool
BuildRequires:  libcurl-devel
BuildRequires: make

%description
libclastfm is an unofficial C-API for the Last.fm web service written with
libcurl. It was written because the official CBS Interactive Last.fm library
requires Nokia QT, which is usually not desired when using GTK+ based distros.

This library supports much more than basic scrobble submission. You can send
shouts, fetch Album covers and much more.

Due to the naming conflict with the official last.fm library, this library will
install as "libclastfm".

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}

%build
NOCONFIGURE=1 sh autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
