%global source0_hash 99f6db36d3fff6c99acd21d4c6096176d4ac8785eab319d0faf77ad995b8b7c5
%global somajor 2
%global _lto_cflags %{nil}
Name:           discount
Version:        3.0.2.0
Release:        1%{?dist}
Summary:        C implementation of Markdown
License:        BSD-3-Clause
URL:            https://github.com/Orc/discount
Source0:        https://github.com/Orc/%{name}/archive/refs/tags/v%{version}.tar.gz#/discount-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Discount is a Markdown parser written in C. This package also ships the
libmarkdown shared library used by many KDE components.

%package -n libmarkdown
Summary:        Shared library for discount Markdown
%description -n libmarkdown
libmarkdown shared object for applications linked against discount.

%package -n libmarkdown-devel
Summary:        Development files for libmarkdown
Requires:       libmarkdown%{?_isa} = %{version}-%{release}
%description -n libmarkdown-devel
Headers and pkg-config file for libmarkdown.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags} -Wno-incompatible-pointer-types -Wno-int-conversion -Wno-discarded-qualifiers"
./configure.sh \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --shared \
  --pkg-config
%{__make} %{?_smp_mflags} libmarkdown
%{__make} %{?_smp_mflags}
%install
sed -i '/ldconfig/d' librarian.sh
%make_install install.everything DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_libdir}/libmarkdown.so.*
%oreon_autofiles libmarkdown usr/*/lib*.so.*
%oreon_autofiles libmarkdown-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmarkdown -f %{oreon_filedir}/libmarkdown.list
%files -n libmarkdown-devel -f %{oreon_filedir}/libmarkdown-devel.list

%changelog

%autochangelog
