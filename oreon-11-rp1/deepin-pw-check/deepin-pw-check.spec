%global source0_hash 831ce7e34e08a8c4a19e8d1ef8b3da933d912f12115bfc967062d617e5ebb45a
%bcond check 1
%global __provides_exclude_from ^%{_libdir}/security/.*\.so$
%global goipath         github.com/linuxdeepin/deepin-pw-check
Version:                6.0.12
%global tag             6.0.6
%gometa -L
Name:           deepin-pw-check
Release:        1%{?dist}
Summary:        A tool to verify the validity of the password
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch1:         0001-Adapt-to-Fedora-cracklib-API.patch
# oreon:deps
BuildRequires:  cracklib-devel
BuildRequires:  cracklib-dicts
BuildRequires:  deepin-gettext-tools
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  iniparser-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
# /oreon:deps
%description
deepin-pw-check is a tool to verify the validity of the password.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cracklib-devel%{?_isa}
Requires:       iniparser-devel%{?_isa}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

sed -i 's|${PREFIX}/lib|${PREFIX}/%{_lib}|; s|cp|cp -a|' Makefile
sed -i 's|${DESTDIR}/lib|${DESTDIR}${PREFIX}/lib|' Makefile
sed -i 's|/usr/lib|%{_libdir}|' misc/pkgconfig/libdeepin_pw_check.pc

sed -i 's|gcc |gcc %{build_cflags} %{build_ldflags} |' Makefile

%build

%global gomodulesmode GO111MODULE=on
export CGO_CFLAGS="%{optflags} -std=gnu17"
%make_build
%install
%go_vendor_license_install -c %{S:2}
%make_install PKG_FILE_DIR=%{_libdir}/pkgconfig PAM_MODULE_DIR=%{_libdir}/security
rm %{buildroot}%{_libdir}/*.a
%find_lang deepin-pw-check
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
export CGO_CFLAGS="%{optflags} -std=gnu17"
%gotest ./...
make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n deepin-pw-check-devel -f %{oreon_filedir}/deepin-pw-check-devel.list

%changelog

%autochangelog
