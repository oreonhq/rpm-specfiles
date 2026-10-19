%global source0_hash 18db04b5931968f5cb9864e0009578a57ef449e8f2997bedbc829ce55f2dc2b1
Name:           libmawk
Version:        1.0.5
Release:        1%{?dist}
Summary:        Embed awk scripting language in any application written in C
License:        GPL-2.0-only
URL:            http://repo.hu/projects/libmawk
Source0:        http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This means the user gets libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
HTML documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./"configure" --prefix=%{_prefix} --libarchdir=%{_lib} --symbols \
  --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}"
%make_build
%install
%make_install LIBARCHDIR=%{buildroot}/%{_libdir} LIBPATH=%{buildroot}/%{_libdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmawk-devel -f %{oreon_filedir}/libmawk-devel.list
%files -n libmawk-doc -f %{oreon_filedir}/libmawk-doc.list

%changelog

%autochangelog
