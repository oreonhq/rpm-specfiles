%global source2_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash eb9314cf3867a438cb0fdd371125d44c57ba66086f152199ad5f40a9c9679acb
%global source0_hash 8bd24b4f23a3065d6e5b26e98aba9ce783ea4fd781069c1b35d149694e90ca3e
Name:           npth
Version:        1.8
Release:        1%{?dist}
Summary:        The New GNU Portable Threads library
License:        LGPL-2.1-or-later
URL:            https://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source0:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2.sig
Source2:        https://gnupg.org/signature_key.asc
Source3:        npth-config.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n npth-devel -f %{oreon_filedir}/npth-devel.list

%changelog

%autochangelog
