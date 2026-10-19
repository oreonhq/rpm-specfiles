%global source0_hash e0fb5df9805a2e217fea92c03c65f9f65f5f6884ac5f470e6c79254f41d6d498
%global _libdir /usr/lib
%global obsrel 2.1
Name:           obs-build
Version:        20260910
Release:        1%{?dist}
Summary:        A generic package build script
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-build
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0501:      0501-Revert-Drop-shebang-line-from-openstack-console.patch
BuildArch:      noarch
Requires:       bash, perl-interpreter, binutils, tar
Requires:       gzip, bzip2, xz, zstd
Requires:       python3-websocket-client
Recommends:     perl(Archive::Tar)
Recommends:     /sbin/mkfs.ext3
Recommends:     /usr/bin/qemu-kvm
Recommends:     bsdtar
Recommends:     qemu-linux-user
Recommends:     zstd
Recommends:     perl(Config::IniFiles)
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Net::SSL)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     perl(YAML::LibYAML)
Requires:       perl(POSIX)
Provides:       build = %{version}-%{release}
Requires:       %{name}-mkbaselibs = %{version}-%{release}
# oreon:deps
BuildRequires:  (perl(YAML::PP) or perl(YAML::XS))
BuildRequires:  /usr/bin/prove
BuildRequires:  make
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  python3-devel
# /oreon:deps
%description
This package provides a script for building packages in a chroot environment.
It is commonly used with the Open Build Service as the engine for building
packages for a wide variety of distributions.

%package mkbaselibs
Summary:        Tools to generate base library packages
Provides:       build-mkbaselibs = %{version}-%{release}
AutoReq:        no
%description mkbaselibs
This package contains the parts which may be installed in the inner build
system for generating base library packages.

%package mkdrpms
Summary:        Tools to generate DeltaRPMs
Provides:       build-mkdrpms = %{version}-%{release}
Requires:       deltarpm
Requires:       %{name} = %{version}-%{release}
%description mkdrpms
This package contains the parts which may be installed in the inner build
system for generating DeltaRPM packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
pushd %{buildroot}%{_libdir}/build/configs/
touch default.conf
test -e default.conf
popd
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 build.1* %{buildroot}%{_mandir}/man1/
install -m 0644 buildvc.1* %{buildroot}%{_mandir}/man1/
install -m 0644 unrpm.1* %{buildroot}%{_mandir}/man1/
sed -e "s|#!/usr/bin/python|#!%{__python3}|" \
    -i %{buildroot}%{_libdir}/build/openstack-console
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n obs-build-mkbaselibs -f %{oreon_filedir}/obs-build-mkbaselibs.list
%files -n obs-build-mkdrpms -f %{oreon_filedir}/obs-build-mkdrpms.list

%changelog

%autochangelog
