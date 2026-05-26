Name:           npth
Version:        1.8
Release:        %autorelease
Summary:        The New GNU Portable Threads library
License:        LGPL-2.1-or-later
URL:            https://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source0:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2.sig
# Full dist signing keys (npth .sig files may carry multiple signatures)
Source2:        https://gnupg.org/signature_key.asc
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source3:        npth-config.1
# oreon url source checksums begin
%global source0_sha256 8bd24b4f23a3065d6e5b26e98aba9ce783ea4fd781069c1b35d149694e90ca3e
%global source0_file npth-1.8.tar.bz2
# oreon url source checksums end

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gnupg2

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/npth-1.8.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8bd24b4f23a3065d6e5b26e98aba9ce783ea4fd781069c1b35d149694e90ca3e" || { echo "oreon: Source0 SHA256 mismatch for npth-1.8.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
gpg --batch --dearmor --output %{_builddir}/gnupg-signature-keyring.gpg %{SOURCE2}
%{gpgverify} --keyring='%{_builddir}/gnupg-signature-keyring.gpg' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 %{S:3}
find %{buildroot} -name '*.la' -delete -print

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LIB
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_mandir}/man1/%{name}-config.1*
%{_datadir}/aclocal/%{name}.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8-1
- Prepare for Oreon 11 (RP1)
