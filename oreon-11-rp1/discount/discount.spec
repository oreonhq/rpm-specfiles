%global somajor 2
# Old-style C + hand-written Makefile: LTO can fail linking; GCC 15 is stricter on conversions.
%global _lto_cflags %{nil}

Name:           discount
Version:        2.2.7
Release:        5%{?dist}
Summary:        C implementation of Markdown
License:        BSD-3-Clause
URL:            https://github.com/Orc/discount
Source0:        %{url}/archive/v%{version}/discount-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

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
%autosetup -p1


%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types -Wno-int-conversion -Wno-discarded-qualifiers"
./configure.sh \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --shared \
  --pkg-config
# pandoc_headers links -lmarkdown; build libmarkdown first so parallel make does not race
%{__make} %{?_smp_mflags} libmarkdown
%{__make} %{?_smp_mflags}


%install
%make_install install.everything DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_libdir}/libmarkdown.so.*


%files
%doc README*
%license COPYING
%{_bindir}/markdown
%{_bindir}/makepage
%{_bindir}/mkd2html
%{_bindir}/theme
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

%files -n libmarkdown
%{_libdir}/libmarkdown.so.%{somajor}*

%files -n libmarkdown-devel
%{_includedir}/mkdio.h
%{_libdir}/libmarkdown.so
%{_libdir}/pkgconfig/libmarkdown.pc
%{_mandir}/man3/*.3*


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.7-2
- Add discount and libmarkdown for KDE text stacks
