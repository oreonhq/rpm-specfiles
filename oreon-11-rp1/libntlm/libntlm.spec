%global source0_hash ce6569a47a21173ba69c990965f73eb82d9a093eb871f935ab64ee13df47fda1
Name:           libntlm
Version:        1.8
Release:        1%{?dist}
Summary:        NTLMv1 authentication library
License:        LGPL-2.0-or-later
URL:            https://gitlab.com/gsasl/libntlm/
Source0:        https://download-mirror.savannah.gnu.org/releases/libntlm/libntlm-%{version}.tar.gz
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
A library for authenticating with Microsoft NTLMV1 challenge-response,
derived from Samba sources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
sed -i 's|$(install_sh) -c|$(install_sh) -pc|g' Makefile
%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libntlm-devel -f %{oreon_filedir}/libntlm-devel.list

%changelog

%autochangelog
