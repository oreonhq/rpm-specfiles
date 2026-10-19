%global source0_hash ab15b7fc5a96e8b4da1b76cc6c7935400879f8a54b0fcf94a947c02815f21006
%global git_user0 gtownsend
Name:           icon
Version:        9.5.25a
Release:        1%{?dist}
Summary:        Icon programming language
License:        LicenseRef-Fedora-Public-Domain
URL:            https://www2.cs.arizona.edu/icon/
Source0:        https://github.com/%{git_user0}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0:         icon-nostrip.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
%description

%package utils
Summary:        Icon utility programs
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description utils

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

make X-Configure name=linux
sed -i -e 's|CFLAGS = -O|CFLAGS = %{optflags} -std=gnu99|' Makedefs
sed -i -e 's|Igpx|Xpm|' Makedefs
make -j1 All
%check

make Test
%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 bin/icon[tx] %{buildroot}%{_bindir}
ln -s icont %{buildroot}%{_bindir}/icon
install -d -m0755 %{buildroot}%{_includedir}
install -p -m0644 lib/icall.h %{buildroot}%{_includedir}
install -d -m0755 %{buildroot}%{_libdir}/%{name}
install -p -m0644 -s bin/libcfunc.so %{buildroot}%{_libdir}/%{name}
install -p -m0644 lib/*.icn lib/*.u[12] %{buildroot}%{_libdir}/%{name}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 man/man1/* %{buildroot}%{_mandir}/man1
install -p -m0755 bin/[cfpvw]* %{buildroot}%{_bindir}
install -p -m0755 bin/xgamma %{buildroot}%{_bindir}/icon-xgamma
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n icon-utils -f %{oreon_filedir}/icon-utils.list

%changelog

%autochangelog
