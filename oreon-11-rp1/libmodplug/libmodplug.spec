%global source0_hash 457ca5a6c179656d66c01505c0d95fafaead4329b9dbaa0f997d00a3508ad9de
Name:           libmodplug
Version:        0.8.9.0
Release:        1%{?dist}
Epoch:          1
Summary:        Modplug mod music file format library
License:        LicenseRef-Fedora-Public-Domain
URL:            http://modplug-xmms.sourceforge.net/
Source0:        https://downloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.8.9.0-timiditypaths.patch
Suggests:      %{_sysconfdir}/timidity.cfg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for the Modplug mod music file format library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gcc-c++
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
sed -i -e 's/\r//g' ChangeLog

%build

%configure
%make_build V=1
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libmodplug-devel -f %{oreon_filedir}/libmodplug-devel.list

%changelog

* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.8.9.0-1
- Import from Fedora 43 dist-git for Oreon 11 RP1
