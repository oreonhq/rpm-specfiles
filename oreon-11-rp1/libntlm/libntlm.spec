%global source0_hash ce6569a47a21173ba69c990965f73eb82d9a093eb871f935ab64ee13df47fda1

Name:           libntlm
Version:        1.8
Release:        %autorelease
Summary:        NTLMv1 authentication library
License:        LGPL-2.0-or-later
URL:            https://gitlab.com/gsasl/libntlm/
Source0:        https://download-mirror.savannah.gnu.org/releases/libntlm/libntlm-%{version}.tar.gz
# https://download.savannah.nongnu.org/releases/libntlm/libntlm-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  make
Provides:       bundled(gnulib)

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

%autosetup

%build
%configure --disable-static
make %{?_smp_mflags}
sed -i 's|$(install_sh) -c|$(install_sh) -pc|g' Makefile

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%doc AUTHORS ChangeLog COPYING README THANKS
%{_libdir}/%{name}.so.*

%files devel
%doc COPYING 
%{_includedir}/ntlm.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
